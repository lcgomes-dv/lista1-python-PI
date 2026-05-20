numero = int(input("Digite um número qualquer e descubra se é impar ou par: "))
par = numero % 2 == 0
if(par):
    print(f"O número {numero} é Par")
else:
    print(f"O número {numero} é Ímpar")