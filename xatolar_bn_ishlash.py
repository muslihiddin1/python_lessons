# TypeError
# son = input("Istalgan son kiriting: ")                      #int ga o'zgartirish kerak
# print(f"{son} ning kvadrati {son**2} ga teng")              #bu yerda xato chiqadi, chunki input() funksiyasi string qaytaradi va stringni kvadratga ko'tarib bo'lmaydi.







# NameError
# prit("Salom Dunyo!")                                        #print() deb yozilishi kerak edi
# mevalar = ["olma", "banan", "shaftoli"]
# for meva in mvalar:                                         #mevalar deb yozilishi kerak edi
#     print(meva)





#ValueError
# son = int(input("Istalgan son kiriting: "))                # bu yerda agar masalan 34.4 qilib o'nlik son kirgizsa xato beradi           
# if son >=0:                                                chunki int faqat butun songa bu yerda int ni orniga float qilish kerak edi
#     print("Musbat son")
# else:
#     print("Manfiy son")









# IndexError
# mevalar = ["olma", "banan", "shaftoli"]
# print(mevalar[3])                                          # ro'yxatda faqat 0,1,2 indekslari bor, 3-indeks yo'q








# ZeroDivisionError
# x, y = 50, 50
# z = 250 / (x - y)                                          # x va y teng bo'lgani uchun (x-y) 0 ga teng bo'ladi va nolga bo'lish xatosi yuz beradi










# Mantiqiy xatolar (Logic Error)      ##  O'ZIMIZ QILADIGAN XATO  ##
# radius = 5
# pi = 4.14                                                 # pi ning qiymati noto'g'ri berilgan, to'g'ri qiymat 3.14 bo'lishi kerak
# aylana_yuzi = pi * radius**2
# print("Aylananing yuzi:", aylana_yuzi)   



# son = float(input("Istalgan son kiriting: "))
# ildiz = son ** 1/2                                        # bu yerda ildizni hisoblashda mantiqiy xato bor, to'g'ri ifoda son ** 0.5  yoki (1/2) bo'lishi kerak
# print(f"{son} sonining ildizi {ildiz} ga teng")     



mevalar = ["olma", "banan", "shaftoli"]
for meva in mevalar:
    print(meva)
    print("Dastur tugadi.")                               # bu yerda dastur tugadi har bir meva uchun alohida chiqadi, 
                                                            #agar faqat oxirida chiqishini istasak, uni for tsiklidan tashqarida yozish kerak. 
                                                            #yani print("Dastur tugadi.") ni chapga bir tab orqaga surish kerak.
                                                            
                                                            
                                                          