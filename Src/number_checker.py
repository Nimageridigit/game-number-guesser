from number_generator import random_num
wg=0        #wrong guess

while True:
    try:
        user_number=int(input("Please enter a number between 0 and 100:"))
        if 0 <= user_number <= 100:
            if user_number == random_num:
                print("!! YOU WIN !!")
                print(f"You guessed the number in {wg} wrong guesses")
                wg_count=wg
                break
            elif user_number < random_num:
                wg +=1
                print("Wrong guess... Try a bigger number")
            elif user_number > random_num:
                wg +=1
                print("Wrong guess... Try a smaller number")
        else:
            print("Your number should be between 0 and 100")
        
    except ValueError:
        print("***ONLY ENTER A NUMBER***")