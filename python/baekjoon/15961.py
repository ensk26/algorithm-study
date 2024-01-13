# 회전 초밥

import sys

input = sys.stdin.readline


def solution(n, k, arr):
    answer = 0
    kindCnt = 1  # 쿠폰 초밥
    cnt = 0
    left = 0

    for right in range(n + k):

        if kind[arr[right % n]] == 0:
            kindCnt += 1

        cnt += 1
        kind[arr[right % n]] += 1

        if cnt == k:
            answer = max(answer, kindCnt)
            if k + 1 == answer:  # 최대 가지수
                break

            kind[arr[left % n]] -= 1

            if kind[arr[left % n]] == 0:
                kindCnt -= 1
            left += 1
            cnt -= 1

    return answer


def main():
    global arr, kind
    n, d, k, c = map(int, input().split())
    arr = [0 for _ in range(n)]
    kind = [0 for _ in range(3000001)]
    kind[c] = 1  # 쿠폰 초밥

    for i in range(n):
        arr[i] = int(input())

    print(solution(n, k, arr))


if __name__ == "__main__":
    main()
