"""
    -Ekrana 1x10 matrisi için aşağıdaki gibi bir çıktı verilecek
        Çıktı
        **********
"""

i=0
deger="*"
while i<10:
    i+=1
    deger+="*"#concat gibi düşün sonuna ekliyor.
print(deger)

"""
    1!+2!+3!+....
    1^2+2^2+3^3....
    (1/1!)+(1/2!)+(1/3!).... gibi işlemlerde içiçe while kullanılır.

"""
#breakpoint ekleyip aşağıdakileri çalıştır j=0 satırına kadar.
# i,j=0,0
# while i<3:
#     i+=1
#     while j<3:
#         j+=1
#     j=0#çok hayati bir dokunuş. j=3olduktan sonra tekrar sıfırlanıp devam etsin diye yapılır bu.
#aşağıdakilerin çalışmasını debug yapark yani breakpointle rahatça görebilirsin.
i,j=0,0
deger=""
while i<5:
    i+=1
    while j<5:
        j += 1
        deger += "*"
    print(deger)
    deger=""#değeri sıfırlamazsan ne olur bak.
    j=0
