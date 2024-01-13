# 경쟁적 전염

from collections import deque

q = deque()
drs = [0, 0, 1, -1]
dcs = [1, -1, 0, 0]


def in_range(r, c):
    global n
    return 0 <= r < n and 0 <= c < n


def solution(arr, s, x, y):
    while q:
        r, c, v, t = q.popleft()
        if t == s:  # 시간이 다 됨
            break
        for dr, dc in zip(drs, dcs):
            nr, nc = dr + r, dc + c
            if in_range(nr, nc) and arr[nr][nc] == 0:
                arr[nr][nc] = v
                q.append((nr, nc, v, t + 1))

    return arr[x - 1][y - 1]


def main():
    global n
    n, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    s, x, y = map(int, input().split())
    temp = []
    for i in range(n):
        for j in range(n):
            if arr[i][j] != 0:
                temp.append((i, j, arr[i][j], 0))

    temp.sort(key=lambda x: x[2])
    for t in temp:
        q.append(t)

    print(solution(arr, s, x, y))


if __name__ == "__main__":
    main()
