adSoyad = input("Lütfen ad soyad giriniz : \t")
print(adSoyad.capitalize())
print(type(adSoyad))  # hangi tip değişken girersek girelim bunu string olarak algılar.
#bu yüzden input tan önce int kullanarak integer a çevirme işlemi yaptık.

sayi = int(input("Lütfen sayı giriniz : \t"))
print(type(sayi))
print(sayi)
print(sayi + 5)
print("{} sayısının 5 fazlası:  {} olur".format(sayi, (sayi + 5)))

s1 = int(input("Lütfen birinci sayıyı giriniz : "))
s2 = int(input("Lütfen ikinci sayıyı giriniz : "))
ort=(s1+s2)/2
print("{} ile {} sayısının ortalaması : {}" .format(s1,s2,ort))
