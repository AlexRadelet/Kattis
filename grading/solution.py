a,b,c,d,e = map(int, input().split())
examScore = int(input())
if examScore >= a:
    print("A")
elif examScore >= b:
    print("B")
elif examScore >= c:
    print("C")
elif examScore >= d:
    print("D")
elif examScore >= e:
    print("E")
else:
    print("F")
