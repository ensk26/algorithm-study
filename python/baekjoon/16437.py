# 양 구출 작전

import sys

sys.setrecursionlimit(10 ** 8)

input = sys.stdin.readline


def solution(cur):
    total = 0

    for next in graph[cur]:  # cur 노드의 자식 노드 탐색
        total += solution(next)  # 자식 노드 양 수 합

    if arr[cur][0] == 'W':  # 늑대
        total -= arr[cur][1]

    elif arr[cur][0] == 'S':  # 양
        total += arr[cur][1]

    return total if total > 0 else 0


def main():
    global arr, graph

    n = int(input())
    arr = [(), (0, 0), ]
    graph = [[] for _ in range(n + 1)]

    for i in range(2, n + 1):
        t, a, p = map(str, input().split())
        a, p = int(a), int(p)
        arr.append((t, a))
        graph[p].append(i)

    answer = solution(1)
    print(answer)


if __name__ == "__main__":
    main()
