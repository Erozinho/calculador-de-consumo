n,total = int(input("Quantos aparelhos quer testar?\n")),0
for x in range(n):
    CONSUMO,HRS,DIAS = int(input("Consumo do aparelho em wats:\n")),float(input("Horas do aparelho ligado:\n")),int(input("Dias no mes de uso:\n"))
    print("R$ {:.2f} POR MÊS.".format(((CONSUMO * HRS * DIAS) / 1000) * 1.30))
    total = float(total + ((CONSUMO * HRS * DIAS) / 1000) * 1.30)
print("\nR$ {:.2f} NO MÊS.".format(total))