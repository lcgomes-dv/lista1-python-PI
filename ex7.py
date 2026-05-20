salario_atual = float(input("Qual o seu salário atual? "))
tempo_empresa = int(input("Qual o seu tempo de empresa? "))
if(tempo_empresa < 2):
    salario_novo = salario_atual * 0.5 + salario_atual
    print(f"Você merece um aumento de 5% pelo seu tempo de colaboração \n Antigo Salário: {salario_atual}\n Novo Salário: {salario_novo}")
elif(2 <= tempo_empresa <= 5):
    salario_novo = salario_atual * 0.10 + salario_atual
    print(f"Você merece um aumento de 10% pelo seu tempo de colaboração \n Antigo Salário: {salario_atual}\n Novo Salário: {salario_novo}")
else:
    salario_novo = salario_atual * 0.15 + salario_atual
    print(f"Você merece um aumento de 15% pelo seu tempo de colaboração \n Antigo Salário: {salario_atual}\n Novo Salário: {salario_novo}")