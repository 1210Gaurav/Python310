def nextpalindrome(n):
    n = n + 1
    a = str(n)
    while a != a[::-1]:
        n += 1
        a = str(n)
    print(f"Next palindrome is {n}")

if __name__ == '__main__':
    while True:
        num = input("Enter the number to find the next consecutive palindrome of a given number\n")
        if num.isnumeric() and len(num) > 1:
            nextpalindrome(int(num))
        elif num.isnumeric() and len(num) == 1 :
            print(f"System dont know to find palindrome of single number {num}!!")
            continue
        else:
            print(f"{num} is not a number. Please enter a number!!")
            continue

        while True:
            user_choice=input("Do you want to continue? 'y' for YES AND 'n' for NO\n")
            if user_choice not in ("y","n"):
                continue
            else:
                break
        if user_choice.upper() == "Y":
            continue
        else:
            break


