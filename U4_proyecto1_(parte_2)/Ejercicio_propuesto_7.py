lis_nom=[]
lis_ed=[]
while True:
    nom=input("Nombre del alumno: ")
    if nom == "-":
        break
    lis_nom.append(nom)
    ed=int(input("Introduce la edad: "))
    lis_ed.append(ed)
print("---------------")
for n,e in zip(lis_nom,lis_ed):
    if e >= 18:

        print(n,e)
print("----------")

maxi= max(lis_ed)
i= lis_ed.index(maxi)
print("El alumno mayor es:", lis_nom[i], maxi)