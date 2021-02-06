"""
    -Ekrana aşağıdaki çıktıyı vereceğiz.
    1.öğrenci
    2.öğrenci
    3.öğrenci
    ....
"""
# # region 1.örnek
# i=1
# while i<=10:
#     print("{}. öğrenci".format(i))#print(i,end=" ")
#     i+=1#i=i+1
#
# """end demek değeri yazdıktan sonra ne olsun ne yazsın demektir. varsayılan altsatıra geçmesi.
#  print tıklayıp +ctrl basarsak bultin sayfasında da bunu görürüz."""
#
# #Döngüyü oluşturma,adım sayısınınetleştirme işin en önemli kısmıdır. Geriye sadecce çıktı üzerinde oynamak kalır.
# # endregion

# region Not:ardışık işlemler
# i+=1
# i-=1
# i*=1
# i/=1
# i%=1#yüzde ala ala git.
# endregion

# # region 2. örnek
# i=input("Lütfen başlangıç değerini giriniz\t")
# # if i.isdigit():
# #     i=int(i)
# #     while i>0:
# #         print(i, end=" ")
# #         i-=1
# # else:
# #     print("Hatalı giriş")
#
# print("-"*15)
#
# if i.isdigit():
#     i=int(i)
#     while i>0:
#         print(i, end=" ")
#         i-=2
# else:
#     print("Hatalı giriş")
# # endregion


i = 50
while i <= 75:
    print(i, end=" ")
    i += 1
print(" ", end="\n")
i=0
while i<100:
    if i%2==1:
       print(i,end=" ")
    i+=1#bunu while içinde yapmış olduk. if içinde yapılmaz.

