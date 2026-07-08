totalcases = int(input())

for _ in range(totalcases):
    case_num, num_of_dates = map(int, input().split())

    s = 0
    for j in range(1, num_of_dates + 1):
        s += j
        if j == num_of_dates:
            s += j

    print(case_num, s)
