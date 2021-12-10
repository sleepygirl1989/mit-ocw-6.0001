number=int(input("Enter number : "))



if number > 0:
    check_condition = number % 2
    if check_condition == 0:
        if number %4 ==0:
            print("Your number is even and divisible by 4 !")
        else:
            print("You have entered even number !")


    else:
        print("You have entered odd number!")
else:
    print("You need to input positive number !")