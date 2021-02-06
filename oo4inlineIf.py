# if kullanımında birçok elif  bir tane else olabiliyordu.Şimdi de tek satırda if then else yapısını göreceğiz.

# sıfırdan büyük rakamları metne çeviren program yapacağız.

sayi = int(input("sayı: "))
metin = ""
# if sayi==0:
#     metin="Sayı sıfır"
# elif sayi==1:
#     metin="bir"
# elif sayi==2:
#     metin="iki"
# else:
#     metin="Hatalı giriş"
# metin = "Sayı sıfır" if sayi == 0 else  "Hatalı giriş"#koşul sağa yazılır, atamalar sola yazılır.
metin = "Sayı sıfır" if sayi == 0 else "Sayı bir" if sayi == 1 else "Sayı iki" if sayi == 2 else "Hatalı giriş"
#elif yerine kullanılan if ler için atama işlemlerinde metin yazmadık tekrar dikkat edersen.
print(metin)
# koşullar else ile bağlanacak if ile devam edecek.else if else if devam ediyor.
