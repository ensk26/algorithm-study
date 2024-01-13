# 불

import sys
from collections import deque

input = sys.stdin.readline

q = deque()

drs = [0, 0, 1, -1]
dcs = [1, -1, 0, 0]


def solution(w, h, arr):
    fire = []

    for i in range(h):
        for j in range(w):
            if arr[i][j] == '*':
                fire.append((i, j, 0))
            elif arr[i][j] == '@':
                q.append((i, j, 0))

    for f in fire:
        q.append(f)

    while q:
        r, c, d = q.popleft()

        for dr, dc in zip(drs, dcs):
            nr, nc = dr + r, dc + c
            if ((0 > nr or nr >= h) or (0 > nc or nc >= w)) and arr[r][c] == '@':
                return d + 1

            if 0 <= nr < h and 0 <= nc < w and arr[nr][nc] != '#' and arr[nr][nc] != '*':  # 범위 안
                if arr[nr][nc] != arr[r][c]:  # 이미 방문한걸 다시 볼 필요 없다
                    arr[nr][nc] = arr[r][c]
                    q.append((nr, nc, d + 1))

    return "IMPOSSIBLE"


def main():
    t = int(input())
    for _ in range(t):
        w, h = map(int, input().split())
        arr = [list(map(str, input())) for _ in range(h)]
        print(solution(w, h, arr))
        q.clear()


if __name__ == "__main__":
    main()
