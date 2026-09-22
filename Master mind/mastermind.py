import mastermind_funcs

code = mastermind_funcs.generate_code()
guess = []
attempts = 10


while True:

    print(code)

    valid_guess = True

    for b in range(1, 5):
        
        try:
            user_guess = int(input(f"Guess digit {b}: "))
        except ValueError:
            print("Must be a number")
            guess.clear()
            continue
        else:

            user_guess = str(user_guess)
            if len(user_guess) > 1:
                input("Enter only one number \n [Enter]")
                valid_guess = False
                
            else: 
                user_guess = int(user_guess)
                guess.append(user_guess)
                print(guess)

    if not valid_guess:
        guess.clear()
        continue
         
    if guess == code:
        print("You win")
        exit()
    elif attempts == 0:
        print("You lose")
        exit()
    else: 
        attempts -= 1
        input(f"\n You have {mastermind_funcs.right_position(guess, code)} correct \n You have {mastermind_funcs.wrong_position(guess, code)} in the wrong spot \n Attempts remaining : {attempts} \n [Enter] ")
        guess.clear()

    

