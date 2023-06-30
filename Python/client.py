import socket

server_ip = '127.0.0.1'
server_port = 12345

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    client_socket.connect((server_ip, server_port))

    message = input("Digite uma string")
    client_socket.sendall(message.encode())

    modified_message = client_socket.recv(1024).decode()
    print("String Modificada: ", modified_message)

except ConnectionRefusedError:
    print("A conexão não foi efetuada, erro ao conectar ao servidor")
 
finally:
    client_socket.close(); 