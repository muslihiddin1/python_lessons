import pickle                                                                   # pickle - o'zgaruvchini saqlashda yordam beradi

talaba1 = {
    "ism": "Muslihiddin",
    "familiya": "Nurmamatov",
    "yosh": 17,
    "kurs": 3
}

talaba2 = {
    "ism": "Ne'matulloh",
    "familiya": "Nurmamatov",
    "yosh": 19,
    "kurs": 3
}


with open("fayllar_bn_ishlash/info", "wb") as file:                            # wb - write binary
    pickle.dump(talaba1, file)
    pickle.dump(talaba2, file)
    