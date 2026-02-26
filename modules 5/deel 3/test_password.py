# password 24 karakters lang!
# Random 2 tot 6 hoofdletters.
# Een hoofdletter mag niet op de twee middelste posities staan.
## Minimaal 8 kleine letters.
## Het wachtwoord mag niet met een kleine letter eindigen.
# 3 speciale tekens uit de volgende reeks: @ # $ % & _ ?.
## De speciale tekens mogen niet op de eerste of laatste positie staan.
# Random 4 tot 7 cijfers (0 t/m 9).
## Op de eerste 3 posities mag geen cijfer staan
import time, string

def test_wachtwoord(ww) -> bool:
    if len(ww) < 24:
        print('te kort')
        return False
    if not 1 < len(list(filter(lambda a: a in string.ascii_uppercase, list(ww)))) < 7:
        print('aantal hoofdletters klopt niet!')
        return False
    if ww[11] in string.ascii_uppercase or ww[12] in string.ascii_uppercase:
        print('In het midden geen hoofdletters')
        return False
    if len(list(filter(lambda a: a in string.ascii_lowercase, list(ww)))) < 8:
        print('te weinig kleine letters')
        return False
    if ww[-1] in string.ascii_lowercase:
        print('Laatste pos niet juist')
        return False
    if len(list(filter(lambda a: a in '@#$%&_?', list(ww)))) != 3:
        print('te weinig specials')
        return False
    if ww[0] in '@#$%&_?' or ww[-1] in '@#$%&_?':
        print('special op end')
        return False
    if not 3 < len(list(filter(lambda a: a.isdigit(), list(ww)))) < 8:
        print('te weinig getallen')
        return False
    if ww[0].isdigit() or ww[1].isdigit() or ww[2].isdigit():
        print('Eerste drie karakters staat een getal')
        return False
    return True

def get_wachtwoord():
    return 'wachtwoord'
import random
import string

def generate_password():
    num_upper = random.randint(2, 6)
    num_lower = 8  
    special_chars = '@#$%&_?'
    num_special = 3
    num_cijfers = random.randint(4, 7)
    total_so_far = num_upper + num_lower + num_special + num_cijfers
    remaining = 24 - total_so_far
    num_lower += remaining


    upper = random.choices(string.ascii_uppercase, k=num_upper)
    lower = random.choices(string.ascii_lowercase, k=num_lower)
    special = random.choices(special_chars, k=num_special)
    cijfers = random.choices(string.digits, k=num_cijfers)
    password_list = upper + lower + special + cijfers

    random.shuffle(password_list)
    for forbidden_index in (10, 11):
        if password_list[forbidden_index].isupper():
            for i in range(len(password_list)):
                if not password_list[i].isupper():
                    password_list[forbidden_index], password_list[i] = password_list[i], password_list[forbidden_index]
                    break

    for pos in range(3):
        if password_list[pos].isdigit():
            for i in range(3, len(password_list)):
                if not password_list[i].isdigit():
                    password_list[pos], password_list[i] = password_list[i], password_list[pos]
                    break
    if password_list[0] in special_chars:
        for i in range(1, len(password_list) - 1):
            if password_list[i] not in special_chars:
                password_list[0], password_list[i] = password_list[i], password_list[0]
                break
    if password_list[-1] in special_chars:
        for i in range(1, len(password_list) - 1):
            if password_list[i] not in special_chars:
                password_list[-1], password_list[i] = password_list[i], password_list[-1]
                break
    if password_list[-1].islower():
        for i in range(len(password_list) - 2, -1, -1):
            if not password_list[i].islower():
                password_list[-1], password_list[i] = password_list[i], password_list[-1]
                break

    return "".join(password_list)

print(generate_password())


# plaats hier de code om minimaal 500 wachtwoorden te testen.