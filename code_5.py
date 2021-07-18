data = []
for i in range(0,11):
    data.append(int(input()))
hop = 0
i = 0
count = 0
while i < 11:
    step = data[i]
    hop += step
    i += step
    count += 1
    if hop >= 10:
        break
print(count)


