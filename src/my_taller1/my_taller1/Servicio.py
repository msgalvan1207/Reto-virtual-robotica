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
        
        
        self.sim_callback_group = MutuallyExclusiveCallbackGroup()
        self.service_callback_group = MutuallyExclusiveCallbackGroup()
        
        #Iniciar variables con un valor inicial
        #Variables de posicón y orientación del robot
        self.posx=None
        self.posy=None
        self.orientation = None
        
        #Variables de posición deseados
        self.posx_deseado=None
        self.posy_deseado=None
        
        #Variables de datos del laser
        self.laser_data_list = []
        self.position_laser = []
        self.x_laser_transform = []
        self.y_laser_transform = []
        
        
        
        #Publicadores y subscriptores que se tienen que tener en cuenta:
        #Subscriptor de posición del robot
        self.pos_sub = self.create_subscription(Twist, '/turtlebot_position', self.pos_callback,10, callback_group=self.sim_callback_group)
        
        #Subscriptor de orientación del robot
        self.orientation_sub = self.create_subscription(Float32, '/turtlebot_orientation', self.orientation_callback,10, callback_group=self.sim_callback_group)
        
        #Subscriptor de laser
        self.laser_sub = self.create_subscription(Float32MultiArray, '/hokuyo_laser_data', self.laser_callback,10, callback_group=self.sim_callback_group)
        
        #Subscriptor del servicio
        self.srv = self.create_service(MiServicio, 'miservicio', self.MiServicio_callback, callback_group=self.service_callback_group) 
        
    
    def orientation_callback(self, msg):
        self.orientation = msg.data + math.pi
    
    
    def pos_callback(self, msg):
        self.posx = msg.linear.x
        self.posy = msg.linear.y
        
    
    def laser_callback(self, msg):
        self.laser_data_list = list(msg.data)
        if self.posx and self.posy and self.orientation:
            self.position_laser,self.x_laser_transform,self.y_laser_transform=self.descompress_data(self.laser_data_list,self.posx,self.posy,self.orientation)
    
    
    def descompress_data(self,lista_sensores,posx,posy,orientation):
        matrix = []
        x = []
        y = []
        for i in range(0,len(lista_sensores),2):
            lx, ly = lista_sensores[i], lista_sensores[i+1]
            fila = (lx,ly)
            xt,xy = self.transform_coordinates(lx,ly,orientation,posx,posy)
            x.append(xt)
            y.append(xy)
            matrix.append(fila)
    
        return matrix,x,y
    
    def transform_coordinates(self,lx,ly,orientation,posx,posy):
        cth = math.cos(orientation)
        sth = math.sin(orientation)
        x_transformated = posx - (cth * lx - sth * ly)
        y_transformated = posy - (sth * lx + cth * ly)
        
        return x_transformated,y_transformated


    def MiServicio_callback(self, request, response):

        ruta=request.ruta
        self.get_logger().info('Incoming request\na: %r' % (request.ruta))

        if len(request.ruta)>0:
            response.confirmacion = True
        else:
            response.confirmacion = False
        
        self.control_robot(str(ruta))

        return response


    def control_robot(self, group):

        self.posx_deseado,self.posy_deseado=group.split(',')
        self.posx_deseado=float(self.posx_deseado)
        self.posy_deseado=float(self.posy_deseado)
        timer_period = 0.1  # seconds
        
        self.publisher_ = self.create_publisher(Twist, '/turtlebot_cmdVel', 1)

        self.get_logger().info("Start navigation loop")

        while(self.apuntar_primero()):
            v,w, hold = self.calcular_comandos()
            msg = Twist()
            msg.linear.x = 0.0
            msg.angular.z = w 
            self.publisher_.publish(msg)
            time.sleep(timer_period*hold)

        while(self.ratio_separation() > 0.5):
            print(self.posx, self.posy)
            #print(math.degrees(self.orientation))
            v,w, hold = self.calcular_comandos()
            msg = Twist()
            msg.linear.x = v
            msg.angular.z = w 
            self.publisher_.publish(msg)
            time.sleep(timer_period*hold)
        
        msg.linear.x = 0.0
        msg.angular.z = 0.0
        self.publisher_.publish(msg)

    def calcular_comandos(self):
        error_x = self.posx_deseado - self.posx
        error_y = self.posy_deseado - self.posy
        error_angular = math.atan2(-error_y,error_x) - self.orientation
        error_angular = math.atan2(math.sin(error_angular), math.cos(error_angular))

        if self.obstaculo_adelante():
            return 0.0, 0.5, 15
        else:
            return 0.2, 0.1 * error_angular, 1
        
    
    def obstaculo_adelante(self):
        umbral_dist_frontal = 0.75
        for lx, ly in self.position_laser:
            distancia_obstaculo = math.sqrt(lx**2 + ly**2)
            angulo_obstaculo = math.atan2(ly,lx)
            if self.angulo_delante(angulo_obstaculo) and distancia_obstaculo < umbral_dist_frontal:
                return True
        return False
    

    def angulo_delante(self, angulo):
        return -math.pi/6 < angulo < math.pi/6

    def ratio_separation(self):
        r=((self.posx-self.posx_deseado)**2+(self.posy-self.posy_deseado)**2)**(0.5)
        return r



def main(args=None):
    rclpy.init(args=args)

    minimal_service_node = MinimalService()

    executor = MultiThreadedExecutor()
    executor.add_node(minimal_service_node)



    try:
        executor.spin()
    finally:
        minimal_service_node.destroy_node()
        executor.shutdown()
        rclpy.shutdown()

if __name__ == '__main__':
    main()