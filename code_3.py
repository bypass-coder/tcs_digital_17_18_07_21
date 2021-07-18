

n = int(input())
data = []
for i in range(0,n):
    in_data = int(input())
    if in_data >=0:
        data.append(in_data)
# print(data)
# print(list(set(data)))
ans = []
for data_ele in data:
    if(data.count(data_ele)==1):
        ans.append(data_ele)

if len(ans)>0:
    print(ans[0])
else:
    print(1)


# 101,102,102,103 expected 103