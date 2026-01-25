list_u = [2, 8, 7, 6, 4]
list_d=[20, 80, 70, 60, 40]
list_c=[200, 800, 700, 600, 400]
list_m=[2000, 8000, 7000, 6000, 4000]
print("U  D  C   M")
for u,d,c,m in zip(list_u,list_d,list_c,list_m):
    print(u,d,c,m)