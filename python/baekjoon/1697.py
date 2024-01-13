# 숨바꼭질

from collections import deque

q = deque()
visited = [0 for _ in range(100001)]


def isValid(x):
    return 0 <= x <= 100000 and not visited[x]


def solution(n, k):
    q.append(n)
    visited[n] = 1

    while q:
        cur = q.popleft();

        if cur == k:
            return visited[cur] - 1

        for next in (cur + 1, cur - 1, cur * 2):

            if isValid(next):
                q.append(next)
                visited[next] = visited[cur] + 1


def main():
    n, k = map(int, input().split())
    print(solution(n, k))


if __name__ == "__main__":
    main()
