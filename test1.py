
number_list= [1,1,2, 3, 5, 8, 13, 21, 34, 55, 89]
less_than_five =[]
user_list_check =[]

for i in number_list:
    if i < 5:
        less_than_five.append(i)
print(less_than_five)

def user_number_check(num):
    for i in number_list:
        if i < num:
            user_list_check.append(i)
    return user_list_check

x = int(input("Please enter a number :"))
print(user_number_check(x))


