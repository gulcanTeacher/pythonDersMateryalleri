"""
    -Döngü içinde kullanıcıdan 3 adet sayı girmesi istenir.
    -Ekrana doğru formatta çıktı verilerek, sayıların ortalaması yazılır.
        Çıktı
        Girilen ... adet sayının ortalaması...

"""

i=1
toplam=0
while i<=3:
    s=input("lütfen {}. sayıyı giriniz:\t".format(i))
    if s.isdigit():
        s=int(s)
        i += 1
        toplam += s
    else:
        continue#sayısal değer girmediysen tekrar döngü devam eder. sayı girmeni ister devamında.
# Ama biz sayısal değer girmediyse çıkmasını istiyoruz.
# continue döngünün başına gelmeyi sağlar. Böylece sayısal değer yoksa çıkar. Yani altsatırları dikkate alma döngü başına git demek.
        print("Lütfen sayısal değer giriniz")
print("Girilen {} adet sayının ortalaması: {}".format(i-1,round(toplam/(i-1),3)))