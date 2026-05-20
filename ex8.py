peso = float(input("Digite o seu peso(em Kg): "))
altura = float(input("Digite a sua altura (em metros): "))
imc = peso/altura**2
if(imc < 18.5):
    print(f"O resultado do seu IMC: {imc}\n Você está abaixo do peso para sua altura")
elif(18.5 <= imc <= 24.9):
    print(f"O resultado do seu IMC: {imc}\n Você está com o peso normal para sua altura")
if(imc > 25):
    print(f"O resultado do seu IMC: {imc}\n Você está sobrepeso para sua altura")