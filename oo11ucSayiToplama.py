"""
    -Döngü içindekullanıcıdan 3 adet sayı girmesi istenir.
    -Ekrana doğru formatta çıktı verilerek, sayıların toplamları yazılır.
        Çıktı
        Girilen ... adet sayının toplamı...

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
        print("Lütfen sayısal değer giriniz")
        continue#sayısal değer girmediysen tekrar döngü devam eder. sayı girmeni ister devamında.
# Ama biz sayısal değer girmediyse çıkmasını istiyoruz.
# continue döngünün başına gelmeyi sağlar. Böylece sayısal değer yoksa çıkar. Yani altsatırları dikkate alma döngü başına git demek.

print("Girilen {} adet sayının toplamı: {}".format(i-1,toplam))