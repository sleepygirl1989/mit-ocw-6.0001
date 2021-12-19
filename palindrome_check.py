user_string = input("Please enter a word : ")
list_check =[]
even_check = len(user_string)%2

for i in user_string:
    list_check.append(i)
print(list_check)

reverse_list =list_check[:]
reverse_list.reverse()
print(reverse_list)
print(list_check)

if list_check == reverse_list:
    print("palindrome")
else:
    print("not a palindrome")





