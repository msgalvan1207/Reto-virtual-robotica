from interface_t1.srv import MiServicio                                                      # CHANGE

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist, TwistStamped
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


        

        self.srv = self.create_service(MiServicio, 'miservicio', self.MiServicio_callback) 
        self.posx_deseado,self.posy_deseado=0,0
        self.posx,self.posy=0,0

        # CHANGE



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

        
        self.control_robot(str(ruta))


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