import random

user_num = int(input("Diga'm un número i tractaré de endevinar-lo: "))
i = 0
cpu_resp = 0
min_num = 0
max_num = 100

while True:
    cpu_num = random.randint(min_num, max_num)
    i += 1
    if cpu_num < user_num:
        print("El número que has pensat és el", cpu_num, "?")
        cpu_resp = input("Escriu 'a' si el teu número és més alt i 'b' si el teu número és més baix (a/b): ")
        if cpu_resp == 'a':
            min_num = cpu_num + 1
    
    elif cpu_num > user_num:
        print("El número que has pensat és el", cpu_num, "?")
        cpu_resp = input("Escriu 'a' si el teu número és més alt i 'b' si el teu número és més baix (a/b): ")
        if cpu_resp == 'b':
            max_num = cpu_num - 1
    
    else:
        print("He endevinat el número en", i, "intents! És", cpu_num)
        break
        