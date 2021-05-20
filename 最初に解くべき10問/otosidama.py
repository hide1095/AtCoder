n, y = map(int, input().split())
man, gosen, sen = -1, -1, -1
for a in range(n + 1):
    for b in range(n - a + 1):
        c = n - a - b
        goukei = 10000 * a + 5000 * b + 1000 * c

        if goukei == y:
            man, gosen, sen = a, b, c
            break


print("{} {} {}".format(man, gosen, sen))
