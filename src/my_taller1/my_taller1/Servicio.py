from interface_t1.srv import MiServicio


import rclpy
import math
import heapq
from rclpy.node import Node
from rclpy.executors import MultiThreadedExecutor
from rclpy.callback_groups import ReentrantCallbackGroup, MutuallyExclusiveCallbackGroup
from geometry_msgs.msg import Twist, TwistStamped
from std_msgs.msg import Float32, Float32MultiArray
from abc import ABC, abstractmethod
from rclpy.qos import qos_profile_system_default


import atexit
import sys

import time
import threading
import random

import cv2
import numpy as np


class MinimalService(Node):

    def __init__(self):
        super().__init__('minimal_service')
                
        self.get_logger().info('Minimal Service has been started')
        
        #Variables de callback Groups (1 por callback, se utilizan para que los callbacks no se bloqueen entre si y par que un mismo callback no se ejecute al mismo tiempo que si mismo)
        
        
        self.pos_callback_group = MutuallyExclusiveCallbackGroup()
        self.orientation_callback_group = MutuallyExclusiveCallbackGroup()
        self.laser_callback_group = MutuallyExclusiveCallbackGroup()
        self.service_callback_group = MutuallyExclusiveCallbackGroup()
        
        #Iniciar variables con un valor inicial
        #Variables de posicón y orientación del robot
        self.posx=None
        self.posy=None
        self.theta = None
        
        #Variables de posición deseados
        self.posx_deseado=None
        self.posy_deseado=None
        
        #Variables de datos del laser
        self.laser_data_list = []
        self.position_laser = []
        self.x_laser_transform = []
        self.y_laser_transform = []
    
        #Variables de navegacion
        self.map = {}
        self.grid_size = 0.1
        self.current_path = []
        
        
        
        #Publicadores y subscriptores que se tienen que tener en cuenta:
        #Subscriptor de posición del robot
        self.pos_sub = self.create_subscription(Twist, '/turtlebot_position', self.pos_callback,10, callback_group=self.pos_callback_group)
        
        #Subscriptor de orientación del robot
        self.orientation_sub = self.create_subscription(Float32, '/turtlebot_orientation', self.orientation_callback,10, callback_group=self.orientation_callback_group)
        
        #Subscriptor de laser
        self.laser_sub = self.create_subscription(Float32MultiArray, '/hokuyo_laser_data', self.laser_callback,10, callback_group=self.laser_callback_group)
        
        #Subscriptor del servicio
        self.srv = self.create_service(MiServicio, 'miservicio', self.MiServicio_callback, callback_group=self.service_callback_group) 
        
    
    def orientation_callback(self, msg):
        #self.get_logger().info("orientation callback")
        self.theta = msg.data - math.pi
    
    
    def pos_callback(self, msg):
        #self.get_logger().info("position callback")
        self.posx = msg.linear.x
        self.posy = msg.linear.y
        
    
    def laser_callback(self, msg):
        #self.get_logger().info("Laser data callback invoqued")
        self.laser_data_list = list(msg.data)
        #self.position_laser,self.x_laser_transform,self.y_laser_transform=self.descompress_data(self.laser_data_list,self.posx,self.posy,self.theta)
        self.update_map(self.laser_data_list,self.posx,self.posy,self.theta)
        #self.recalculate_path()
        
    def update_map(self, lista_sensores,posx,posy,orientation):
        for i in range(0,len(lista_sensores),2):
            lx = lista_sensores[i]
            ly = lista_sensores[i+1]
            #self.map[(int(lx//self.grid_size), int(ly//self.grid_size))] = 1

            #xt,xy = self.transform_coordinates(lx,ly,orientation,posx,posy)
            #self.map[int(xt//self.grid_size),int(xy//self.grid_size)] = 1
            self.addPointGlobal(lx,ly,posx,posy,orientation)

    
    def addPointGlobal(self, x, y, posx, posy, orientation):
        rotation_matrix = np.array([[math.cos(orientation), -math.sin(orientation)], [math.sin(orientation), math.cos(orientation)]])
        translation_vector = np.array([posx, posy])
        global_coordinates = np.dot(rotation_matrix, np.array([x, y])) + translation_vector
        self.map[(int(global_coordinates[0]//self.grid_size), int(global_coordinates[1]//self.grid_size))] = 1
    
    
    def descompress_data(self,lista_sensores,posx,posy,orientation):
        matrix = []
        x = []
        y = []
        for i in range(0,len(lista_sensores),2):
            fila = []
            fila.append(lista_sensores[i])
            fila.append(lista_sensores[i+1])
            lx = lista_sensores[i]+posx
            ly = lista_sensores[i+1]+posy
            xt,xy = self.transform_coordinates(lx,ly,orientation,posx,posy)
            
            x.append(xt)
            y.append(xy)
            matrix.append(fila)
    
        return matrix,x,y
    
    def transform_coordinates(self,lx,ly,orientation,posx,posy):
        cth = math.cos(orientation)
        sth = math.sin(orientation)
        x_transformated = (cth * lx - sth * ly) +posx
        y_transformated = (sth * lx + cth * ly) +posy
        
        return x_transformated,y_transformated
    
    def a_star(self,start,goal):
        open_set = []
        heapq.heappush(open_set,(0,start))
        came_from = {}
        g_score = {start:0}
        f_score = {start:self.heuristic(start,goal)}
        
        while open_set:
            current = heapq.heappop(open_set)[1]
            
            if current == goal:
                path = []
                while current in came_from:
                    path.append(current)
                    current = came_from[current]
                path.append(start)
                path.reverse()
                return path
            
            neighbors = self.get_neighbors(current)
            for neighbor in neighbors:
                tentative_g_score = g_score[current] + 1
                
                if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g_score
                    f_score[neighbor] = tentative_g_score + self.heuristic(neighbor,goal)
                    heapq.heappush(open_set,(f_score[neighbor],neighbor))
        
        return []
    
    def heuristic(self,a,b):
        return abs(a[0]-b[0]) + abs(a[1]-b[1])
    
    def get_neighbors(self,node):
        neighbors = []
        directions = [(0,1), (1,0), (0,-1), (-1,0)]
        for direction in directions:
            neighbor = (node[0]+direction[0],node[1]+direction[1])
            if neighbor not in self.map:
                neighbors.append(neighbor)
        return neighbors
    
    def recalculate_path(self):
        #print('invoqued recalculate_path')
        try:
            start = (int(self.posx//self.grid_size),int(self.posy//self.grid_size))
            goal = (int(self.posx_deseado//self.grid_size),int(self.posy_deseado//self.grid_size))
            #print(start, goal, (self.posx, self.posy), (self.posx_deseado, self.posy_deseado))
            self.current_path = self.a_star(start,goal)
            #print(self.current_path)
            #print('try function')
        except:
            self.current_path = []
            #print('catch except')
            


    def MiServicio_callback(self, request, response):

        ruta=request.ruta
        self.get_logger().info('Incoming request\na: %r' % (request.ruta))
        


        if len(request.ruta)>0:
            response.confirmacion = True
        else:
            response.confirmacion=False # CHANGE

        
        self.control_robot(str(ruta))


        return response


    def control_robot(self, group):

        self.posx_deseado,self.posy_deseado=group.split(',')
        self.posx_deseado=float(self.posx_deseado)
        self.posy_deseado=float(self.posy_deseado)
        timer_period = 0.1  # seconds
        #self.get_logger().info("posx_deseado: %f posy_deseado: %f" % (self.posx_deseado, self.posy_deseado))
        self.publisher_ = self.create_publisher(Twist, '/turtlebot_cmdVel', 1)
        
        
        while(self.ratio_separation() > 0.5):
            #self.get_logger().info("while loop in service callback")
            
            self.recalculate_path()
            print(self.current_path, math.degrees(self.theta)%360)
            
            v,w=0.0,0.0 
            msg = Twist()
            msg.linear.x = v
            msg.angular.z = w 
            self.publisher_.publish(msg)
            time.sleep(timer_period)
        
        
            
    def ratio_separation(self):
        r=((self.posx-self.posx_deseado)**2+(self.posy-self.posy_deseado)**2)**(0.5)
        return r
    


def displayMapRealtime(matrix, Node):
	map_display = cv2.resize(matrix, (900,900), interpolation = cv2.INTER_NEAREST)
	map_display = cv2.cvtColor(map_display, cv2.COLOR_GRAY2RGB)
	cv2.imshow("Map", map_display)
	cv2.waitKey(1)


def displayThread(Node):
    while Node:

        matrix = 255*np.ones((300,300), dtype = np.uint8)
        if Node.posx and Node.posy:
            matrix[int(Node.posx//Node.grid_size)+100][int(Node.posy//Node.grid_size)+100] = 1
        for pos in list(Node.map):
            matrix[pos[0]+100][pos[1]+100] = Node.map[pos]
        displayMapRealtime(matrix, Node)
        time.sleep(1 /30.0)



def main(args=None):
    rclpy.init(args=args)

    minimal_service_node = MinimalService()

    executor = MultiThreadedExecutor()
    executor.add_node(minimal_service_node)
    
    thread = threading.Thread(target=displayThread, args=(minimal_service_node,), daemon=True)
    
    thread.start()

    try:
        executor.spin()
    finally:
        minimal_service_node.destroy_node()
        executor.shutdown()
        rclpy.shutdown()

if __name__ == '__main__':
    main()