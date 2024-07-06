import socket
import threading


#   Con gethostname(), se obtiene el nombre del host donde esta el socket
# hostname = socket.gethostname()

#   Con gethostbyname(nombre), se obtiene la IP del host donde esta el socket
# ip = socket.gethostbyname(nombre)

def handle_client(client_socket, client_address):
    try:
        while True:
            #with client_socket:
            request = client_socket.recv(1024).decode("utf-8") # los datos recibidos por el cliente estan en una forma binario sin formato y los datos en la variable se decodifican en una secuencia de cadena de bytes

            if request.lower() == "close":
                client_socket.send("closed".encode("utf-8"))
                break

            print(f"Recibido: {request}")

            response = "Aceptado".encode("utf-8")
            client_socket.send(response)

    except Exception as e:
        print(f"Error en la conexion cliente: {e}")

    finally:
        #  despues de terminar la comunicacion con el cliente, se cierra el socket mediante el metodo close()
        client_socket.close()
        print(f"Conexion finalizada con {client_address[0]}:{client_address[1]}")


def run_server():
    try:
        #  creando un SOCKET INET (IPv4) con el protocolo TCP/IP
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:

        #server_address = (socket.gethostname(),65432)
            server_address = ("127.0.0.1", 65432)
            server.bind((server_address))


            #  El metodo listen(), especifica el numero maximo de conexiones no aceptadas en cola. Con el valor igual a 0 
            #  significa que sólo un cliente puede interactuar con el servidor y se rechazará un intento de conexión de cualquier 
            #  cliente realizado mientras el servidor está trabajando con otro cliente.

            #  Si especifica un valor mayor que 0, digamos 1, le dice al sistema operativo cuántos clientes se pueden poner en la cola 
            #  antes de que se llame al método de aceptación.
            server.listen(0)

            print(f"EL socket servidor {server_address[0]} escucha en el puerto {server_address[1]}")


            #  despues de aceptar la conexion con el cliente, se crea un loop infinito para la comunicacion del cliente a servidor
            while True:
                #  aceptar conexiones entrantes
                #  el metodo accept() devuelve una tupla donde "address" es una tupla de la IP y PUERTO del cliente
                client_socket, client_address = server.accept()

                print(f"Conexion aceptada de {client_address[0]}:{client_address[1]}")

                #  Se crea un nuevo hilo para crear diferentes clientes
                thread = threading.Thread(target=handle_client, args=(client_socket,client_address))
                thread.start()
                
                total_thread = threading.active_count()
                print(total_thread)

                size = threading.stack_size()
                print(size)

    except Exception as e:
        print(f"Error: {e}")

    finally:
        #server.close()
        print("Servidor cerrado")
        
run_server()