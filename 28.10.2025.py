print("Bankomatga xush kelibsiz")

print("Bankomat 2 ta kartani qo‘llab quvvatlaydi: 1) Humo 2) Uzcard")

turi = input("Qanday karta kiritasiz >> ").lower().strip()

if turi == "humo" or turi == "uzcard":
    karta = input("Karta raqamini kiriting: ")

    if len(karta) != 12:
        print("Karta raqami 12 ta bo‘lishi kerak!")
    else:
        pin = input("Karta parolini kiriting (4 xonali): ")

        if len(pin) != 4:
            print("Xato parol kiritdingiz!")
        else:
            print("Parol to‘g‘ri kiritildi")

            if turi == "uzcard":
                hisob = 500_000
                sms_raqam = input("SMS ulangan telefon raqamini kiriting: ")
            else:
                hisob = 300_000
                sms_raqam = None

            for i in range(5):
                print("\nXizmatlar:")
                print("1) Pin kodni o‘zgartirish")
                print("2) Hisobni ko‘rish")
                print("3) Hisobdan pul yechish")
                if turi == "uzcard":
                    print("4) SMS raqamni o‘zgartirish")
                else:
                    print("4) SMS xizmati mavjud emas")
                print("5) Chiqish")

                xizmatlar = input("Xizmat raqamini kiriting: ")

                if xizmatlar == "1":
                    eski_parol = input("Eski parolni kiriting: ")
                    if eski_parol != pin:
                        print("Parol xato!")
                    else:
                        yangi_parol = input("Yangi parolni kiriting (4 xonali): ")
                        if len(yangi_parol) == 4:
                            pin = yangi_parol
                            print("Parol o‘zgartirildi")
                        else:
                            print("Parol 4 xonali bo‘lishi kerak!")

                elif xizmatlar == "2":
                    print(f"Hisobingizda {hisob} so‘m mavjud.")

                elif xizmatlar == "3":
                    print("Yechishingiz mumkin bo‘lgan summalar:")
                    print("1) 50000\n2) 200000\n3) 400000\n4) Boshqa summa")

                    tanla = input("Summani tanlang: ")

                    if tanla == "1":
                        ayir = 50_000
                    elif tanla == "2":
                        ayir = 200_000
                    elif tanla == "3":
                        ayir = 400_000
                    elif tanla == "4":
                        ayir = int(input("Xohlagan summani kiriting: "))
                    else:
                        print("Noto‘g‘ri tanlov!")
                        continue

                    if ayir > hisob:
                        print("Hisobingizda mablag‘ yetarli emas!")
                    else:
                        tasdiq = input(f"{ayir} so‘m yechilsinmi? (ha/yo‘q): ").lower()
                        if tasdiq == "ha":
                            hisob -= ayir
                            print(f"{ayir} so‘m yechildi. Hisobingizda {hisob} so‘m qoldi.")
                        else:
                            print("Pul yechish bekor qilindi.")

                elif xizmatlar == "4":
                    if turi == "uzcard":
                        eski_sms = input("Eski SMS raqamni kiriting: ")
                        if eski_sms == sms_raqam:
                            yangi_sms = input("Yangi SMS raqamni kiriting: ")
                            sms_raqam = yangi_sms
                            print("SMS raqam o‘zgartirildi")
                        else:
                            print("Eski raqam xato!")
                    else:
                        print("Humo kartasida SMS xizmati mavjud emas")

                elif xizmatlar == "5":
                    print("Foydalanganingiz uchun rahmat!")
                    break

                else:
                    print("Noto‘g‘ri xizmat raqami tanlandi!")

            print("\n--- Karta ma’lumotlari ---")
            print(f"Karta turi: {turi.upper()}")
            print(f"Karta raqami: {karta}")
            print(f"PIN kodi: {pin}")
            if turi == "uzcard":
                print(f"SMS raqam: {sms_raqam}")

else:
    print("Noto‘g‘ri karta turini kiritdingiz!")
