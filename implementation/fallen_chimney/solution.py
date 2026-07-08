n = int(input())
secure = 0
for i in range(n):
    i, note = input().split()
    if note =="nej":
        if int(i) > secure:
            secure = int(i)
print(secure)
