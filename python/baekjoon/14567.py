# 선수과목 (Prerequisite)

import sys

input = sys.stdin.readline


def main():
    n, m = map(int, input().split())

    graph = [[] for _ in range(n)]
    dp = [1 for _ in range(n)]

    for _ in range(m):
        u, v = map(int, input().split())
        graph[v - 1].append(u - 1)  # 선수 과목만 연결 (단방향)

    for cur in range(n):
        for pre in graph[cur]:
            dp[cur] = max(dp[cur], dp[pre] + 1)

    print(' '.join(map(str, dp)))


if __name__ == "__main__":
    main()
