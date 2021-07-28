

var = input()
if var.isdigit():
    if int(var) >=0 and int(var) <= 1000000:
        data = {'0':9,'1':8,'2':7,'3':6,'4':5,'5':4,'6':3,'7':2,'8':1,'9':0}

        for i in var:
            print(data[i],end="")
    else:
        print("Wrong Input")
else:
    print("Wrong Input")


# class Mobile:
#     def __init__(self,*data):
#         if len(data)>0:
#             self.data = data[0]

#     def __init__(self):
#         self.data = 0


# obj = Mobile(10)
# # obj2 = Mobile()

# print(obj.data)

# a = int()
# b = int()


# print(a)