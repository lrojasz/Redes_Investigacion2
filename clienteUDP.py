import socket

# Declaración de variables
msgFromClient       = "Hola Servidor!"
serverAddressPort   = ("127.0.0.1", 20001)
bufferSize          = 1024

# Tomar entrada del usuario
msgFromClient = input("Ingrese el mensaje que desea enviarle al servidor:")
if (len(msgFromClient) >= bufferSize):
    print("El mensaje es demasiado largo. Se va a enviar el mensaje por defecto: 'Hola Servidor!'")
    msgFromClient = "Hola Servidor!"

# Codificar el mensaje
bytesToSend = str.encode(msgFromClient)

# Hacer socket UDP
UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
# Enviar mensaje al cliente
UDPClientSocket.sendto(bytesToSend, serverAddressPort)

# Recibir e imprimir mensaje de recibido del servidor
msgFromServer = UDPClientSocket.recvfrom(bufferSize)
msg = "Message from Server {}".format(msgFromServer[0])
print(msg)