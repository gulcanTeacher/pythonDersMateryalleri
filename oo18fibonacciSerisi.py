"""
    -Ekrana 10 adet fibanocci serisini yazdıran program
        Çıktı
        1 1 2 3 5 8 13 21 34 55 89
          | | |
          a+b=c
            | |
            a b

yani a+b =c olmuş. sonra a=b ve b=c olmuş. a nın yerine b gelmiş, cnin yerine b gelmiş.yer değiştirme algoritması var.
"""

i=1
a,b=0,1
print(b,end=" ")
while i<=10:
    i+=1
    c=a+b
    print(c,end=" ")
    a=b
    b=c
