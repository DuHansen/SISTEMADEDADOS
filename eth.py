import sqlite3,os, time,winsound

class Manager:
    def __init__(self):
        self.name = ""
        self.phone = ""
        self.address = ""
    
    def add(self):
        running = True
        while running:
            os.system("cls")
            print("---------------Adicione um novo contato-----------------")
            print("PRECIONE A TECLA SHIFT + Q PARA CANCELAR")
            print()
            

            temp_name = input("Name: ")
            if len(temp_name)!= 0 and temp_name != "Q".upper(): #Utilizando IF para fazer uma verificação que irá bloquear informação vazia .upper conecta ao banco
                db = sqlite3.connect("connection.sqlite3")
                cursor = db.cursor()
                cursor.execute("SELECT Name FROM informacoes")
                results = cursor.fetchall()
                for i in results:
                    if temp_name in i:
                        print("CONTATO EXISTENTE")
                        time.sleep(3)
                        self.add()
                self.name = temp_name
                temp_name = ""

                time.sleep(0.20)
                
                self.phone = input("Phone :")

                time.sleep(0.20)

                self.address = input("Address :")
                
                cursor.execute("""INSERT INTO  informacoes\
                                (Name, Phone, Address)VALUES(?,?,?)""",\
                                (self.name, self.phone, self.address))
                db.commit()
                add_more = input("DESEJA ADICIONAR OUTRO CONTATO ? (Y/N) :")
                if add_more =="y" .lower():
                    continue
                else:
                    db.close()
                    running = False
                    print("Fechando o menu")
                    time.sleep(2)
                    self.menu()

            elif temp_name =="Q".upper():

                print("Fechando o menu")
                time.sleep(2)
                self.menu()
            else:
                winsound.Beep(3000,100)
                winsound.Beep(3000,100)
                
                print("FAVOR PREENCHER TODOS OS CAMPOS")
                time.sleep(3)
                self.add()


    def uptade(self):
        print()
        print("******************* ATUALIZAR CADASTROS ************************")
        print()
        name = input("DIGITE O NOME DO CLIENTE PARA ATUALIZAR =")
        confirm = input("TENHA CERTEZA ? (y/n):")
        if confirm == "y".lower():
            db = sqlite3.connect("connection.sqlite3")
            cursor = db.cursor()
            phone_update = input("ATUALIZAR TELEFONE ? (y/n):")
            if phone_update =="y".lower():
                phone = input("DIGITE O NUMERO DE TELEFONE ? :")

                cursor.execute("UPDATE informacoes SET Phone = ? WHERE Name =?",(phone,name))
                db.commit()
                print("CADASTRO ATUALIZADO COM SUCESSO")
                time.sleep(3)

            address_update = input("ATUALIZAR ENDERECO ? (y/n):")
            if address_update =="y".lower():
                address = input("DIGITE O ENDRECO PARA ATUALIZAR ? :")

                cursor.execute("UPDATE informacoes SET Address = ? WHERE Name =?",(address,name))
                db.commit()
                time.sleep(3)
            if phone_update !="y" .lower() and address_update !="y" .lower():
                print("SAINDO DO MENU PRINCIPAL, SEM FAZER ATUALIZACOES")
                time.sleep(3)
                self.menu()
                print("ENDERECO ATUALIZADO COM SUCESSO")
            db.close()
            time.sleep(3)
            self.menu()
        else:
            print("SAINDO DO MENU PRINCIPAL, SEM FAZER ATUALIZACOES")
            time.sleep(3)
            self.menu()


    def remove(self):
        print()
        print("******************* DELETAR CADASTROS ************************")
        print()
        name = input("DIGITE O NOME DO CLIENTE PARA DELETAR")
        confirm = input("TENHA CERTEZA ?(y/n)")
        if confirm == "y".lower():
            db = sqlite3.connect("connection.sqlite3")
            cursor = db.cursor()
            cursor.execute("DELETE FROM informacoes WHERE Name = ?", (name,))
            db.commit()
            print("CADASTRO DELETADO COM SUCESSO")
            time.sleep(3)
            self.menu()
        else:
            print("SAINDO DO MENU PRINCIPAL")
            time.sleep(3)
            self.menu()


    def get_list(self):
        count = 0
        count_2 = 0
        db = sqlite3.connect("connection.sqlite3")
        cursor = db.cursor()
        os.system("cls")
        print("-------------CONTATOS---------------")
        

        time.sleep(0.50)
        cursor.execute("SELECT Name, Phone, Address FROM informacoes")
        results = cursor.fetchall()
        for row in results:
            time.sleep(0.50)
            count += 1
            count_2 += 1
            print(count_2, row)
            if count == 5:
                print()
                input("PRECIONE QUALQUER TECLA PARA CONTINUAR")
                
                count = 0 
            print()
        print()
        print("FINAL DOS RESULTADOS")
        db.close()
        print()
        print("PRECIONE QUALQUER TECLA PARA CONTINUAR")
        option = input("APERTE (A)ATUALIZAR, (D)DELETAR, (M)MENU :")
        if option == "a".lower():
            self.uptade()
            
        elif option == "d".lower():
            self.remove()
            
        elif option == "m".lower():
            self.menu()


    def terminate(self):
        confirm = input("DESEJA REALMENTE SAIR DO SISTEMA?(y/n) :")
        if confirm == "y".lower():
            print("SAINDO DO SISTEMA")
            winsound.Beep(3000,50)
            winsound.Beep(3000,50)
            winsound.Beep(3000,50)
            winsound.Beep(3000,50)
            time.sleep(0.05)
            print("............")
            time.sleep(0.05)
            print("........")
            time.sleep(0.05)
            print("....")
            time.sleep(0.05)
            print(".")
            exit()
        else:
            print("SAINDO DO MENU PRINCIPAL")
            time.sleep(0.05)
            self.menu()


    def menu(self):
        os.system("cls")
        winsound.Beep(2000,50)
        print("-----------MENU------------")
        time.sleep(0.05)
        print("1: Add")
        time.sleep(0.05)
        print("2: Remove")
        time.sleep(0.05)
        print("3: Uptade")
        time.sleep(0.05)
        print("4: List")
        time.sleep(0.05)
        print("5: Terminate")
        print()

        opcao = input("Selecione uma opção :")
        if opcao == "1":
            self.add()
        elif opcao == "2":
            self.remove()
        elif opcao == "3":
            self.uptade()
        elif opcao == "4":
            self.get_list()
        elif opcao == "5":
            self.terminate()
        
        else:
            winsound.Beep(2500,100)
            print("ERROR,Tente Novamente ")
            time.sleep(2)
    

    def main(self):
        os.system("cls")
        if os.path.isfile("connection.sqlite3"):
            db = sqlite3.connect("connection.sqlite3")
            time.sleep(3)
            winsound.Beep(2000,50)
            print()
            print("Conexão bem sucetida")
            time.sleep(3)
            self.menu()
        else:
            print("Não foi possivel conectar")
            print()
            time.sleep(3)
            winsound.Beep(2000,50)

            print("Creating new connection file")
            time.sleep(3)
            db = sqlite3.connect("connection.sqlite3")

            cursor = db.cursor()
            cursor.execute("""CREATE TABLE informacoes
                            (Name TEXT NOT NULL, Phone TEXT, Address TEXT)""")
            
           

            winsound.Beep(2000,50)
            print()

            print("Conexão criada com sucesso")
            print("Conectado com sucesso")
            time.sleep(3)
            self.menu()
            
        self.menu()

contacts_manager = Manager()
contacts_manager.main()




