# file = open("fayllar_bn_ishlash/pi.txt")
# pi = file.read()
# file.close()
# print(pi)




# with open("fayllar_bn_ishlash/pi.txt") as file:
#     pi = file.read()

# print(pi)

# pi = pi.rstrip()
# pi = pi.replace("/n", "")
# #pi = float(pi)
# print(pi)






# 1- usul
# filename = "fayllar_bn_ishlash/talabalar.txt"
# with open(filename) as file:
#     for line in file:
#         print(line)



# 2- usul
# filename = "fayllar_bn_ishlash/talabalar.txt"
# with open(filename) as file:
#     talabalar = file.readlines()
# print(talabalar)

# talabalar = [talaba.rstrip() for talaba in talabalar]                       # rstrip() - /n belgini olib tashlaydi
# print(talabalar)










# yangi fayl ochish

# faylnomi = "fayllar_bn_ishlash/newfile.txt"
# ism = "Muslihiddin Nurmamatov"
# tyil = 2008
# with open(faylnomi, "w") as file:
#     file.write(ism+"\n")
#     file.write(str(tyil)+"\n")
    
    
    
# mavjud faylni ichiga yozish

faylnomi = "fayllar_bn_ishlash/newfile.txt"
with open(faylnomi, "a") as file:
    file.write("Ne'matulloh Nurmamatov\n")
    file.write("2006")