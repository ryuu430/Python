while True:
    print("------------------------------------")
    nom=input("Escrive el nombre y los apellidos: ")
    ed=input("Ecrive tu edad: ")
    tel=input("Escrive tu telefono: ")
    nick=input("Escrive tu nickname: ")
    print("------------------------------------")
# contar palabras
    pa=nom.split()
    
# Nombre en mayusculas
    nom_ma=nom.title()

# Validar nombre y apellidos
    if len(pa) == 3 and nom == nom_ma:
        print("Nombre valido")

        # Validar edad
        if ed.isdigit():
            print("Edad valida")

            # Validar telefono
            if tel.isdigit() and len(tel) == 9:
                print("Telefono valido")

                # Validar nickname
                if nick.isalnum():
                    print("Nickname valido")
                    print("------------------------------------")
                    break
                else:
                    print("Nickname")
                    print("------------------------------------")
            else:
                print("Telefono invalido")
                print("------------------------------------")
        else:
            print("Edad no valida")
            print("------------------------------------")
    else:
        print("Nombre invalido")
        print("------------------------------------")

        

            

                