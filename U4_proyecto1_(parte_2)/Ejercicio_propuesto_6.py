num=int(input("Numero del mes: "))
dia=list(range(1,31)) #lista basica
meses=[" ","Enero","Febrero","Marzo","Abil","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"]

if num in (1,3,5,7,8,10,12):
    dia.append(31)
    print(meses[num],dia)
elif num in (4,6,9,11):
    print(meses[num],dia)
else:
    dia.pop()
    dia.pop()
    print(meses[num],dia)