

data = input()

ans_list = []

if len(data) < 5:
    for i in range(0,len(data)):
        for j in range(i,len(data)):
            ans_list.append(int(data[i:j+1]))
    print(sum(ans_list))
else:
    print(-1)



