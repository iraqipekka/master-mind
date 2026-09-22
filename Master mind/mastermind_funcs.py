import random

def generate_code():

    code = []

    
    for _ in range(4):
        n = random.randint(0,5)
        code.append(n)

    return code


def right_position(guess, code):

    correct_amount = 0

    for i in range(4):
        if guess[i] == code[i]:
            correct_amount += 1

    return correct_amount


def wrong_position(guess, code):

    wrong_spot = 0

    already_checked = []

    for i in range(4):
        if guess[i] == code[i]:
            already_checked.append(i)

    for a in range(4):

        for b in range(4):

            if guess[a] == code[b] and guess[a] != code[a] and b not in already_checked:
                wrong_spot += 1
                already_checked.append(b)
                break

    return wrong_spot




    
