okul = "Meslek Lisesi"
print(okul)
print(okul.upper())
print(okul.upper().lower())
print(okul.upper().lower().title())
print(okul.upper().lower().title().replace("e", "@"))
print(okul.upper().lower().title().replace("e", "@").index("l"))
print(type(okul.upper().lower().title().replace("e", "@").index("l")))
#bir üst satırdaki ifadenin sonuna nokta koyarsak integer metotları görürüz
#fakat bu ifadeyi string e çevirirsek yani str(okul.upper().lower().title().replace("e", "@").index("l")) şeklinde
#yazarsak string ifadeleri görürüz.
print(okul.upper().lower().title().replace("e", "@").index("l")+3)

