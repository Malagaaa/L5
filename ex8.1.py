# Vom considera un program care va prelucra temperaturile medii pentru fiecare oră din cele 31 de zile ale unei luni.
# Se va crea o matrice cu 31 linii și 24 coloane.
# Considerăm că temperaturile sunt scrise de către un alt proces care măsoară temperaturile respective.
# a. prima cerință este să determinați temperatura medie de la prânz pentru întreaga lună
# b. determinați cea mai înaltă temperatură medie pentru întreaga lună
# c. numărați câte zile au avut temperatura medie peste 20 de grade  

zile = 31
ore = 24
matrice = []
for z in range(zile):
    a = []
    for o in range(ore):
        a.append('-')
    matrice.append(a)
#print(matrice)
for z in range(zile):
    for o in range(ore):
        print(matrice[z][o], end = " ")
    print()   
# temperatura = [[0 for h in range(24)] for d in range(31)] # matricea pt 31 zile si 24 h/zi
# print(temperatura)

# temperaturaPranz = temperatura [12] # temperatura de la jum zilei


