import random

top_of_range = input("type a number : ")
if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0 :
        print("please type a number larger than 0 next time .")
        quit()

else:
    print("type a number next time .")
    quit()

random_number = random.randint(1, top_of_range)
print(random_number)

guesses = 0

while True:
    guesses += 1
    user_guess = input("guess a number : ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else :
        print("type a number next time .")
        continue

    if user_guess == random_number:
        print("you guessed right")
        break
    else:
        if user_guess > random_number:
            print("you were above the number!")
        else:
            print("you were below the number!")

print("you got it in ",guesses," guesses")


