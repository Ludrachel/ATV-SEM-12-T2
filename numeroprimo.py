num = int(input())

num_primo = True

for i in range(2,num):
    if num % i == 0:
        num_primo = False
        break
if num_primo:
    print("True")
else:
    print("False")
