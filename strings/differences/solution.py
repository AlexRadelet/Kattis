n = int(input())
for i in range(n):
    diff = ""
    line1 = input()
    line2 = input()
    for j in range(len(line1)):
        if line1[j] != line2[j]:
            diff += "*"
        else:
            diff += "."
    print(line1)
    print(line2)
    print(diff + "\n")
