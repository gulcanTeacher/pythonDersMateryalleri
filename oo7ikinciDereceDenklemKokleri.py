'''
    -ax2+bx+c=0
    -Kullanıcıdan a,b,c değerleri alınır.Bu değerler uygunsa;
        -delta=b2+4ac
        -delta>0. iki kök: (-b+kök(delta))/2a,(-b-kök(delta))/2a
        -delta=0 iki kök. k1=k2=-b/2a
        -delta<0 kök yoktur.

'''

a = input("A: ")
b = input("B: ")
c = input("C: ")

if a.isdigit() and b.isdigit() and c.isdigit():
    a, b, c = int(a), int(b), int(c)
    delta = b ** 2 - 4 * a * c
    if delta > 0:
        k1 = (-b - delta ** 0.5) / (2 * a)
        k2 = (-b + delta ** 0.5) / (2 * a)
        print(round(k1, 3), round(k2, 3))  # örn 2,5,2 delta>0 kökler:-2 ve 0.5 örn 1,5,1 kökler:-4.71 ve -0.209
    elif delta == 0:
        k1 = k2 = -b / (2 * a)  # örn 1,2,1 delta=0 kökler:-1 ve -1 eşit yani.
        print(k1, k2)
    else:
        print("Kök yoktur.")  # 5,1,5 delta<0 kökler:kök yoktur.
else:
    print("Hatalı giriş")
