# startswith ve endswith metodlarının ikisi de geriye true ya da false olarak değer döndürür.

# region startswith
# startswith- belirttiğimiz değerle başlıyorsa true döndürür. yoksa false değeri döndürür.

# örneğin web sitesi kontrolü yapabilirim. www ile mi başlıyor bakarım bunun için
web = "www.gulcanparlamis.com"
print(web.startswith("www"))
print(web.startswith("wwww"))
# endregion

# endswith- belirttiğimiz değerle bitiyorsa true döndürür. yoksa false değeri döndürür.
print("-"*30)
web = "www.gulcanparlamis.com"
print(web.endswith("com"))
