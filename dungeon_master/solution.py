import sys
from collections import deque

MOVES = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]


def main():
    lines = sys.stdin.read().split("\n")
    pos = 0

    def next_line():
        nonlocal pos
        while lines[pos].strip() == "":
            pos += 1
        line = lines[pos]
        pos += 1
        return line

    output = []
    while True:
        levels, rows, cols = map(int, next_line().split())
        if levels == rows == cols == 0:
            break

        grid = [[next_line() for _ in range(rows)] for _ in range(levels)]
        start = end = None
        for l in range(levels):
            for r in range(rows):
                for c in range(cols):
                    if grid[l][r][c] == "S":
                        start = (l, r, c)
                    elif grid[l][r][c] == "E":
                        end = (l, r, c)

        dist = [[[-1] * cols for _ in range(rows)] for _ in range(levels)]
        dist[start[0]][start[1]][start[2]] = 0
        queue = deque([start])
        while queue:
            l, r, c = queue.popleft()
            for dl, dr, dc in MOVES:
                nl, nr, nc = l + dl, r + dr, c + dc
                if (0 <= nl < levels and 0 <= nr < rows and 0 <= nc < cols
                        and dist[nl][nr][nc] == -1 and grid[nl][nr][nc] != "#"):
                    dist[nl][nr][nc] = dist[l][r][c] + 1
                    queue.append((nl, nr, nc))

        escape_time = dist[end[0]][end[1]][end[2]]
        if escape_time == -1:
            output.append("Trapped!")
        else:
            output.append(f"Escaped in {escape_time} minute(s).")

    print("\n".join(output))


if __name__ == "__main__":
    main()
