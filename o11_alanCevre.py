# region alan/çevre soru 1
"""
    pi adında bir değişken tanımlayın. 3.1496546 veya 22/7
    kullanıcıdan yarıçapve yükseklik değişkenleri alınır.
    alan=yarıçap*yükseklik*pi
    Çıktı
    Yarıçapı ....... , yüksekliği ........ olan koninin alanı : ......

"""

pi = 22 / 7
yaricap = float(input("Lütfen yarıçap giriniz : "))
yukseklik = float(input("Lütfen yükseklik giriniz: "))
alan = yaricap * yukseklik * pi
print("Yariçapı {}, yüksekliği {} olan koninin alanı : {}  ".format(yaricap, yukseklik, round(alan, 3)))
# endregion

# region alan/çevre soru 2
"""
    Kullanıcıdan iki tane kenar(taban,yükseklik) değeri alınır.
    alan=tabanxyukseklik /2
    Çıktı
    Tabanı.... , yüksekliği .....olan üçgenin alanı : ....... birimdir.
"""
taban = int(input("Lütfen taban değeri giriniz : "))
yukseklik = int(input("Lütfen yukseklik değeri giriniz : "))
alan = int(taban * yukseklik / 2)  # int yaptım ki sonuç tam sayı olarak dönsün.
print("Tabanı {}, yüksekliği {} olan üçgenin alanı : {} birimdir.".format(taban, yukseklik, alan))
# endregion
