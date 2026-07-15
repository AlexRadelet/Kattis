h, w, l, c = map(int, input().split())

if h*w*l > c:
    print("SO MUCH SPACE")
if h*w*l == c:
    print("COZY")
if h*w*l < c:
    print("TOO TIGHT")
