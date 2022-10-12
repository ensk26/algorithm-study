# 벽 부수고 이동하기

from collections import deque

q = deque()
drs = [0, 0, 1, -1]
dcs = [1, -1, 0, 0]


def solution(n, m, arr):
    visited = [[[2000001, 2000001] for _ in range(m)] for _ in range(n)]  # 벽을 부술때, 안부술때

    # 초기값
    q.append((0, 0, True))  # 위치값, 벽 부술수 있다.
    visited[0][0][1] = 1  # 길 거리
    while q:
        r, c, b = q.popleft()

        if b:  # 벽 아직 안부숨
            d = visited[r][c][1] + 1  # 거리
        else:
            d = visited[r][c][0] + 1

        for dr, dc in zip(drs, dcs):
            nr, nc = dr + r, dc + c

            if nr < 0 or nr >= n or nc < 0 or nc >= m:  # 범위
                continue

            # 해당 위치 벽, 벽 부술수 있음, 해당 위치 벽이 있는 거리보다 작은지 확인:
            if arr[nr][nc] == 1 and b and visited[nr][nc][0] > d:
                visited[nr][nc][0] = d
                q.append((nr, nc, False))

            # 해당 위치 길, 벽을 부술수 있으면, 1번, 없으면 0번 에 위치값 저장, 해당 거리보다 작은지 확인:
            if arr[nr][nc] == 0:
                if b and visited[nr][nc][1] > d:  # 벽 아직 안부숨
                    visited[nr][nc][1] = d
                    q.append((nr, nc, b))

                elif not b and visited[nr][nc][0] > d:  # 벽 이미 부숨
                    visited[nr][nc][0] = d
                    q.append((nr, nc, b))

    if visited[n - 1][m - 1][0] == 2000001 and visited[n - 1][m - 1][1] == 2000001:
        return -1
    else:
        return min(visited[n - 1][m - 1][0], visited[n - 1][m - 1][1])


def main():
    n, m = map(int, input().split())
    arr = [list(map(int, input())) for _ in range(n)]
    print(solution(n, m, arr))


if __name__ == "__main__":
    main()
