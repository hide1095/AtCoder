N = int(input())
l = list(map(int, input().split()))

count = 0
exist_odd = False
while True:
    for i in range(len(l)):
        if l[i] % 2 == 1:
            exist_odd = True
    if exist_odd:
        break
    for i in range(len(l)):
        l[i] /= 2
    count += 1
print(count)