

# region ilk program
print("Gülcan Parlamış")
print("Bilişim Teknolojileri")
okul = "Meslek Lisesi"

print(type("Gülcan Hoca"))
# endregion


# region formatlama
print("Gülcan\n Parlamış")
print("Gülcan\t\t Parlamış")
print("""
    Tab
Alt
Uçan Kuşlar martılaaar....:)))
""")
# endregion

# region değer atama
x1 = 5
x2 = 50
x3 = "Gülcan"

x1, x2, x3, ehliyetVarMi = 20, 30, "Gülcan", True
print(ehliyetVarMi)

print(3.14, True, "ali", 1064, sep="-")
# endregion

# region tip dönüşümü ve formatlama
pi = 3.14
print(pi)
print("Pi Değeri : " + str(pi))

print("{} Pi Değerinin 2 katı = {}".format(pi, (pi * 2)))
# endregion