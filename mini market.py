print("Mini marketga xush kelibsiz!")

mevalar = {
    "nok": 25000,
    "olma": 30000,
    "anor": 45000,
    "behi": 16000,
    "uzum": 19000,
    "gilos": 17000,
    "banan": 27000
}

jami = 0
for i in range(3):
    a = input(f"{i+1}-chi mahsulotni tanlang: ").lower()
    if a in mevalar:
        b = float(input(f"{a} dan nechta kerak (kg yoki dona): "))
        jami += mevalar[a] * b
    else:
        print("Bu meva mavjud emas!")

asil = jami
if jami >= 100000:
    jami -= jami * 0.1
    print(f"10% chegirma qo‘llandi! Eski summa: {asil:.0f} so‘m, yangi summa: {jami:.0f} so‘m")
else:
    print(f"Umumiy summa: {jami:.0f} so‘m (chegirmasiz)")

turi = int(input("\nTo‘lov turini tanlang:\n1) Naqd\n2) Karta\n>>"))

if turi == 1:
    print("Naqd to‘lovni kiriting.")
elif turi == 2:
    karta_turi = int(input("1) Uzcard yoki 2) Humo tanlang: "))
    if karta_turi == 1:
        hisob = 300000
        print("Siz Uzcard kartasini tanladingiz.")
    elif karta_turi == 2:
        hisob = 200000
        print("Siz Humo kartasini tanladingiz.")
    else:
        print("Noto‘g‘ri raqam tanlandi.")
    raqam = input("Karta raqamini kiriting: ")
else:
    print("To‘lov turi noto‘g‘ri tanlandi.")

print(f"\nXaridingiz uchun rahmat! Yakuniy summa: {jami:.0f} so‘m")
