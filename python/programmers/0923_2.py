#거리두기 확인하기

# o 빈테이블
# p 응시자가 앉아있는 자리
# x 파티션을 의미
# 상하좌우를 다 확인후 파티션이 없다면 확인하기
# 사람이 있으면 return 0
# 만약 테이블이면 테이블에서 상하좌우에 사람이 있는지 확인
# 이미 방문 한곳은 확인 안함
# 맨해튼 거리 2이하 인지 확인
from collections import deque

q = deque()

drs = [0, 0, 1, -1]
dcs = [1, -1, 0, 0]

visited = [
    [False for _ in range(5)]
    for _ in range(5)
]

def solution(places):
    answer = []

    def in_range(r, c):
        return r >= 0 and r < 5 and c >= 0 and c < 5

    def bfs(i,j):
        while q:
            r, c = q.popleft()

            for dr, dc in zip(drs, dcs):
                nr, nc = dr + r, dc + c
                d = abs(i-nr) + abs(j-nc) # 맨해튼 거리

                if in_range(nr, nc) and not visited[nr][nc]:  # 처음 방문

                    if p[nr][nc] == 'P' and d<=2:
                        return False

                    elif p[nr][nc] == 'O' and d==1:
                        visited[nr][nc] = True
                        q.append((nr, nc))

        return True

    def check(p, visited):
        for i in range(5):
            for j in range(5):
                if p[i][j] == 'P':
                    q.append((i, j))
                    visited[i][j] = True
                    if not bfs(i,j):
                        return 0
        return 1

    for p in places:

        answer.append(check(p, visited))

        for i in range(5):
            for j in range(5):
                visited[i][j] = False

    # print(places[1][1])
    return answer

def main():
    places=[["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
            ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
            ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]
    print(solution(places))

if __name__ == "__main__":
    main()