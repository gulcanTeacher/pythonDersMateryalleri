"""
    -Döngü içinde kullanıcıdan x adet sayı girmesi istenir.
    -0 girene kadar sayı istemeye devam edecek.
    -Ekrana doğru formatta sayı girilerek çıktı vermesi istenir.
        Çıktı
        Girilen ... adet sayının toplamı ...

"""

# önce sonsuz döngü oluştururuz. Yani while True:
toplam, adet=0,0
while True:
    s=int(input("Lütfen sayı giriniz:\t"))
    adet+=1
    if s==0:
        break
    else:
        toplam+=s
#print("Girilen sayıların toplamı {}".format(toplam))
print("Girilen {} adet sayının toplamı toplamı {}".format(adet,toplam))

