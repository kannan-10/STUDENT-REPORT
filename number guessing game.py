import random

lowest_num = 1 
highest_num = 100
answer = random.randint(lowest_num,highest_num)
guesses = 0
is_running=True

print("python number guess")

print(f"select number between {lowest_num} and {highest_num}")



while is_running :

    guess = input("enter you guess  ")

    if guess.isdigit():
        guess = int(guess)
        guesses += 1

        if guess < lowest_num or guess > highest_num:
            print("thr number is out of range")
            print(f"slecet the number between {lowest_num}and {highest_num}")
        elif guess < answer :
            print("too low! try again")

        elif guess > answer :
            print("too high!try again")

        else :
            print(f"corect the ansewr{answer}")
            print(f"guesse:{guesses}")

            is_running = False
    else:
        print("invalid number")
        print(f"slecet the number betwwen {lowest_num}and {highest_num}")



