import socket

postes = 4

server_ip = '127.0.0.1'
server_ports = [12345] #, 12346, 12347, 12348

luas = "crescente3, minguante3, quarto_crescente6, quarto_minguante6, nova0, grande_crescente12, grande_minguante12, cheia15"
nuvens = "nublado6, limpo15, chuva3 ou temporal0"

luas = [
    {
        name: "crescente",
        value: 3
    },

]

try:
    for port in server_ports:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        lua = ""
        while not lua:
            lua = input("Qual a fase da lua? (Crescente, Minguante, Quarto_crescente, Quarto_minguante, Nova, Grande_Crescente, Grande_minguante e Cheia): ")
            if lua.lower() not in luas:
                print("Entrada Inválida")
                lua = ""

        nuvem = ""
        while not nuvem:
            nuvem = input("Como está o céu? (Nublado, Limpo, Chuva ou Temporal): ")
            if nuvem.lower() not in nuvens:
                print("Entrada Inválida")
                nuvem = ""

        client_socket.connect((server_ip, port))

        message = lua + ";" + nuvem
        client_socket.sendall(message.encode())

        modified_message = client_socket.recv(1024).decode()
        lua, nuvem = modified_message.split(";")
        print("String Modificada (Porta", port, "):", lua, nuvem)

except ConnectionRefusedError:
    print("A conexão não foi efetuada, erro ao conectar ao servidor")

finally:
    client_socket.close()
