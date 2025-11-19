# def bahola(ismlar):
#     baholar = {}
#     while ismlar:
#         ism = ismlar.pop()
#         baho = int(input(f"{ism.title()} uchun baho kiriting: "))
#         baholar[ism] = baho
#     return baholar
# talabalar = ['ali', 'vali', 'hasan', 'husan']
# talaba_baholari = bahola(talabalar[:])                                          # ro'yxatning nusxasini yuboramiz      [:] - nusxa olish belgisi
# print(talaba_baholari)
# print(talabalar)




# AMALIYOT
#01
# Matnlardan iborat ro'yxat qabul qilib, 
# ro'yxatdagi har bir matnning birinchi harfini katta harfga o'zgatiruvchi funksiya yozing.

# def katta_harf(matnlar):
#     for i in range(len(matnlar)):
#         matnlar[i]=matnlar[i].title()   

# ismlar = ['ali', 'vali', 'hasan', 'husan']
# katta_harf(ismlar)
# print(ismlar)




#02

#Yuoqirdagi funksiyani asl ro'yxatni o'zgartirmaydigan va yangi ro'yxat qaytaradigan qilib o'zgartiring

# def katta_harf(matnlar):
#     matnlar = matnlar[:]
#     for i in range(len(matnlar)):
#         matnlar[i]=matnlar[i].title()
#     return matnlar

# ismlar = ['ali', 'vali', 'hasan', 'husan']
# yangi_ismlar = katta_harf(ismlar)
# print(ismlar)
# print(yangi_ismlar)


#03

# Darsimiz davomida yozgan bahola funksiyasini .pop() metodidan foydalanmasdan 
# va asl ro'yxatga o'zgartirish kiritmasdan faqat lug'at qaytaradigan qilib yozing.

talabalar = ['ali', 'vali', 'hasan', 'husan']

def bahola(ismlar):
    baholar = {}
    for ism in ismlar:
        baho = input(f"Talaba {ism.title()}ning bahosini kiriting: ")
        baholar[ism]=baho
    return baholar
        
baholar = bahola(talabalar)
print(baholar)
print(talabalar)