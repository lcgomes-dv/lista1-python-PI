n1 = float(input("Digite a sua primeira nota: "))
n2 = float(input("Digite a sua segunda nota: "))
media = (n1 + n2) / 2
if(media <= 7):
    print(f"Parabés, você foi aprovado!\nSua Média: {media}")
elif(5 <= media <= 6.9):
    print(f"Você ficou de recuperação, se esforce, você tem chances!\nSua Média: {media}")
else:
    print(f"Infelizmente você reprovou, dedique-se mais próximo ano!\nSua Média: {media}")