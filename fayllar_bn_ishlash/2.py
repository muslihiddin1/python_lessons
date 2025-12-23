import pickle                                                                       # pickle - o'zgaruvchini saqlashda yordam beradi

with open("fayllar_bn_ishlash/info", "rb") as file:                                  # rb - read binary
    talaba1 = pickle.load(file)
    talaba2 = pickle.load(file)
    
print(talaba1)
print(talaba2)