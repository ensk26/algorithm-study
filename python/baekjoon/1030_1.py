# 아기 상어 2
from collections import deque

q = deque()
drs = [0, 0, 1, -1, -1, -1, 1, 1]
dcs = [1, -1, 0, 0, -1, 1, -1, 1]


def solution(n, m, arr):
    answer = 0
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 1:
                q.append((i, j))

    while q:
        r, c = q.popleft()
        for dr, dc in zip(drs, dcs):
            nr, nc = dr + r, dc + c
            if 0 <= nr < n and 0 <= nc < m and arr[nr][nc] == 0:
                arr[nr][nc] = max(arr[nr][nc], arr[r][c] + 1)
                q.append((nr, nc))

    for a in arr:
        answer = max(answer, max(a))

    return answer - 1


def main():
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    print(solution(n, m, arr))


if __name__ == "__main__":
    main()
