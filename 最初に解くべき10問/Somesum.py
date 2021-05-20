N, A, B = map(int, input().split())

souwa = 0
ketano_sum = 0
for i in range(N):
    si = str(i + 1)
    for num in range(len(si)):
        ketano_sum += int(si[num])
    if A <= ketano_sum <= B:
        souwa += i + 1
    ketano_sum = 0

print(souwa)