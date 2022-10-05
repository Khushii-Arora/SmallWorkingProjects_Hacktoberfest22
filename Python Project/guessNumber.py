n = 18
tries = 0
print("You get 5 tries to guess the number!")

while True:
    tries += 1
    a = int(input("Guess a number: "))
    if tries<=4:
        if a > n:
            print("You guessed a higher number. Guess a lower number.")

        elif a < n:
            print("You guessed a lower number. Guess a higher number.")

        elif a == n:
            print("You guessed it correct. You win!!")
            print(f"You guessed it in {tries} tries!")
            break

    else:
        print("You exceeded the number of tries. You lose :( :( :(")
        print(f"The number is {n}.")
        break