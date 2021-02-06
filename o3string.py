# region count
# count - kaç tane geçer

okul = "meslek lisesi"
print(okul)
print(okul.count("e"))
print(okul.count("E"))  # case sensitive. o yuzden E ile e aynı sonuç vermez.
print(okul.count("le"))

print("-" * 30)
# başlangıç ve bitiş aralığı belirterek belli aralıkta arama yapanbiliriz.
# Başlangıç dahil, bitiş dahil olmaz.

print(okul.count("s", 0, 3))  # index numaralarını çok iyi okumalıyız. Sonuç olarak hata verir aksi halde.
# endregion

# region replace
# replace- yer değiştirme
print("-" * 30)
okul = "meslek lisesi"
print(okul)
print(okul.replace("meslek", "anadolu"))
print(okul.replace("meslekkkk", "anadolu"))  # değiştirilecek ifade bulamayınca hata vermez. Aynısını yazar

print("-" * 30)
websitesi = "www.mesleklisesi.k12.tr"
print(websitesi)
print(websitesi.replace("k12.tr", "meb.gov.tr"))

print("-" * 30)
okul = "meslek lisesi"
websitesi = "www.mesleklisesi.k12.tr"
yorum = "bu kelime sansürlenecek"

print(websitesi.replace("k12.tr", "gov.tr"))
print(yorum.replace("sansürlenecek", "***"))
# endregion

# region swapcase
# swapcase- büyük olanlar küçük, küçük olanlar büyük olacak
cümle = "Benim Biricik Yeğenim \"Alparslan\""
print(cümle)
print(cümle.swapcase())
# endregion
