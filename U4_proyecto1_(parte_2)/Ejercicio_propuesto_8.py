from colorama import Fore
#listas
nombre = []
horas=[]
tot_ex =[]
print (Fore.CYAN + "--------------------------------")
while True:
    nom = input(Fore.WHITE + "- Nombre de los trabajadores "+ Fore.RED +"(finaliza con - ):" + Fore.WHITE + " ")
    if nom == "-":
        break
    nombre.append(nom)
    he= float(input(Fore.WHITE + "- Horas extras de los trabajadores: "))
    horas.append(he)
    print(Fore.CYAN + "--------------------------------")
for i,h in zip(nombre,horas):
    print("\t")
    print(Fore.GREEN + "--------------------------------")
    print("----- Total horas extras -------")
    print("--------------------------------")
    hex = float(h * 16.25)
    print (Fore.WHITE + f"---- Nombre: {i:<15} ---")
    print (f"---- Horas extras: {hex:<8} ----")
    print(Fore.CYAN + "--------------------------------")
    