
'''
var = input()

if int(var)>= 0 and int(var) <= 1000000:
    data = {0:9,1:8,2:7,3:6,4:5,5:4,6:3,7:2,8:1,9:0}
    ans = []
    for i in var:
        for key, val in data.items():
            if key==int(i):
                ans.append(str(val))
    ans = "".join(ans)
    print(ans)
else:
    print("Wrong Input")
'''

# 123876

var = input()

if int(var)>=0 and int(var) <=1000000:
    data = {"0":9, "1":8, "2":7, "3":6, "4":5, "5":4, "6":3, "7":2, "8":1, "9":0}
    for i in var:
        print(data[i], end="")

else:
    print("Wrong Input")


