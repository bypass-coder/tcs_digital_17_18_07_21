

n = input()
list_a = []
if n <= 100:
    for i in range(0,int(n)):
        # print((input())
        list_a.append(int(input()))
    

zero = []
one = []
two = []


for list_a_ele in list_a:
    if list_a_ele == 0:
        zero.append(str(list_a_ele))
    elif list_a_ele == 1:
        one.append(str(list_a_ele))
    else:
        two.append(str(list_a_ele))

data = one+zero+two
print(" ".join(data))







