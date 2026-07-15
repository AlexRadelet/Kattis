N = int(input())

used_words = set()
previous = None

for i in range(1, N + 1):
    word = input()

    if word in used_words:
        print(f"Player {1 if i % 2 else 2} lost")
        break

    if previous is not None and word[0] != previous[-1]:
        print(f"Player {1 if i % 2 else 2} lost")
        break

    used_words.add(word)
    previous = word
else:
    print("Fair Game")
