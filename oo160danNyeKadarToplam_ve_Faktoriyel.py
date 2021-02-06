"""
    -Kullanıcıdan bir N değeri girmesi istenir, int kontrolü yapılır.
    -ekrana doğru formatta çıktı verilerek 0-N arası sayıların toplamı yazılır.
        Çıktı
        Lütfen bir değer giriniz... :5
        0 dan 5 sayısına kadar olan sayıların toplamı: 15

"""

i,n,toplam=0,0,0
n=input("Lütfen bir sayı giriniz:\t")
if n.isdigit():
    n=int(n)
    while i<=n:
        toplam += i
        i+=1

    print("0 dan {} sayısına kadar olan sayıların toplamı: {}".format(n,toplam))
else:
    print("Hatalı giriş")

"""
    -Kullanıcının girdiği sayının faktöriyelini bulunuz.
        Çıktı
        5 -> 5! = 120
"""
i=1
sonuc=1
sayi=input("Lütfen sayı giriniz:\t")
if sayi.isdigit():
    sayi=int(sayi)
    while i<=sayi:
        sonuc*=i
        i += 1
    print("{} -> {}! = {}".format(sayi,sayi,sonuc))
