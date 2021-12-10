name = input("What is your name: ")
age = int(input("What is your age :"))
repeat_message = int(input("Please enter your favourite number: "))

Hundred_age = (100 - age)+2021

for i in range(repeat_message):
    print(name +"! , You will be hundred year old in :" + str(Hundred_age))

