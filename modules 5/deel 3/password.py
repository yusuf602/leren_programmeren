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
