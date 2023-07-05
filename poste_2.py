import socket

server_ip = '127.0.0.1'
server_port = 12346

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    server_socket.bind((server_ip, server_port))
    print("Servidor pronto para receber a conexão")

    server_socket.listen(1)  

    while True:
        client_socket, client_address = server_socket.accept()
        print("Conexão estabelecida com", client_address)

        request = client_socket.recv(1024).decode()
        lua, nuvem = request.split(";")
        lua = lua.lower();
        nuvem = nuvem.lower();
        
        soma = 0;

        print(lua, nuvem)
        luaValue = 0;
        nuvemValue = 0;
        Visibility = 0;
        
        Output = "";
        
        # crescente 3, minguante 3, quarto_crescente 6, quarto_minguante 6, nova 0, grande_crescente 12, grande_minguante 12, cheia 15
        
        # "nublado 6, limpo 15, chuva 3 ou tempestade 0"
        
        if(lua == "crescente" or  lua == "minguante"):
            luaValue = 3;
        elif(lua == "quarto_crescente" or lua == "quarto_minguante"):
            luaValue = 6;
        elif(lua == "nova"):
            luaValue = 0;
        elif(lua == "grande_crescente" or lua == "grande_minguante"):
            luaValue = 12;
        elif(lua == "cheia"):
            luaValue = 15;
            
        if(nuvem == "nublado"):
            nuvemValue = 6;
        elif(nuvem == "limpo"):
            nuvemValue = 15;
        elif(nuvem == "chuva"):
            nuvemValue = 3;
        elif(nuvem == "tempestade"):
            nuvemValue = 0;
        
        Visibility = luaValue + nuvemValue;
        print(luaValue, nuvemValue)
        
        Energy = ""
        for i in range(Visibility // 3):
            Energy += "🔆"
            
        if(Energy == ""): Energy += "🎇"

        if Visibility >= 0 and Visibility < 10:
            Output = "Baixa Visibilidade, Energia poupada: " + Energy + "\nConsumo de energia elevado."
        elif Visibility >= 10 and Visibility <= 21:
            Output = "Visibilidade Média, Energia poupada:" + Energy + "\nConsumo de energia moderado."
        elif Visibility > 21 and Visibility <= 30:
            Output = "Visibilidade Alta, Energia poupada: " + Energy + "\nConsumo de energia reduzido."
        else:
            Output = "Erro"
        
        message = Output

        client_socket.send(message.encode())

        client_socket.close()

except socket.error as e:
    print("Erro durante a execução do servidor:", str(e))

finally:
    server_socket.close()