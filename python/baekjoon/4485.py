# 녹색 옷 입은 애가 젤다지?

# X 지점에서 하 방향으로 올라오는 경로가 있다면
# 0 2 3
# 1 X 3
# 0 0 4
# 일때 (0,0)에서 X 지점 까지  (0,0) -> (0,1)로 가는것이 최소다.
# 만약 (0,0)->(0,1)->(0,2)->(1,2) 로 돌아간다면 보이는것과 같이, 돌아가는 길이 전부 0이라도 제일 먼저 나온 경우가 최소값과 같다.
# 그러므로 이미 방문한 칸은 다시 방문해서 확인할 필요가 없다.

# 다익스트라 방식


from heapq import heappush, heappop

drs = [-1, 1, 0, 0]
dcs = [0, 0, -1, 1]


def inRange(r, c):
    return 0 <= r < n and 0 <= c < n


def solution():
    heap = []
    visited = [[False for _ in range(n)] for _ in range(n)]  # 해당 구간을 방문 했는지

    heappush(heap, (arr[0][0], 0, 0))
    visited[0][0] = True

    while heap:
        money, r, c = heappop(heap)

        if r == n - 1 and c == n - 1:
            return money

        for dr, dc in zip(drs, dcs):
            nr, nc = r + dr, c + dc
            if inRange(nr, nc) and not visited[nr][nc]:
                heappush(heap, (arr[nr][nc] + money, nr, nc))
                visited[nr][nc] = True


def main():
    global arr, n
    cnt = 0

    while True:
        n = int(input())
        if n == 0:
            return

        arr = [list(map(int, input().split())) for _ in range(n)]

        cnt += 1
        answer = solution()

        print("Problem %s: %s" % (cnt, answer))


if __name__ == "__main__":
    main()
