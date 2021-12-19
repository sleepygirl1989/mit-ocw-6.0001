a = [13, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [13, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

c= []
unique_list=[]

for i in a:
    for j in b :
        if i == j:
            if i not in c:
                c.append(i)
                c.sort()


print(c)