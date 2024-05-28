#!/usr/bin/env python3

import rclpy
from interface_t1.srv import MiServicio
from rclpy.node import Node

from geometry_msgs.msg import Twist
import random

import serial


class my_cliente(Node):

    def __init__(self):
        super().__init__('my_taller2_node')

        try:
            self.serialPort = "/dev/ttyACM0"
            self.get_logger().info('Intentando abrir puerto serial en: %s' % self.serialPort)
            self.serialCon = serial.Serial(self.serialPort, 9600, timeout=1)
            self.get_logger().info('Puerto serial abierto en: %s' % self.serialPort.name)
        except Exception as e:
            self.get_logger().info('Error al abrir puerto serial: %r' % e)
            self.serialPort = None
            self.serialCon = None

        self.cliente = self.create_client(MiServicio, 'miservicio')

        

        while not self.cliente.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Esperando por el servicio...')

        #self.publisher_ = self.create_publisher(Twist, '/turtlebot_cmdVel', 10)

        self.req=MiServicio.Request()

    def send_request(self, ruta):
        
        self.req.ruta=ruta

        self.future=self.cliente.call_async(self.req)


def coordinates(grooup_name):
   
    coords= [[6.4,-1.8],[-1,-5],[-2.5,-5.4],[3.8,-6.4],[1,3.9],[6.9,6.7],[-5.8,5.2]] 
    indice_aleatorio = random.randint(0, int(len(coords)) - 1)

    coordenadas_aleatorio =coords[indice_aleatorio]
    text=str(coordenadas_aleatorio[0])+","+str(coordenadas_aleatorio[1])
    return text

def main(args=None):

    rclpy.init(args=args)
    node = my_cliente()
    coord=coordinates('Grupo2')

    node.send_request(coord)
    print("Coordenadas a llegar:",coord)
    while rclpy.ok():
        rclpy.spin_once(node)

        if node.future.done():
            try:
                response=node.future.result()
            
            except Exception as e:
                node.get_logger().info(
                    'Service call failed %r' % (e,))
            else:
                print("BAZINGA")
                print(node.req.ruta, response.confirmacion)
                if node.serialCon and node.serialPort:
                    node.serialCon.write("run".encode("utf-8"))
                    node.get_logger().info('Enviando ruta al robot: %s' % node.req.ruta)
                    node.get_logger().info('Respuesta del robot: %s' % response.confirmacion)
            break

            
    node.destroy_node()
    rclpy.shutdown()




    

if __name__ == "__main__":
    main()

