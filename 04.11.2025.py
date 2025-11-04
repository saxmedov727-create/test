# ishora = True
# son = []
# while ishora:
#     kirit = input("Butun sonni kiriting: ")
#     print("Dasturni tugatish uchun 0 ni kiriting")
#     a = float(kirit)
#     if a%2 == 0:
#         son.append(a)
#     else:
#         continue
#     if a == 0:
#         b = sum(son)
#         print(b)
#         ishora = False




# mevalar = { "gilos" : 23000,
#     "anor" : 35000,
#     "banan" : 38000
# }
# print(f"bizda quydagi mahsulotlar bor: {mevalar}")
# b = 0
# while True:
#     a = input("Mevani tanlang: Tugatish uchun 'exit' ni kiriting: ")
#     if a == "exit":
#         print (f"Jami summa: {b}")
#         break
#     elif a in mevalar:
#         c = int(input("Ushbu mahsulotdan nechta kerak: "))
#         u = mevalar[a]*c
#         b += u
#     else:
#         print("Bunday meva mavjud emas")




# ishora = True
# c = 0
# while ishora:
#     a = (input("sonni kiriting: tugatasizmi: (ha/yoq): "))
#     if a == "ha":
#         break
#     else:
#         b = int(a)
#     if b%5 == 0:
#         continue
#     else:
#         c = b**2
#         print(c)



# oylar = {
#     1: "yanvar",
#     2: "fevral",
#     3: "mart",
#     4: "aprel",
#     5: "may",
#     6: "iyun",
#     7: "iyul",
#     8: "avgust",
#     9: "sentabr",
#     10: "oktabr",
#     11: "noyabr",
#     12: "dekabr"
# }
# ishora = True
# while ishora:
#     a = (input("Oy raqamini kiriting: Tugatish uchun exit: "))
#     if a == "exit":
#         break
#     else:
#         b = int(a)
#     if b in oylar:
#         print(f"{b} chi oy {oylar[b]}")
#     else:
#         print("Bunday oy mavjud emas")



parol = input("parol kiriting: ")

xato = ["123", "321"]

if len(parol) <= 6:
    print("Parol 6 xonadan uzun bo`lishi kerak")
elif any(ketma_ket in parol for ketma_ket in xato):
    print("Parol boshida yoki ichida 123, 321 kabi ketma-ket raqamlar bo‘lmasin!")
else:
    print(f"Parol qabul qilindi: {parol}")
    
        
