# kullanıcıya değişken değeri girdireceğimiz zaman kullanıcı boşluk bırakabilir.
# Boşluk da string olarak basar. hafızada da yer kaplar. Bunu kontrol et.strip ile
print("*" * 30)
print("strip -başındaki ve sonundaki boşlukları alır.")
print("*" * 30)
# region strip
okul = "            Meslek lisesi           "
print(okul)
print(okul.strip())
# parantez içi değişken almazsa başında ve sonunda boşlukları siler.
# Bir değişken girersek o değişkenleri siler başındanve sonundan

school1 = "........           Meslek lisesi ....."
print(school1.strip("."))

school2 = "   ........           Meslek lisesi .....   "
print(school2.strip("."))

# Neden kullanıyoruz biz bu strip metodunu?Örnek verin.
# Kullanıcıdan alınan veriyi database e atamazsın doğrudan. Manipule edilmiş veri olur bu.
# Kendi kontrolümde bir veri olması gerek. Bu yüzden kullanıyorum.
# Veritabanına göndermeden önce kontrol edip düzenliyorum.
# endregion

print("*" * 30)
print("rstrip/lstrip -sağındaki /solundaki boşlukları alır.")
print("*" * 30)
# region rstrip ve lstrip
# highschool = ".......meslek lisesi......."
# print(highschool.rstrip("."))
# print(highschool.lstrip("."))
# endregion

print("*" * 30)
print("isdigit- rakam mı")
print("*" * 30)
# region isdigit
# deger = "1"
# print(deger.isdigit())
# value = "_1258"
# print(value.isdigit())
# endregion

print("*" * 30)
print("isalpha -harf mi")
print("*" * 30)
# region isalpha
# deger = "1"
# print(deger.isalpha())
# value = "gülcan"
# print(value.isalpha())
# endregion

print("*" * 30)
print("alfanumarik mi yani harf ve rakamlardan oluşacak yani a-z arası ve 0-9 arası olacak.")
print("*" * 30)
# region isalphanum
# isalpha- harf mi
# deger = "1."
# print(deger.isalnum())
# value = "gülcan"
# print(value.isalnum())
# endregion

print("*" * 30)
print("#isupper/islower- tamamı büyük/küçük mü?")
# region isupper/islower
# print("*" * 30)
# deger="MESLEK LİSESİ"
# print(deger.isupper())
# deger="mESLEK LİSESİ"
# print(deger.isupper())
# print("-"*15)
# deger="MESLEK LİSESİ"
# print(deger.islower())
# deger="meslek lisesi"
# print(deger.islower())
# endregion

print("*" * 30)
print("isspace - tamamı boşluk mu diye bakar.")
print("*" * 30)
# region isspace
# deger=" "
# print(deger.isspace())
# deger=" ."
# print(deger.isspace())
# endregion

print("*" * 30)
print("istitle - ilk harf büyükmü diye bakar. title metodu zaten ilk harfi büyük yapıyordu ya hatırla.")
print("*" * 30)
# region istitle
# deger="Gülcan Parlamış"
# print(deger.istitle())
# deger="gülcan Parlamış"
# print(deger.istitle())
# endregion

print("*" * 30)
print("isidentifier - Belirtilen değer deişken ismi olur mu olmaz mı.")
print("*" * 30)
# region isidentifier
deger = "meslek Lisesi"
print(deger.isidentifier())
deger = "meslekLisesi"
print(deger.isidentifier())
deger = "1meslekLisesi"
print(deger.isidentifier())
deger = "_1meslekLisesi"
print(deger.isidentifier())
# endregion

print("*" * 30)
print("split - string bölme.")
print("*" * 30)
# region split
gorev = "Fatih Projesi Koordinatörü"
print(gorev.split())
print(len(gorev.split()))  # kelime sayar.
print("-" * 15)
gorev = "Gülcan Parlamış. Fatih Projesi Koordinatörü"
print(gorev.split("."))  # cümle sayar.
# endregion

print("*" * 30)
print("index-Aradığın değer yani index() içine yazdığın değer neyse onu ilk bulduğu yerin index değerini verir.")
print("*" * 30)
# region index
deger = "Meslek Lisesi"
print(deger.index("e"))
# aradığın değeri bulamazsa ValueError: substring not found hatası verir.
# belli bir aralıkta aratmak için index("e",8,15) gibi birformat kullanırız.
print(deger.index("e", 8, 13))
# endregion

print("*" * 30)
print("format-Aradığın değer yani index() içine yazdığın değer neyse onu ilk bulduğu yerin index değerini verir.")
print("*" * 30)
# format işlemiyle yapacağımız şeyleri concat(+) ve % işaretleriyle de yapabiliriz.
dil = "Python"
versiyon = "3.7.4"
print("Bu yazılım " + dil + " dilinde "+ versiyon+" versiyonu ile yazılmıştır.")#concat ile formatlama
print("-" * 15)
print("Bu yazılım %s dilinde %s versiyonu ile yazılmıştır." % (dil,versiyon))# % ile formatlama
print("-" * 15)
print("Bu yazılım {} dilinde {} versiyonu ile yazılmıştır." .format (dil,versiyon))# % ile formatlama
# % ile formatlama işleminde nokta koyduktan sonra string metotlarını da kullanabiliriz.
print("Bu yazılım {} dilinde {} versiyonu ile yazılmıştır." .format (dil,versiyon).upper())
print("***************2. örnek***************")
dil="Python"
us="Paytaan"
uk="Paytın"
print(dil+ " dili amerikan aksanı ile " + us + " şeklinde, ingiliz aksanı ile "+ uk +" şeklinde telaffuz edilir.")
print("%s dili amerikan aksanı ile %s şeklinde, ingiliz aksanı ile %s şeklinde telaffuz edilir." % (dil,us,uk))
print("{} dili amerikan aksanı ile {} şeklinde, ingiliz aksanı ile {} şeklinde telaffuz edilir." .format (dil,us,uk).upper())

