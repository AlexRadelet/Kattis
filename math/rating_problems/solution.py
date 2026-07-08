n , k = map(int, input().split())
notes = []
for i in range(k):
    notes.append(int(input()))
if k < n:
    minNotes = (float(sum(notes)) + -3*(n-k))/n
    maxNotes = (float(sum(notes)) + 3*(n-k))/n
    print(minNotes, maxNotes)
if k == n:
    print(float(sum(notes))/n, float(sum(notes))/n)
