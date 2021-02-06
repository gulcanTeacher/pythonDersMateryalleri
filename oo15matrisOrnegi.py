"""
    ekrana 3x4 matrisi için aşağıdaki gibi bir çıktı verilecek
    Çıktı
    * * * *
    * * * *
    * * * *

"""
# i,j=0,0
# deger=""
# while i<3:
#     i+=1
#     while j<4:
#         j += 1
#         deger += "* "
#     print(deger)
#     deger=""
#     j=0

"""
    ekrana 4x3 matrisi için aşağıdaki gibi bir çıktı verilecek
    Çıktı
    * * * 
    * * * 
    * * * 
    * * * 

"""
# i,j=0,0
# deger=""
# while i<4:
#     i+=1
#     while j<3:
#         j += 1
#         deger += "* "
#     print(deger)
#     deger=""
#     j=0

"""
    ekrana 4xi matrisi için aşağıdaki gibi bir çıktı verilecek
    Çıktı
    * * * 
    * * * 
    * * * 
    * * * 

"""
i,j=0,0
deger=""
while i<4:
    i+=1
    while j<i:
        j += 1
        deger += "* "
    print(deger)
    deger=""
    j=0