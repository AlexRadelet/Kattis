def can_fill(x, helium, n):
    index = 0

    for capacity in range(1, n + 1):
        while index < n and helium[index] < x * capacity:
            index += 1

        if index == n:
            return False

        if helium[index] > capacity:
            return False

        index += 1

    return True


n = int(input())
helium = list(map(int, input().split()))
helium.sort()

if not can_fill(0, helium, n):
    print("impossible")
else:
    left = 0.0
    right = 1.0

    for _ in range(60):
        mid = (left + right) / 2
        if can_fill(mid, helium, n):
            left = mid
        else:
            right = mid

    print(f"{left:.10f}")
