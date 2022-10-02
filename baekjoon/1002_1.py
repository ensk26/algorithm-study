# 마법사 상어와 비바라기

# (N, 1), (N, 2), (N-1, 1), (N-1, 2)에 비구름
# 대각선 방향으로 거리가 1인 칸에 물이 있는 바구니의 수만큼 (r, c)에 있는 바구니의 물이 양이 증가
# 경계를 넘어가는 칸은 대각선 방향으로 거리가 1인 칸이 아니다.
# 바구니에 저장된 물의 양이 2 이상인 모든 칸에 구름이 생기고, 물의 양이 2 줄어든다
# 이때 구름이 생기는 칸은 구름이 사라진 칸이 아니어야 한다
# 1부터 순서대로 ←, ↖, ↑, ↗, →, ↘, ↓, ↙
# 구름 방문 유무
# 대각선 위치
# 구름 이동 방향
# 범위 지정
from collections import deque

cloud = [(0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]  # 구름 이동 방향
cross = [(-1, -1), (-1, 1), (1, 1), (1, -1)]  # 대각선

q = deque()  # 비 구름 위치
nq = deque()  # 물 복사 위치


def solution(n, m, arr, move):
    answer = 0
    col = len(arr[0])  # 가로 길이
    position = [
        [False for _ in range(col)]
        for _ in range(n)
    ]  # 현재 구름이 있는지

    def in_range(r, c):  # 범위 내에 있는지 확인
        return r >= 0 and r < n and c >= 0 and c < col

    # 초기 구름 위치
    q.append((n - 1, 0))
    q.append((n - 1, 1))
    q.append((n - 2, 0))
    q.append((n - 2, 1))

    for d, s in move:  # 비 구름
        while q:  # 구름 이동
            r, c = q.popleft()
            r += cloud[d - 1][0] * s
            c += cloud[d - 1][1] * s

            r, c = (r % n), (c % col)

            # 현재 위치에서 비내려주고,
            arr[r][c] += 1
            position[r][c] = True  # 구름이 있었다 체크
            nq.append((r, c))

        while nq:  # 물 복사
            r, c = nq.popleft()

            # 각 대각선의 구름이 있을때 유무와 구름이 있는 칸 수 더해주기
            for dr, dc in cross:
                nr, nc = dr + r, dc + c
                if in_range(nr, nc) and arr[nr][nc] > 0:  # 구름이 있어
                    arr[r][c] += 1

        # 2이상인 모든 칸에 비구름 생성, 생기고 2를 빼준다.
        for i in range(n):
            for j in range(col):
                if arr[i][j] >= 2 and not position[i][j]:
                    arr[i][j] -= 2
                    q.append((i, j))  # 비구름 위치

                elif position[i][j]:
                    position[i][j] = False  # 이전 비구름 위치 해제

    # 전체 for문으로 계산
    for i in range(n):
        for j in range(col):
            answer += arr[i][j]

    return answer


def main():
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    move = [list(map(int, input().split())) for _ in range(m)]
    print(solution(n, m, arr, move))


if __name__ == "__main__":
    main()
