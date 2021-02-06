"""
    Kullanıcıdan doğum tarihi girmesi istenir.
    Yaş hesaplaması yapılarak ekrana doğru formatta çıktısı verilir.
    Çıktı
    Yaşınız : .....

"""

dTarihi = int(input("Lütfen doğum tahinizi giriniz: "))
bulundugumuzYil = int(input("Lütfen bulunduğumuz yılı giriniz : "))
yas = bulundugumuzYil - dTarihi
print("Yaşınız : {}".format(yas))

import datetime  # python daki bir modül. Daha sonra modüller kısmında göreceğiz bunu.

print("*" * 15 + "2.yol" + "*" * 15)
yas = datetime.datetime.now().year - dTarihi  # datetime.datetime.now().year  bulunduğumuz yıl demek
print("Yaşınız : {}".format(yas))
