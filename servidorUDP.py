import socket
import time
from itertools import count
from multiprocessing import Process 

'''
Declarar variables globales.
'''
counter = count(1)  

'''
Función que inicializa un servidor UDP. Espera infinitamente una respuesta.
'''
def servidorUDP():
    # Declarar variables locales
    localIP = "127.0.0.1"
    localPort = 20001
    bufferSize = 1024
    msgFromServer = "Mensaje recibido"
    bytesToSend = str.encode(msgFromServer)
    # Crear socket y conectarlo al IP y el puerto
    UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    UDPServerSocket.bind((localIP, localPort))
    print("Servdor UDP inicializado. Esperando datos de un cliente.")
    # Recibir datos de clientes
    while(True):
        # Esperar a recibir datos
        bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)
        message = bytesAddressPair[0]
        address = bytesAddressPair[1]
        # Imprimir mensaje y dirección del cliente
        clientMsg = "Mensaje del cliente:{}".format(message)
        clientIP  = "Dirección IP del cliente:{}".format(address)
        print("\n",clientMsg)
        print(clientIP,"\n")
        # Enviarle respuesta al cliente
        UDPServerSocket.sendto(bytesToSend, address)

'''
Función que cuenta infinitamente, de 5 en 5, utilizado para determinar por cuánto tiempo se ha tenido encendido el servidor.
'''
def contador():
    while True:
        time.sleep(5)
        next(counter)
        next(counter)
        next(counter)
        next(counter)
        print("El servidor ha estado encendido por",next(counter),"segundos.")

'''
Utiliza multiprocesamiento para asegurar que haya un "timeout" del servidor
'''
if __name__ == '__main__':
    # El proceso espera bastante tiempo, entonces aplicamos un "timeout" de 10 segundos 
    counter = count(1)    
    p1 = Process(target=servidorUDP, name='Process_servidorUDP')
    p2 = Process(target=contador, name='Process_contador')
    p1.start()
    p2.start()
    p1.join(timeout=30)
    p2.join(timeout=30)
    p1.terminate()
    p2.terminate()
    # Revisar código de salida
    if (p1.exitcode is None) or (p2.exitcode is None):
        print(f'Ha sido un minuto desde que se inicializó el servidor. ¡El proceso {p1} se terminó!')
