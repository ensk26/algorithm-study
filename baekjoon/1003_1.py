# 인구 이동

# 국경을 공유 할때 인구차이가 l 명 이상, r 이하
# 인구 이동, 총 인구수/ 칸 개수, 소수점 버림

from collections import deque
from sys import stdin

input = stdin.readline

q = deque()
pos = deque()
rote = deque()

drs = [0, 0, 1, -1]
dcs = [1, -1, 0, 0]


def solution(n, L, R, people):
    global total
    answer = 0
    total = 0

    visited = [  # 방문 유무
        [-1 for _ in range(n)]
        for _ in range(n)
    ]

    def in_range(r, c):
        return r >= 0 and r < n and c >= 0 and c < n

    def bfs():  # 특정지점에서 만족하는 칸이 있는지
        global total

        while q:
            r, c = q.popleft()

            for dr, dc in zip(drs, dcs):
                nr, nc = dr + r, dc + c
                if in_range(nr, nc) and visited[nr][nc] != cnt:
                    diff = abs(people[nr][nc] - people[r][c])  # 인구 차

                    if diff >= L and diff <= R:
                        visited[nr][nc] = cnt
                        q.append((nr, nc))
                        pos.append((nr, nc))  # 위치값 저장
                        total += people[nr][nc]  # 전체 값

    for i in range(n):
        for j in range(n):
            rote.append((i, j))

    cnt = 0

    while True:
        move = False  # 인구 이동이 유무

        for _ in range(len(rote)):
            i, j = rote.popleft()
            if visited[i][j] != cnt:  # 그룹이 있는가
                q.append((i, j))
                visited[i][j] = cnt
                total = people[i][j]

                bfs()

                total //= (len(pos) + 1)  # 인구수 평균값

                if pos:  # 인구 이동이 있을때
                    people[i][j] = total
                    rote.append((i, j))

                while pos:  # 해당 칸 값 바꾸기
                    r, c = pos.popleft()
                    people[r][c] = total
                    rote.append((r, c))

        if rote:  # 인구 이동이 있다.
            cnt += 1
        else:  # 인구 이동이 없다.
            break

    answer = cnt

    return answer


def main():
    n, L, R = map(int, input().split())
    people = [list(map(int, input().split())) for _ in range(n)]
    print(solution(n, L, R, people))


if __name__ == "__main__":
    main()
