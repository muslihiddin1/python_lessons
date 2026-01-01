#1     ValueError - kiritilgan qiymat xato bo'lishi mumkin

# yosh = input("Yoshingizni kiriting: ")

# try:
#     yosh = int(yosh)
# except ValueError:
#     print("Siz butun son kiritmadingiz.")
# else:
#     print(f"Siz {2025-yosh} yilda tug'ilgaysiz.")





#2     ZeroDivisionError - 0 ga bo'lib bo'lmaydi

# x,y = 5,10
# try:
#     y/(x-5)
# except ZeroDivisionError:
#     print("0 ga bo'lib bo'lmaydi")
    
    
    
    
#3     IndexError - listning indexi noto'g'ri bo'lishi mumkin

# mevalar = ["olma", "banan", "shaftoli"]
# try:
#     print(mevalar[5])
# except IndexError:
#     print(f"Listda {len(mevalar)} ta meva bor.")






#4     KeyError - lug'atning kaliti noto'g'ri bo'lishi mumkin

# user = {"username": "muslihiddin_nurmamatov",
#         "email": "muslihiddinnurmamatov1gmail.com",
#         "phone": "+998 97 295 56 16"}
# key = "password"
# try:
#     print(f"foydalanuvchi: {user[key]}")
# except KeyError:
#     print("Kechirasiz, bunday kalit mavjud emas.")
    
    
    
    
    
    
    
#5     FileNotFoundError - bunday fayl yo'q

# filename = "L.txt"
# try:
#     with open(filename) as file:
#         print(file.read())
# except FileNotFoundError:
#     print(f"Kechirasiz, {filename} fayli mavjud emas.")






#6     bir nechta except lardan foydalanish mumkin

# n = input("Butun son kiriting: ")
# try:
#     n = int(n)
#     x = 20/n
# except ValueError:
#     print("Siz butun son kiritmadingiz.")
# except ZeroDivisionError:
#     print("0 ga bo'lib bo'lmaydi")
# else:
#     print(f"x={x} ga teng")







#7     except bilan emas while yordamida foydalanish mumkin

while True:
    yosh = input("Yoshingizni kiriting: ")
    if yosh.isdigit():                                                         # isdigit() - butun sonligini tekshiradi
        yosh = int(yosh)
        break
    
print(f"Siz {2025-yosh} yilda tug'ilgaysiz.")