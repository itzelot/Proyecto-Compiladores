#                 EQUIPO 11
#       Espinosa Castro Heili Yamilit
#            Ortiz Tellez Itzel
#       Ramos Rodriguez Wendy Ariadna

import math 

inst = []
param = []
pc = 0
ac = 0
memDatos = {}
archivo = open("prueba13.txt", "r")
for renglon in archivo:
    datos = renglon.split()
    if (len(datos)>0):
        inst.append(datos[0])
        param.append(datos[1][:-1])
archivo.close()

while (inst[pc]!="END"):
    print ("PC: ", pc, "  AC: ",ac," inst: ", inst[pc], "  parametro: ", param[pc]) 
    if (inst[pc]=="LDV"):
        ac = int(param[pc])
        pc = pc + 1
        
    elif (inst[pc]=="STA"):
        memDatos[int(param[pc])] = ac
        pc = pc + 1
        
    elif (inst[pc]=="LDA"):
        ac = memDatos[int(param[pc])]
        pc = pc + 1
        
    elif (inst[pc]=="IN1"):
        val = int(input("Escriba un entero: "))
        memDatos[int(param[pc])] = val
        pc = pc + 1
        
    elif (inst[pc]=="IN2"):
        val = float(input("Escriba un flotante: "))
        memDatos[int(param[pc])] = val
        pc = pc + 1
        
    elif (inst[pc]=="IN3"):
        val = (input("Escriba un char: "))
        if (len(val) != 1):
            print("No es un char")
            break
        else:
            memDatos[int(param[pc])] = val
            pc = pc + 1
        
    elif (inst[pc]=="IN4"):
        val = str(input("Escriba una cadena: "))
        memDatos[int(param[pc])] = val
        pc = pc + 1
        
    elif (inst[pc]=="IN5"):
        val = memDatos[int(param[pc])]
        print("El valor ENTERO ingresado es: ")
        print(memDatos[int(param[pc])])
        pc = pc + 1
        
    elif (inst[pc]=="IN6"):
        val = memDatos[int(param[pc])]
        print("El valor FLOTANTE ingresado es: ")
        print(val)
        pc = pc + 1
        
    elif (inst[pc]=="IN7"):
        val = memDatos[int(param[pc])]
        print("El valor CHAR ingresado es: ")
        print(val)
        pc = pc + 1
        
    elif (inst[pc]=="IN8"):
        val = memDatos[int(param[pc])]
        print("El valor STRING ingresado es: ")
        print(val)
        pc = pc + 1
        
    elif (inst[pc]=="IN9"):
        print(str(input("Escribe una cadena: ")))
        pc = pc + 1
        
    elif (inst[pc]=="ADD"):
        ac = ac + memDatos[int(param[pc])]       
        pc = pc + 1
        
    elif (inst[pc]=="SUB"):
        ac = ac - memDatos[int(param[pc])]       
        pc = pc + 1
        
    elif (inst[pc]=="MUL"):
        ac = ac * memDatos[int(param[pc])]
        pc = pc + 1
        
    elif (inst[pc]=="DIV"):
        ac = ac / memDatos[int(param[pc])]
        pc = pc + 1
        
    elif (inst[pc]=="SIN"):
        ac = math.sin(memDatos[int(param[pc])])
        pc = pc + 1
        
    elif (inst[pc]=="COS"):
        ac = math.cos(memDatos[int(param[pc])])
        pc = pc + 1
        
    elif (inst[pc]=="TAN"):
        ac = math.tan(memDatos[int(param[pc])])
        pc = pc + 1
        
    elif (inst[pc]=="JZ"):
        if (ac==0):
            pc = int(param[pc])
        else:
            pc = pc + 1  
            
    elif (inst[pc]=="JMP"):
        pc = int(param[pc])
        
    elif (inst[pc]=="INC"):
        valor = memDatos[int(param[pc])]        
        valor = valor + 1
        memDatos[int(param[pc])] = valor        
        pc = pc + 1



