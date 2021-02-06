# # region ilk örnek
# havaDurumu = "güneşli"
# if havaDurumu == "yağmurlu":
#     print("Şemsiyeni al.")
# else:
#     print("şemsiye almaya gerek yok.")
# # endregion
#
# # region ikinci örnek
# engeleDegdiMi = False
# can, skor = 3, 0
# if engeleDegdiMi:
#     can -= 1
#     print("{} canınız kaldı".format(can))
# else:
#     skor += 1
#     print("{} anlık skorunuz".format(skor))
# # endregion
#
# # region üçüncü örnek
# sayi=int(input("Lütfen sayı giriniz : "))
# if sayi>0:
#     print("pozitif")
# else:
#     print("negatif")
# # endregion

# # region 4. örnek
# havaDurumu = "sıcak" #değer olarak sıcak yaz ve başka bir değer yaz.
# if havaDurumu == "yağmurlu":
#     print("şemsiyeni al")
# elif havaDurumu == "sıcak":
#     print("tşört giy")
# else:
#     print("kazak giy")
# # endregion

sayi=int(input("Lütfen sayı giriniz :\t"))
# if sayi>0: # if içi dolu olmak zorunda. boş geçmek istiyorsan pass yazmalısın içine.
#     print("Pozitif")
# elif sayi==0:
#     print("Sıfırdır.")
# else:
#     print("negatiftir.")

if sayi==5:
    pass
elif sayi>5:
    print("Sayı 5 ten büyük")
elif sayi<-5:
    print("Sayı -5 ten küçük")
elif sayi>0:
    print("Sayı pozitiftir.")
else:
    print("Hiçbir koşul sağlanmadı")
#Birden fazla elif kullanılabilir.
#Tüm koşullar unutulmadan yazılmalıdır. Hem de sıralama mantıklı olmalıdır.
