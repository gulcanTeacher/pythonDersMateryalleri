"""
    Kullanıcıdan denklemin katsayı,sabit değer bilgileri alınır.
    kok=-b/a
     Çıktı
     1.dereceden katsayı {} ve sabit değer {} olan denklemin kökü : .....
"""
a=int(input("Birinci 1. derece katsayısı?:\t"))
b=int(input("Birinci 1. sabit değeri?:\t"))
kok=-b/a
print("1.dereceden katsayı {} ve sabit değer {} olan denklemin kökü {} :".format(a,b,kok))