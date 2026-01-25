# una tupla
tupla= ('a', 'b', 'c')

# Se pasa a lista
lis= list(tupla)

# Editamos la lista
lis.pop()
lis.append('d')
lis.append('e')

# se pasa a tupla otra vez
tupla= tuple(lis)

# confirmar que clase es
print(type(tupla))