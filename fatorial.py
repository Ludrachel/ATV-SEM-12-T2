num = int(input())
fatorial = 1
for i in range(1,num+1):
    if num == 0:
        fatorial = 1
    fatorial *= i
print(fatorial)
