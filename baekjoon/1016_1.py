# 수열과 헌팅

# 각 범위 값을 다 확인해보기, bisect 이진 탐색 가능

import sys

input = sys.stdin.readline

low = []
up = []


def solution(n, arr):
    answer = [[] for _ in range(n)]

    for a, b in arr:
        low.append(a - b)
        up.append(a + b)

    l = sorted(low)
    u = sorted(up)

    for i in range(n):
        # 최소
        left = 0
        right = n - 1
        while left <= right:
            mid = (left + right) // 2

            if u[mid] >= low[i]:  # 만족하면
                right = mid - 1
            else:
                left = mid + 1

        answer[i].append(left + 1)

        # 최대
        left = 0
        right = n - 1
        while left <= right:
            mid = (left + right) // 2

            if l[mid] <= up[i]:  # 만족하면
                left = mid + 1
            else:
                right = mid - 1

        answer[i].append(right + 1)

    for a in answer:
        print(' '.join(map(str, a)))


def main():
    n = int(input())
    arr = [list(map(int, input().split())) for i in range(n)]
    solution(n, arr)


if __name__ == "__main__":
    main()
