from math import pi

diameter = float(input())
width = float(input())
knights = float(input())

circumference = pi * diameter

print("YES" if width * knights <= circumference else "NO")
