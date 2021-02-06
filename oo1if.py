# region if giriş
havaDurumu="yağmurlu"
if havaDurumu=="yağmurlu" :
    print("Şemsiye al")
# endregion

# region if örnek1
a=int(input("Lütfen sayı giriniz : "))
#if çalışması sonucunu görmek için prınt("buradayım") yazdık.
print("buradayız")
if a<0:
    print("{} sayısı negatiftir.".format(a))
print("buradayız")
# endregion

# region if örnek2
kullaniciAdi=input("Lütfen kullanıcı adınızı giriniz : ")
if kullaniciAdi =="admin":
    print("Merhaba sevgili yönetici")
# endregion

# region if örnek3
ehliyetVarMi=True
if ehliyetVarMi==True : #if ehliyetVarMi: aynı şey
    print("Tamam. Devam edebilirsiniz.")
# endregion

s1=15
s2=25
dil="Python"
if s1>=s2 : pass #s1,s2 den büyük eşitse bu koşula gir
if s1<=s2 : pass #s1,s2 den küçük eşitse bu koşula gir
if s1==s2 : pass #s1,s2 ye eşitse bu koşula gir
if s1 is s2 : pass #s1,s2 ye eşitse bu koşula gir
if s1!=s2 : pass #s1,s2 ye eşit değilse bu koşula gir
if s1 is not s2 : pass #s1,s2 ye eşit değilse bu koşula gir
if s1**2 >s2 *8 : pass
if dil="english": pass
if "yth" in dil: pass#string ifadenin içinde bu varsa true
#yukarıdaki komutların her biri sonuç vermez. koşullar doğruysa geç diye komutlar yazdık. sadece denedik.

