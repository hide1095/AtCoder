n = int(input())
t = [0] * (n + 1)
x = [0] * (n + 1)
y = [0] * (n + 1)
for i in range(1, n + 1):
    t[i], x[i], y[i] = map(int, (input().split()))

count = 0
for i in range(1, n + 1):
    x_d = x[i] - x[i - 1]
    y_d = y[i] - y[i - 1]
    # 移動距離と経過時間
    dist = abs(x_d) + abs(y_d)
    dt = t[i] - t[i - 1]
    if dist > dt:
        break

    # １秒毎に偶奇が入れ替わるパリティ
    elif dist % 2 == dt % 2:
        count += 1

if count == n:
    print("Yes")
else:
    print("No")
