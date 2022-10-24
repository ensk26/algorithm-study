# 점프 게임

# 한칸씩 사라지는 조건은, 해당 index의 값과 해당 칸에 도착한 거리(d)를 비교해서
# 거리값이 index 값보다 크면 index가 사라지고 나서 도착하니까, c+1>=d의 조건 걸어 가지치기 한다.

from collections import deque
import sys

input = sys.stdin.readline  # 뒤에 '\n' 개행문자 제거 해야함 (strip)

q = deque()


def solution(n, k, arr):
    visited = [[False for _ in range(n)] for _ in range(2)]  # 방문 유무
    q.append((0, 0, 1))

    while q:
        r, c, d = q.popleft()

        if c + 1 >= n or c + k >= n:  # 범위가 넘었을때
            return 1

        if not visited[(r + 1) % 2][c + k] and arr[(r + 1) % 2][c + k] == 1 and c + k >= d:
            visited[(r + 1) % 2][c + k] = True
            q.append(((r + 1) % 2, c + k, d + 1))

        if not visited[r][c + 1] and arr[r][c + 1] == 1 and c + 1 >= d:
            visited[r][c + 1] = True
            q.append((r, c + 1, d + 1))

        if not visited[r][c - 1] and arr[r][c - 1] == 1 and c - 1 >= d:
            visited[r][c - 1] = True
            q.append((r, c - 1, d + 1))

    return 0


def main():
    n, k = map(int, input().split())
    arr = [list(map(int, input().strip())) for _ in range(2)]
    print(solution(n, k, arr))


if __name__ == "__main__":
    main()
