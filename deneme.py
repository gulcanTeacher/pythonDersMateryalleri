def Welcome:
    ad=input("Adınız : \t")
    print("Hoşgeldiniz",ad)
    a=10
    print("Fonksiyondaki a değişkeninin ram deki yeri :"+str(id(a)))


Welcome()
a=15
print("Main deki a değişkeninin ram deki  yeri : "+str(id(a)))

"""
****
****
****

"""
satır, sutun = 0, 0
deger = ""
while satır < 3:
    satır += 1
    while sutun < 4:
        deger += "*"
        sutun += 1
    print(deger)