# 작업

import sys

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

answer = 0


def solution(n, m, arr, x):
    graph = [[] for _ in range(n + 1)]
    visited = [False for _ in range(n + 1)]

    # print(arr)
    for a, b in arr:
        graph[b].append(a)

    def dfs(cur):
        global answer

        if not graph[cur]:
            return

        for i in graph[cur]:
            if not visited[i]:
                visited[i] = True
                dfs(i)
                answer += 1

    dfs(x)

    return answer


def main():
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(m)]
    x = int(input())
    print(solution(n, m, arr, x))


if __name__ == "__main__":
    main()
