num = int(input())

n1 = 0
n2 = 1
print(n1,end=", ")
print(n2,end=", ")

for i in range(2,num):
    n3 = n1 + n2
    n1 = n2
    n2 = n3
    if i == num - 1:
        print(n3,end="")
    else:
        print(n3,end=", ")
    

