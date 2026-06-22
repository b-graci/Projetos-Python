#Escreva um código que imprima todos os números exceto o número 13.
for n in range(1,16):
    if n != 13:
     print(n,"º andar","recebe o número",n)
    else:
      print("OBS: O dono não quer andar com número 13 porque atrai azar")


#Escreva mais dois códigos que resolvam o mesmo problema, mas dessa vez usando os outros dois tipos de laços de repetição aprendidos.

n = 1

while n <=20:

    if n == 13:
        print("OBS: O dono não quer andar com número 13 porque atrai azar")
        n += 1
        continue

    print(f"{n}º andar recebe o número {n}")
    n += 1

#Como desafio, imprima eles em ordem decrescente (20, 19, 18...)
for n in range(20, 0, -1):

    if n == 13:
        print("OBS: o 13 foi ignorado")
        continue

    print(f"{n}º andar recebe o número {n}")
