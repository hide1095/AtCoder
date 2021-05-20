a = int(input())
b = int(input())
c = int(input())
x = int(input())

count = 0
for h in range(a + 1):
    for i in range(b + 1):
        for j in range(c + 1):
            money = x - 500 * (h) - 100 * (i) - 50 * (j)
            if money == 0:
                count += 1

print(count)