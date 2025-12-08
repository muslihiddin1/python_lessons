# import random
# from uzwords import words

# def get_word(words):
#     word = random.choice(words)
#     while "-" in word or " " in word:
#         word = random.choice(words)
#     return word.upper()

# def display(user_later, words):
#     display_word = ""
#     for letter in words:
#         if letter in user_later.upper():
#             display_word += letter
#         else:
#             display_word += "-"
#     return display_word

# def play():
#     word = get_word(words)
#     word_letters = set(word)
#     user_letters = ''
#     print(f"Men {len(word)} ta harfli so'z o'yladim. Topa olasizmi?")
#     while len(word_letters) > 0:
#         print(display(user_letters, word))
#         if len(user_letters) > 0:
#             print(f"Shu vaqtgacha kiritgan harflaringiz: {user_letters}")
#         letter = input("Harf kiriting: ").upper()
#         if letter in user_letters:
#             print("Bu ha harfni oldin kiritdingiz!")
#             continue
#         elif letter in word:
#             word_letters.remove(letter)
#             print(f"{letter} harfi to'g'ri!")
#         else:
#             print("Bunday harf mavjud emas!") 
#             user_letters += letter
#         print(f"Tabriklayman! {word} so'zini {len(user_letters)} ta taxmin bilan topdingiz!")
        
# play()
























import random
from uzwords import words


def get_word():
    word = random.choice(words)
    while "-" in word or " " in word:
        word = random.choice(words)
    return word.upper()


def display(user_letters, word):
    display_letter = ""
    for letter in word:
        if letter in user_letters:
            display_letter += letter
        else:
            display_letter += "-"
    return display_letter


def play():
    word = get_word()
    # So'zdagi harflar
    word_letters = set(word)
    # Foydalanuvchi kiritgan harflar
    user_letters = ""
    print(f"Мен {len(word)} хонали сўз ўйладим. Топа оласизми?")
    # print(word)
    while word_letters:
        print(display(user_letters, word))
        if user_letters:
            print(f"Шу вақтгача киритган ҳарфларингиз: {user_letters}")

        letter = input("Ҳарф киритинг: ").upper()
        if letter in user_letters:
            print("Бу ҳарфни аввал киритгансиз. Бошқа ҳарф киритинг.")
            continue
        elif letter in word:
            word_letters.remove(letter)
            print(f"{letter} ҳарфи тўғри.")
        else:
            print("Бундай ҳарф йўқ.")
        user_letters += letter
    print(f"Табриклайман! {word} сўзини {len(user_letters)} та уринишда топдингиз.")
    
play()