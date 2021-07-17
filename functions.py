import random, json, os

list_of_chars = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ&é\"\'()-è_çà=~#}{[]|`\\^°+¨¤£%ù$*µ!§/:;.,?<>² "
CUR_DIR = os.path.dirname(os.path.abspath(__file__))
PATH = CUR_DIR + '\DATA\password.json'

def generator(min, max, cap, nbr, spe):
    password = ""

    if cap == False and nbr == False and spe == False:
        list_of_chars = "abcdefghijklmnopqrstuvwxyz"
    elif cap == True and nbr == False and spe == False:
        list_of_chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    elif cap == False and nbr == True and spe == False:
        list_of_chars = "abcdefghijklmnopqrstuvwxyz0123456789"
    elif cap == False and nbr == False and spe == True:
        list_of_chars = "abcdefghijklmnopqrstuvwxyz&é\"\'()-è_çà=~#}{[]|`\\^°+¨¤£%ù$*µ!§/:;.,?<>²"
    elif cap == True and nbr == True and spe == False:
        list_of_chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    elif cap == False and nbr == True and spe == True:
        list_of_chars = "abcdefghijklmnopqrstuvwxyz0123456789&é\"\'()-è_çà=~#}{[]|`\\^°+¨¤£%ù$*µ!§/:;.,?<>²"
    elif cap == True and nbr == False and spe == True:
        list_of_chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ&é\"\'()-è_çà=~#}{[]|`\\^°+¨¤£%ù$*µ!§/:;.,?<>²"
    elif cap == True and nbr == True and spe == True:
        list_of_chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789&é\"\'()-è_çà=~#}{[]|`\\^°+¨¤£%ù$*µ!§/:;.,?<>²"

    nbr_list_char = -1
    for i in list_of_chars:
        nbr_list_char += 1

    v = random.randint(min, max)
    while v != 0:
        password += list_of_chars[random.randint(0, nbr_list_char)]
        v -= 1

    return password

def solver():

    with open(PATH, "r") as f:
        password = json.load(f)
    password = password[0]
    attempted_password = ""

    for character in password:
        for entry in list_of_chars:
            if character == entry:
                attempted_password += character
                continue

    length = 0
    for char in password:
        length += 1

    return [password, length]

def writePassword(pwrd):
    res = []
    res.append(str(pwrd))
    with open(PATH, "w") as f:
        json.dump(res, f, indent=4)