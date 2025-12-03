# import avto_info_mod

# avto1 = avto_info_mod.avto_info("GM", "Malibu", "Qora", "avtomat", 2020,40000)
# avto_info_mod.info_print(avto1)

# import avto_info_mod as aim

# avto1 = aim.avto_info("GM", "Malibu", "Qora", "avtomat", 2020,40000)
# aim.info_print(avto1)

# from avto_info_mod import avto_info, info_print

# avto1 = avto_info("GM", "Malibu", "Qora", "avtomat", 2020,40000)
# info_print(avto1)

# from avto_info_mod import avto_info as ainfo, info_print as iprint

# avto1 = ainfo("GM", "Malibu", "Qora", "avtomat", 2020,40000)
# iprint(avto1)

# from avto_info_mod import *

# avto1 = avto_info("GM", "Malibu", "Qora", "avtomat", 2020,40000)
# info_print(avto1)

# avtolar = avtoil.avto_kirit()

# for avto in avtolar:
#     avtoil.info_print(avto)

































# modulni yuklash va foydalanish
#1
 
# import avto_info_mod                                                                # import - modulni yuklash, uni chaqirish uchun ishlatiladi

# avto1 = avto_info_mod.avto_info("GM", "Malibu", "Qora", "avtomat", 2020,40000)
# avto_info_mod.info_print(avto1)



# #2
# import avto_info_mod as aim                                                         # aim - avto_info_mod  uni qisqartirib keyin faqat shu nom bilan ishlatsa bo'ladi

# avto1 = aim.avto_info("GM", "Malibu", "Qora", "avtomat", 2020,40000)
# aim.info_print(avto1)



# #3
# from avto_info_mod import avto_info, info_print                                     # avto_info va info_print - modul ichidagi funksiyalar

# avto1 = avto_info("GM", "Malibu", "Qora", "avtomat", 2020,40000)
# info_print(avto1)                                                                   # endi bu yerda qayta qayta yozish kerak emas.



# #4
# from avto_info_mod import avto_info as ainfo, info_print as iprint

# avto1 = ainfo("GM", "Malibu", "Qora", "avtomat", 2020,40000)
# iprint(avto1)



#5 
from avto_info_mod import *                                                          # * - bu avto_info_mod ichidagi barcha funksiyalarni chaqirib oladi

avto1 = avto_info("GM", "Malibu", "Qora", "avtomat", "2020", "40000")
info_print(avto1)





