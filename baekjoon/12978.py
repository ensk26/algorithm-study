# 스크루지 민호 2
import sys

sys.setrecursionlimit(10 ** 8)

input = sys.stdin.readline


def dfs(cur):
    for next in graph[cur]:
        if not visited[next]:
            visited[next] = True
            dfs(next)
            dp[0][cur] += min(dp[0][next], dp[1][next])  # 현재 노드 경찰서 설치할 경우, 다음 노드 경찰서 있어도 없어도 됨
            dp[1][cur] += dp[0][next]  # 현재 노드 경찰서 없는 경우, 다음 노드 경찰서 있어야 함

    dp[0][cur] += 1  # 현재 노드 경찰서 설치


def main():
    global graph, visited, dp

    n = int(input())
    graph = [[] for _ in range(n + 1)]
    visited = [False for _ in range(n + 1)]
    dp = [[0 for _ in range(n + 1)] for _ in range(2)]  # dp[0]: 경찰서 설치, dp[1]: 경찰서 없음

    for _ in range(n - 1):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    start = 1
    visited[start] = True
    dfs(start)

    print(min(dp[0][1], dp[1][1]))


if __name__ == "__main__":
    main()
