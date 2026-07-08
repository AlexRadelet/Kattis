n = int(input())
prices = list(map(int, input().split()))
sorted_prices = sorted(prices)
second_price = sorted_prices[-2]
print(second_price)
