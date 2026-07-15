N = int(input())
SUM = 0
for i in range(N):
    person, direction, num = input().split()
    if direction == "IN":
        SUM += int(num)
    if direction == "OUT":
        SUM -= int(num)
if SUM == 0:
    print("NO STRAGGLERS")
else:
    print(SUM)
