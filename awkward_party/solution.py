n = int(input())
numbers = list(map(int, input().split()))

last_seen = {}
answer = n

for i, lang in enumerate(numbers):
    if lang in last_seen:
        answer = min(answer, i - last_seen[lang])
    last_seen[lang] = i

print(answer)
