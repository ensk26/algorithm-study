# DFS와 BFS

from collections import deque


def dfs(cur, arr):
    answer.append(cur)

    for next in arr[cur]:
        if not visited[next]:
            visited[next] = True
            dfs(next, arr)


def bfs(v, arr):
    q = deque()
    visited[v] = True
    q.append(v)

    while q:
        cur = q.popleft()
        answer.append(cur)

        for next in arr[cur]:
            if not visited[next]:
                visited[next] = True
                q.append(next)

    return answer


def main():
    global visited, answer

    n, m, v = map(int, input().split())
    arr = [[] for _ in range(n + 1)]
    visited = [0 for _ in range(n + 1)]
    answer = []

    for _ in range(m):
        a, b = map(int, input().split())
        arr[a].append(b)
        arr[b].append(a)

    for i in range(1, n + 1):
        arr[i].sort()

    visited[v] = True
    dfs(v, arr)
    print(' '.join(map(str, answer)))

    for i in range(n + 1):
        visited[i] = False

    answer = []
    print(' '.join(map(str, bfs(v, arr))))


if __name__ == "__main__":
    main()
