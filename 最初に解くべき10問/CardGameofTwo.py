N = input()
l = list(map(int, input().split()))

Alice = 0
Bob = 0
"""
length = len(l)
for idx in range(length):
    if idx % 2 == 0:
        Alice += max(l)
        l.remove(max(l))

    else:
        Bob += max(l)
        l.remove(max(l))

print(Alice - Bob)
"""

l.sort(reverse=True)
for idx in range(len(l)):
    if idx % 2 == 0:
        Alice += l[idx]

    else:
        Bob += l[idx]

print(Alice - Bob)
