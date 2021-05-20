N, A, B = map(int, input().split())
goukei = 0


def souwa(n):
    summ = 0
    while n > 0:
        summ += n % 10
        n = n // 10
    return summ


for i in range(N):
    if A <= souwa(i + 1) <= B:
        goukei += i + 1
print(goukei)