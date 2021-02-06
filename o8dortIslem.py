"""
    Kullanıcıdan s1 ve s2 sayıları alınır
    Dört işlem yaparak, ekrana doğru formatta çıktısı verilir.
    Çıktı
    .... ile .... sayılarının ..... işlemi sonucu : ....
"""

islem="toplama"

s1=input("Lütfen birinci sayıyı giriniz... : ")
s2=input("Lütfen ikinci sayıyı giriniz... : ")

sonuc=s1+s2
print(" {} sayısı ile {} sayısının {} işlemi sonucu : {} olur.".format(s1,s2,islem,(int(s1)+int(s2))))
# region 2. yol
#2. yol
# islem="toplama"
#
# s1=int(input("Lütfen birinci sayıyı giriniz... : "))
# s2=int(input("Lütfen ikinci sayıyı giriniz... : "))
#
# sonuc=s1+s2
# print(" {} sayısı ile {} sayısının {} işlemi sonucu : {} olur.".format(s1,s2,islem,sonuc))
# endregion



s1=int(input("Lütfen birinci sayıyı giriniz... : "))
s2=int(input("Lütfen ikinci sayıyı giriniz... : "))
islem="çıkarma"

sonuc=s1-s2
print(" {} sayısı ile {} sayısının {} işlemi sonucu : {} olur.".format(s1,s2,islem,sonuc))


islem="çarpma"

sonuc=s1*s2
print(" {} sayısı ile {} sayısının {} işlemi sonucu : {} olur.".format(s1,s2,islem,sonuc))


islem="bölme"

sonuc=s1/s2
print(" {} sayısı ile {} sayısının {} işlemi sonucu : {} olur.".format(s1,s2,islem,sonuc))

