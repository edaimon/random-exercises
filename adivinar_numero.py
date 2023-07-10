# crear un programa que crees un numero random i et preguntes per adivinar,
# i et digués si és menor o major # reiteradament fins que tu l'encertis
import random

num_adivinar  = random.randint(0, 100)
print(num_adivinar)
i = 0
while True:
    num_intento = int(input("Diga'm un numeret de 0 a 100 a vore si l'endevines: "))
    if num_intento < 0 or num_intento > 100:
        print("El número ha de ser de l'0 al 100")
        print("=" * 50)
    elif num_intento < num_adivinar:
        print("El número a endevinar és més gran")
        print("=" * 50)
        i += 1 
    elif num_intento > num_adivinar:
        print("El número a endevinar és més petit")
        i += 1
    elif num_intento == num_adivinar:
        print(f"Asertaste en {i} intentossss")
        break
    else:
        print("Error desconegut")
        break

