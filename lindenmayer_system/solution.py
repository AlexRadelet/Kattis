r, n = map(int, input().split())

rules = {}
for _ in range(r):
    left, right = input().split(" -> ")
    rules[left] = right

current = input()

for _ in range(n):
    current = "".join(rules.get(c, c) for c in current)

print(current)
