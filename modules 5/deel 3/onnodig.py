import random
import string

def generate_password():
    # --- RULES ---
    # 2–6 hoofdletters (geen in positie 11 en 12 → index 10 en 11)
    num_upper = random.randint(2, 6)

    # minimaal 8 kleine letters
    num_lower = 8

    # 3 speciale tekens (niet op eerste of laatste positie)
    special_chars = "@#$%&_?"
    num_special = 3

    # 4–7 cijfers (geen in eerste 3 posities)
    num_digits = random.randint(4, 7)

    # Check total so far → rest wordt opgevuld met kleine letters
    total_so_far = num_upper + num_lower + num_special + num_digits
    remaining = 24 - total_so_far

    # Extra kleine letters om tot 24 te komen
    num_lower += remaining

    # --- Create pools ---
    upper = random.choices(string.ascii_uppercase, k=num_upper)
    lower = random.choices(string.ascii_lowercase, k=num_lower)
    specials = random.choices(special_chars, k=num_special)
    digits = random.choices(string.digits, k=num_digits)

    # Combine alles
    password_list = upper + lower + specials + digits

    # Shuffle voorlopig
    random.shuffle(password_list)

    # --- Apply position rules ---

    # 1. Hoofdletters MOGEN NIET op positie 11 en 12
    for forbidden_index in (10, 11):
        if password_list[forbidden_index].isupper():
            # zoek een niet-hoofdletter om mee te ruilen
            for i in range(len(password_list)):
                if not password_list[i].isupper():
                    password_list[forbidden_index], password_list[i] = password_list[i], password_list[forbidden_index]
                    break

    # 2. Eerste 3 posities mogen GEEN cijfers bevatten
    for pos in range(3):
        if password_list[pos].isdigit():
            # zoek een niet-digit om te ruilen
            for i in range(3, len(password_list)):
                if not password_list[i].isdigit():
                    password_list[pos], password_list[i] = password_list[i], password_list[pos]
                    break

    # 3. Speciale tekens mogen NIET op eerste of laatste positie
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

    # 4. Laatste teken mag GEEN kleine letter zijn
    if password_list[-1].islower():
        # zoek een teken dat GEEN kleine letter is
        for i in range(len(password_list) - 2, -1, -1):
            if not password_list[i].islower():
                password_list[-1], password_list[i] = password_list[i], password_list[-1]
                break

    return "".join(password_list)


# ---- Run ----
print(generate_password())
