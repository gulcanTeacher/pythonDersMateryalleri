
"""
    Kullanıcıdan sayı girmesi istenir
    Karesi - karekökü- küpü hesaplanır, ekrana doğru formatta çıktısı verilir.
    Çıktı
    ..... sayısının;
    karesi .....
    karekökü .....
    küpü .....
"""

sayi=int(input("Lütfen sayı giriniz : "))
print("""
    {} sayısının ;
    karesi {}
    karekoku {}
    küpü {}
""".format(sayi,sayi**2,round(sayi**(1/2),3),sayi**3)
      )
