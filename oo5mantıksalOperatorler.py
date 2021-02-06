# # region 1. örnek
# a = int(input("a değeri giriniz...\t"))
# if 0<a<100:#a > 0 and a < 100:
#     print("{} sayısı 100 den küçük ve pozitiftir.".format(a))
# # endregion
#
# # region 2. örnek
# yas=int(input("Lütfen yaşınızı giriniz: "))
# if yas>6 or yas<4:
#     print("Kurs 1 için uygun değilsiniz.")
# else:
#     print("Kursa Hoşgeldiniz...")
# # endregion

a = input("Lütfen birinci sayıyı giriniz: ")
b = input("Lütfen ikinci sayıyı giriniz: ")
# değer olarak string bir değer de girebilir kullanıcı örneğin glcan yazar, 2 yerine iki yazar. o yuzden isdigit kullanacağız.
if a.isdigit() and b.isdigit():
    a, b = int(a), int(b)
    if a > b:
       print("{} sayısı {} sayısından büyüktür.".format(a,b))
       # print(a + "sayısı " + b + " sayısından büyüktür.") bu şekilde hata verdi. biz de string concat işlemi yaptık.
    else:
        print("{} sayısı {} sayısına eşit ya da küçüktür.".format(a, b))
        #print(a + "sayısı" + b + "sayısına eşit ya da büyüktür.")
else:
    print("Hatalı giriş...")
#input kısmında int yazıp input yazıyorduk neden yazdığımızı görmüş olduk.
#burda int yazmazsak isdigit ve a, b = int(a), int(b) şeklinde komut kullanarak da
# ne yapacağımızı görmüş olduk.