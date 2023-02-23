# 단지번호붙이기
from collections import deque

q = deque()
drs = [0, 0, 1, -1]
dcs = [1, -1, 0, 0]


def in_range(r, c, n):
    return 0 <= r < n and 0 <= c < n


def solution(n, arr):
    cnt = 1

    while q:
        r, c = q.popleft()

        for dr, dc in zip(drs, dcs):
            nr, nc = dr + r, dc + c

            if in_range(nr, nc, n) and arr[nr][nc] == 1:
                arr[nr][nc] = 0
                cnt += 1
                q.append((nr, nc))

    return cnt


def main():
    answer = []
    n = int(input())
    arr = [list(map(int, input())) for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if arr[i][j] == 1:
                q.append((i, j))
                arr[i][j] = 0
                cnt = solution(n, arr)
                answer.append(cnt)

    answer.sort()
    print(len(answer))
    for ans in answer:
        print(ans)


if __name__ == "__main__":
    main()
