from interface_t1.srv import MiServicio                                                      # CHANGE

import rclpy
import math
from rclpy.node import Node
from geometry_msgs.msg import Twist, TwistStamped
from std_msgs.msg import Float32, Float32MultiArray
from abc import ABC, abstractmethod
from rclpy.qos import qos_profile_system_default


import atexit
import sys

import time
import threading
import random

class MinimalService(Node):

    def __init__(self):
        super().__init__('minimal_service')
                
        print("Servicio")
        
        
        #Iniciar variables con un valor inicial
        #Variables de posicón y orientación del robot
        self.posx=0
        self.posy=0
        self.theta = 0
        
        #Variables de posición deseados
        self.posx_deseado=0
        self.posy_deseado=0
        
        #Variables de datos del laser
        self.laser_data_list = []
        self.position_laser = []
        self.x_laser_transform = []
        self.y_laser_transform = []
        
        
        
        #Publicadores y subscriptores que se tienen que tener en cuenta:
        #Subscriptor de posición del robot
        self.pos_sub = self.create_subscription(Twist, '/turtlebot_position', self.pos_callback)
        
        #Subscriptor de orientación del robot
        self.orientation_sub = self.create_subscription(Float32, '/turtlebot_orientation', self.orientation_callback)
        
        #Subscriptor de laser
        self.laser_sub = self.create_subscription(Float32MultiArray, '/hokuyo_laser_data', self.laser_callback)
        
        #Subscriptor del servicio
        self.srv = self.create_service(MiServicio, 'miservicio', self.MiServicio_callback) 
        
    
    def orientation_callback(self, msg):
        self.theta = msg.data + math.pi
    
    
    def pos_callback(self, msg):
        self.posx = msg.linear.x
        self.posy = msg.linear.y
        
    
    def laser_callback(self, msg):
        self.laser_data_list = list(msg.data)
        self.position_laser,self.x_laser_transform,self.y_laser_transform=self.descompress_data(self.laser_data_list,self.posx,self.posy,self.theta)
        
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


    def MiServicio_callback(self, request, response):

        ruta=request.ruta
        print("Servicio")
        print(ruta)
        


        if len(request.ruta)>0:
            response.confirmacion = True
        else:
            response.confirmacion=False  
                                                          # CHANGE
        self.get_logger().info('Incoming request\na: %r' % (request.ruta))  # CHANGE

        
        #self.control_robot(str(ruta))


        return response

 
    def control_robot(self, group):

        self.posx_deseado,self.posy_deseado=group.split(',')
        self.posx_deseado=float(self.posx_deseado)
        self.posy_deseado=float(self.posy_deseado)
        timer_period = 0.1  # seconds
        print("posx_deseado: %f posy_deseado: %f" % (self.posx_deseado, self.posy_deseado))
        self.publisher_ = self.create_publisher(Twist, '/turtlebot_cmdVel', 1)
        while (self.ratio_separation() > 0.5):
            print("x_deseado: %f y_deseado: %f x_actual: %f y_actual: %f" % (self.posx_deseado,self.posy_deseado,self.posx,self.posy))
            #Hacer codigo de moviemiento de roboot , recordar suscribirse a los topicos de '/turtlebot_position', /turtlebot_orientation' y '/hokuyo_laser_data''
            
            v,w=0.0,0.0 
            msg = Twist()
            msg.linear.x = v
            msg.angular.z = w 

            self.publisher_.publish(msg)
            time.sleep(timer_period)
            
    def ratio_separation(self):
        r=((self.posx-self.posx_deseado)**2+(self.posy-self.posy_deseado)**2)**(0.5)
        return r
        



def main(args=None):
    rclpy.init(args=args)

    minimal_service = MinimalService()

    rclpy.spin(minimal_service)

    rclpy.shutdown()

if __name__ == '__main__':
    main()