s = input()

# 逆から読むことでprefix(被り)解消
dic = {1: "maerd", 2: "remaerd", 3: "esare", 4: "resare"}
s_r = s[::-1]

t = ""
for i in s_r:
    t = t + i
    if t in dic.values():
        t = ""

if len(t) == 0:
    print("YES")
else:
    print("NO")
