def findage():
    if len(user_input) == 2:
        finalageyear= (currentyear - int(user_input)) + 99
    else:
        finalageyear=int(user_input)+100

    print(f"Your age will be 100 in the year {finalageyear}. Still long way to Go.")

def findyear():

    while True:
        user_input1 = input("Enter the year to know your age: \n")
        if user_input1.isnumeric():
            break
        else:
            print(f"Invalid input {user_input1}!!")

    if len(user_input) == 2:
        birthyear = (currentyear - int(user_input))
        finalyearage = (int(user_input1) - int(birthyear))
    else:
        finalyearage = (int(user_input1) - int(user_input))

    if finalyearage > 0:
        print(f"You will be {finalyearage} year in the year {user_input1}")
    else:
        print("You have successfully time traveled. Congratulations!!")


if __name__ == '__main__':

    import time
    currentyear = time.localtime().tm_year

    while True:

        while True:
            user_input = input("Enter your 'Age' or 'Year of birth': \n")
            if user_input.isnumeric():
                break
            else:
                print(f"Invalid input {user_input}!!")

        print("Enter number 1 to get the year you will be 100 years old")
        print("Enter number 2 to know your age for your entered year")

        while True:
            choice = input("Enter your choice of number: \n")

            if choice in ("1","2"):
                break
            else:
                print(f"Invalid Input{choice}!!")

        match int(choice):
            case 1:
                findage()

            case 2:
                findyear()

        while True:
            user_continue = input("Do you still want to continue? Press Y for 'Yes' and N for 'No': \n").upper()

            if user_continue in ("Y", "N"):
                break
            else:
                print(f"Invalid input {user_continue} .Kindly enter Y or N")

        if user_continue == "Y":
            continue
        elif user_continue == "N":
            break



