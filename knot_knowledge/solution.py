n = int(input())
Xi = list(map(int, input().split()))
Yi = list(map(int, input().split()))
for i in range(n):
    if Xi[i] not in Yi:
        print(Xi[i])
        break
