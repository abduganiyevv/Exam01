narx = 100.000
yosh = int(input("yosh?:"))
chegirma1 = 0.5
chegirma2 = 0.2
chegirma3 = 0.3
if yosh >= 0 and yosh <= 6:
    print(f"{narx*chegirma1} so'm (50 % chegirma qo'llanildi)")
elif yosh >= 7 and yosh <= 17:
    print(f"{narx - (narx*chegirma2)} so'm (20 % chegirma qo'llanildi)")
elif yosh >= 60:
    print(f"{narx - (narx*chegirma3)} so'm (30 % chegirma qo'llanildi)")
else:
    print("Chegirma mavjud emas!!!")
