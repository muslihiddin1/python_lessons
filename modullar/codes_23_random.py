import random as r                                               # r - random ning qisqa nomi

#randint()

# son = r.randint(0,100)                                         # randint() - 0 dan 100 gacha istalgan son chiqarib beradi
# print(son)



#choice()

ismlar = ['olim','anvar','hasan','husan']                        # choice() - ro'yxatdan istalgan(tasodifiy) elementni chiqarib beradi
ism = r.choice(ismlar)
print(ism)
print(r.choice(ism))                                             # bu yerda tasodifiy tanlangan ismning ichidan istalgan harfini tanlaydi

x = list(range(0,51,5))                                          # 0 dan 50 ga bolgan sonni 5 talik qilib chiqaradi   [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
print(x)                                                         # va istalgan bittasini tanlaydi
print(r.choice(x))



#shuffle()    ---   inglizchada shuffle - aralasshtirib tashlamoq

x = list(range(0,11))                                            # 0 dan 10 gacha bo'lgan sonlar ro'yxatini yaratish
print(x)
r.shuffle(x)                                                     # ro'yxatni tasodifiy aralashtirib tashlaydi   masalan ---> bundan [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(x)                                                         #                                                           bunga  [3, 5, 7, 9, 8, 2, 1, 10, 0, 4, 6]





































# randint()
# son = r.randint(10,50)
# print(son)

# choice()
# ismlar = ['olim','anvar','hasan','husan']
# ism = r.choice(ismlar)
# print(ism)
# print(r.choice(ism))
# x = list(range(0,51,5))
# print(x)
# print(r.choice(x))

# shuffle()
# x = list(range(11))
# print(x)
# r.shuffle(x)
# print(x)