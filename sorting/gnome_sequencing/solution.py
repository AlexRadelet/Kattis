n = int(input())
print("Gnomes:")
for i in range(n):
    line = list(map(int, input().split()))
    if sorted(line) == line or sorted(line, reverse=True) == line:
        print("Ordered")
    else:
        print("Unordered")
