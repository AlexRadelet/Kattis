a,b = map(int, input().split())
alcoholA, alcoholB = 0,0
for i in range(a):
    v, c =map(int, input().split())
    alcoholA += v*c
for i in range(b):
    v, c =map(int, input().split())
    alcoholB += v*c
if alcoholA != alcoholB:
    print("different")
else:
    print("same")
