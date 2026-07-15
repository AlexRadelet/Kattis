n = int(input())
book = {}
for _ in range(n):
    word, page = input().split()
    book[int(page)] = word

print(" ".join(book[i] for i in range(1, n + 1)))
