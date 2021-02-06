# region Örnek1
havaYagisliMi = "yağmurlu"
havaSogukMu = "soğuk"
if havaYagisliMi == "yağmurlu":  # burası yanlışsa if içine hiç girmez. değiştir ve gör.
    if havaSogukMu == "soğuk":  # değiştir sonucu gör.Ama yukarıdaki if içine girsin.
        print("Şemsiyeni al, gocuk giy")
    else:
        print("Şemsiyeni al,tşört giy")
# endregion

# region 2. örnek
# a=int(input("a değeri giriniz..."))
# if a>0:
#     if a<100:
#         print("{} sayısı 100 den küçük ve pozitiftir.".format(a))
#     else :
#         print("{} sayısı 100 den büyük ve pozitiftir.".format(a))
#  endregion

sıcaklık1 = int(input("sıcaklık 1......:"))
sıcaklık2 = int(input("sıcaklık 2......:"))

if sıcaklık2 > sıcaklık1:
    if sıcaklık2 == 39:
        print("ateş artıyor,kritik vücut sıcaklığı {}".format(sıcaklık2))
    elif sıcaklık2 == 37:
        print("ateş artıyor, vücut sıcaklığı {}".format(sıcaklık2))
    else:
        print("Vücut sıcaklığı normal".format(sıcaklık2))
else:
    print("Ateşi düşüyor.")
