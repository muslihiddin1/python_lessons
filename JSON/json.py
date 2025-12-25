import json

# x = 10
# x_json = json.dumps(x)

# y = 5.5
# y_json = json.dumps(y)

# m = True
# m_json = json.dumps(m)

# # ism = "anvar"
# # ism_json = json.dumps(ism)
# # familiya_json = json.dumps('narzullaev')

# sonlar = (12, 45, 23, 67)
# sonlar_json = json.dumps(sonlar)


bemor = {
    "ism": "Alijon Valiyev",
    "yosh": 30,
    "oila": True,
    "farzandlar": ("Ahmad", "Bonu"),
    "allergiya": None,
    "dorilar": [
        {"nomi": "Analgin", "miqdori": 0.5},
        {"nomi": "Panadol", "miqdori": 1.2},
    ],
}

bemor_json = json.dumps(bemor)
print(bemor_json)

with open("JSON/bemor.json", "w") as f:
    json.dump(bemor_json, f)

#bemor2 = json.loads(bemor_json)

filename = "bemor.json"
with open(filename) as f:
    bemor = json.load(f)

print(type(bemor))





#    dumps() - o'zgaruvchini JSON formatiga o'tkazish
#    dump() - o'zgaruvchini JSON formatiga o'tkazish
#    load() - JSON formatini o'zgaruvchiga o'tkazish
#    loads() - JSON formatini o'zgaruvchiga o'tkazish