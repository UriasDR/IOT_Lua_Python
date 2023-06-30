import socket

server_ip = '127.0.0.1'
server_port = 12347

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    server_socket.bind((server_ip, server_port))
    print("Servidor pronto para receber a conexão")

    server_socket.listen(1)  

    while True:
        client_socket, client_address = server_socket.accept()
        print("Conexão estabelecida com", client_address)

        message = client_socket.recv(1024).decode()

        modified_message = message.upper()

        client_socket.send(modified_message.encode())

        client_socket.close()

except socket.error as e:
    print("Erro durante a execução do servidor:", str(e))

finally:
    server_socket.close()