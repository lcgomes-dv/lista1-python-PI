temp_caldera = int(input("Digite a temperatura: "))
if(temp_caldera < 100):
    print("Temperatura Baixa")
elif(100 <= temp_caldera <=150):
    print("Temperatura Normal")
else:
    print("ALERTA: Temperatura Alta!!!")