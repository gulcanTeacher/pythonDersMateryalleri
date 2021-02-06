
# region Örnek1
"""
    -Kullanıcıdan yazılı1,yazılı2 girmesi istenir. int kontrolü yapılır.
    -yazılı1 ve yazılı2 ortalaması alınır.
    -Eğer ort>50 ise
        Çıktı geçtiniz ortalamanız={}....
    değilse
        Çıktı kaldınız ortalamanız={}....

"""

yazili1 = input("Lütfen birinci yazılı notu giriniz:\t")
yazili2 = input("Lütfen ikinci yazılı notu giriniz:\t")
if yazili1.isdigit() and yazili2.isdigit():
    yazili1,yazili2=int(yazili1),int(yazili2)
    ortalama=(yazili1+yazili2)/2
    if ortalama>=50:
        print("Geçtiniz ortalamanız: {} ".format(ortalama))
    else:
        print("Kaldınız ortalamanız: {} ".format(ortalama))

else:
    print("Hatalı")
# endregion

# region Örnek2
"""
    -Kullanıcıdan vize, final notu girmesi istenir . int kontrolü yapılır.
    -ortalama vize %40 final %60
    -eğer ortalama<50
        Çıktı bütünlemeye kaldınız. Ortalama ={}
    değilse
        çıktı geçtiniz, ortalamanız={}
"""
vize=input("Vize notu giriniz:\t")
final=input("Final notu giriniz:\t")

if vize.isdigit() and final.isdigit():
    vize,final=int(vize),int(final)
    ort=vize*0.40+final*0.60
    if ort<50:
        print("Bütünlemeye kaldınız.Ortalama={}".format(ort))
    else:
        print("Geçtiniz, ortalamanız={}".format(ort))
else:
        print("Hatalı giriş")
# endregion

