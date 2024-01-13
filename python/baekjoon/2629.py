# 양팔저울

import sys

input = sys.stdin.readline


def dfs(cur, total):  # 추를 사용할때 나올수 있는 무게 구하는 재귀

    if gram[cur][total]:
        return

    gram[cur][total] = True

    if cur == n:
        return

    dfs(cur + 1, abs(total - arr[cur]))  # 무게를 확인하는 추에 둘 때
    dfs(cur + 1, total + arr[cur])  # 무게 재는 추에 둘 때
    dfs(cur + 1, total)  # 추를 안사용할때


def main():
    global arr, gram, n

    n = int(input())
    arr = list(map(int, input().split()))

    gram = [[False for _ in range(15001)] for _ in range(n + 1)]  # 비교할 수 있는 무게인지

    dfs(0, 0)

    k = int(input())

    answer = [
        'Y' if g < 15001 and gram[n][g] else 'N' for g in map(int, input().split())
    ]

    print(' '.join(answer))


if __name__ == "__main__":
    main()
