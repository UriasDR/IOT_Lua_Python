import socket

postes = 4

server_ip = '127.0.0.1'
server_ports = [12345, 12346, 12347, 12348] #, 12346, 12347, 12348

luas = "crescente3, minguante3, quarto_crescente6, quarto_minguante6, nova0, grande_crescente12, grande_minguante12, cheia15"
luasVet = ["crescente", "minguante", "quarto_crescente", "quarto_minguante", "nova", "grande_crescente", "grande_minguante", "cheia"]
nuvens = "nublado6, limpo15, chuva3 ou temporal0"

nuvensVet = ["nublado", "limpo", "chuva" , "tempestade"]

lua = ""
while not lua:
        lua = input("Qual a fase da lua? (Crescente, Minguante, Quarto_crescente, Quarto_minguante, Nova, Grande_Crescente, Grande_minguante e Cheia): ")
        if lua.lower() not in luasVet:
                print("Entrada Inválida")
                lua = ""
        nuvem = ""
        while not nuvem:
            nuvem = input("Como está o céu? (Nublado, Limpo, Chuva ou Tempestade): ")
            if nuvem.lower() not in nuvensVet:
                print("Entrada Inválida")
                nuvem = ""

try:
    for port in server_ports:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        

        client_socket.connect((server_ip, port))

        Lua_Nuvem = lua + ";" + nuvem
        client_socket.sendall(Lua_Nuvem.encode())

        message_recieved = client_socket.recv(1024).decode()
        print(message_recieved)

except ConnectionRefusedError:
    print("A conexão não foi efetuada, erro ao conectar ao servidor")

finally:
    client_socket.close()
