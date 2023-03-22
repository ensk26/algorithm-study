# 퍼레이드

import sys

sys.setrecursionlimit(1000 * 5)
input = sys.stdin.readline


def solution(cur):
    global cnt

    for next in graph[cur]:
        if not visited[next]:
            visited[next] = True
            cnt += 1
            solution(next)

    return


def main():
    global visited, graph, cnt, v
    cnt = 0
    v, e = map(int, input().split())
    visited = [False for _ in range(v + 1)]
    graph = [[] for _ in range(v + 1)]

    for _ in range(e):
        v1, v2 = map(int, input().split())
        graph[v1].append(v2)
        graph[v2].append(v1)

    odd = 0  # 정점의 간선이 홀수가 0개, 2개 일때 오일러 서킷, 트레일 존재
    for g in graph:
        if len(g) % 2 != 0:
            odd += 1

    if odd == 0 or odd == 2:
        solution(1)  # 그래프가 전부 연결되있는지 확인

        print("YES" if cnt == v else "NO")
    else:
        print("NO")


if __name__ == "__main__":
    main()
