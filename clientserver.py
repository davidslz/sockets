import socket

def run_client():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as cliente:

        server_address = ("127.0.0.1", 65432)

        #  creando la conexion con el servidor
        cliente.connect(server_address)


        #  se crea un loop para el envio de datos del cliente al servidor
        while True:
            mensaje = input("Ingresa el mensaje: ")
            cliente.send(mensaje.encode("utf-8")[:1024])
            #client.send(mensaje.encode("utf-8")[:1024])

            #  se recive el mensaje del servidor
            response = cliente.recv(1024)
            response = response.decode("utf-8")

            if response.lower() == "closed":
                break

            print(f"Respuesta del server: {response}")


    #  se cierra la conexion con el servidor, cerrando el socket del cliente
    #  cliente.close()
    print("conexion terminada")


run_client()