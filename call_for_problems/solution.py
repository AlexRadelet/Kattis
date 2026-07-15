n = int(input())
SUM = 0
for i in range(n):
    problem = int(input())
    if problem%2 != 0:
        SUM += 1
print(SUM)
