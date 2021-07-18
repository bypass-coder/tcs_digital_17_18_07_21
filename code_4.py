
data = input()
ans = ord(data[0])
for i in range(1, len(data)):
    ans ^= ord(data[i])
print(ans)



