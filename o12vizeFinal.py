"""
    Kullanıcıdan vize final notları alınır
    not=vize*0.40+final*0.60
    Çıktı
    Dönem sonu notunuz : ....
"""

vize=int(input("Vize notunuzu giriniz:\t"))
final=int(input("Final notunuzu giriniz:\t"))
notu=vize*0.40+final*0.60
print(type(notu))#0.40 ve 0.60 sayılarıyla çarptık. vize ve final int de olsa float sonuç olur
print(" Dönem sonu notunuz : {} ".format(notu))
