N = int(input())
l = [0] * N
for i in range(N):
    l[i] = int(input())

l.sort(reverse=True)

count = 1
for i in range(len(l)):
    if i + 1 < len(l):
        if l[i] > l[i + 1]:
            count += 1

print(count)