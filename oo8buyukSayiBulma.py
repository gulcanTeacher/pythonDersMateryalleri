"""
    -Kullanıcıdan alınan sayının hangisi büyükse ekrana yazan program
    -ekrana yazdırılacak format:
    ..... sayısı ..... sayısından büyüktür. ...... fazladır.
"""

# region iki sayıyı karşılaştırma
# sayi1=int(input("Lütfen 1. sayıyı giriniz:\t"))
# sayi2=int(input("Lütfen 2. sayıyı giriniz:\t"))
#
# if sayi1>sayi2:
#     print("{} sayısı {} sayısından büyüktür. {} fazladır.".format(sayi1,sayi2,sayi1-sayi2))
# elif sayi2>sayi1:
#     print("{} sayısı {} sayısından büyüktür. {} fazladır.".format(sayi2,sayi1,sayi2-sayi1))
# else:
#     print("{} sayısı {} sayısına eşittir." .format(sayi1,sayi2))
# endregion

# region 3 sayıyı karşılaştırma
# sayi1 = input("Lütfen 1. sayıyı giriniz:\t")
# sayi2 = input("Lütfen 2. sayıyı giriniz:\t")
# sayi3 = input("Lütfen 3. sayıyı giriniz:\t")
# if sayi1.isdigit() and sayi2.isdigit() and sayi3.isdigit():  # yukarıda sayı girişlerinde int yazıp input yapmıştık.
#     # int leri silip burada isdigit kullandık. sonra da int lerle eşitleme yaptık.Program mükemmel hale geldi.
#     sayi1, sayi2, sayi3 = int(sayi1), int(sayi2), int(sayi3)
#     if sayi1 > sayi2 and sayi1 > sayi3:
#         print("{} sayısı {} sayısından ve {} sayısından büyüktür.".format(sayi1, sayi2, sayi3))
#     elif sayi2 > sayi1 and sayi2 > sayi3:
#         print("{} sayısı {} sayısından ve {} sayısından büyüktür.".format(sayi2, sayi1, sayi3))
#     else:
#         print("{} sayısı {} sayısından ve {} sayısından büyüktür.".format(sayi3, sayi2, sayi1))
#
# else:
#     print("Hatalı giriş...")
# endregion

# karşılaştırılacak sayı arttıkça problem karmaşık hale gelir. Bir kolay yol bulmamız lazım.
# Kaç sayı olursa olsun en büyüğü bulmalıyız.
# Bunun için en büyük sayıyı en başta 0(sıfır) eşitleyerek işe başlarız. bu algoritmamızın %99 unu oluşturur.
# burada yer değiştirme algoritması kullanacağız. Sayı büyükse enbüyük sayı sensin diyecek.
sayi1 = input("Lütfen 1. sayıyı giriniz:\t")
sayi2 = input("Lütfen 2. sayıyı giriniz:\t")
sayi3 = input("Lütfen 3. sayıyı giriniz:\t")
sayi4 = input("Lütfen 4. sayıyı giriniz:\t")
enb = 0
if sayi1.isdigit() and sayi2.isdigit() and sayi3.isdigit() and sayi4.isdigit():  # yukarıda sayı girişlerinde int yazıp input yapmıştık.
    sayi1, sayi2, sayi3, sayi4 = int(sayi1), int(sayi2), int(sayi3),int(sayi4)
    if sayi1 > enb:
        enb = sayi1
    if sayi2 > enb:
        enb = sayi2
    if sayi3 > enb:
        enb = sayi3
    if sayi4 > enb:
        enb = sayi4
    print("{} , {}, {},{} sayılarından en büyük olanı:  {}".format(sayi1, sayi2, sayi3,sayi4, enb))
else:
    print("Hatalı giriş...")
