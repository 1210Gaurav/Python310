import random


def guess_my_num(user_num, comp_num):
    if user_num > guess_num:
        if (user_num - guess_num) > 10:
            print("The guessed number is much greater than my number, Give another try!")
        else:
            print("The guessed number is greater than my number, Give another try!")
        return 0
    elif user_num < guess_num:
        if (guess_num - user_num) > 10:
            print("The guessed number is much lesser than my number, Give another try!")
        else:
            print("The guessed number is lesser than my number, Give another try!")
        return 0
    else:
        return 1


if __name__ == '__main__':
    print("Guess the number in the range 50!! ", "Instructions: ",
          "1.Computer will choose a random number that will in the range 1 to 50 ",
          "2.You will have only 10 attempts to guess the number ",
          "3.Computer will provide the hint based on your inputs ", sep="\n")
    flag, i = 0, 0

    guess_num = random.randint(0, 50)

    while i < 10 and flag == 0:
        print(f"You have {10 - i} attempts left")
        userint = int(input("Enter your guess \n"))

        flag = guess_my_num(userint, guess_num)
        i += 1

    if flag == 1:
        print(f"Congratulations!! You guess the number in {i} attemptes")
    elif i > 10:
        print(f"Try again!! The number was {guess_num}")
