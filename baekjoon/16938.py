# 캠프 준비

import sys

input = sys.stdin.readline
answer = 0


def solution(cur, cnt, total, low, top):
    global answer

    if cur == n:
        if l <= total <= r and cnt > 1 and top - low >= x:  # 총 난이도 합, 두 문제 이상, 가장 어려운, 쉬운 난이도 차이
            answer += 1
        return

    solution(cur + 1, cnt + 1, total + arr[cur], min(low, arr[cur]), max(top, arr[cur]))
    solution(cur + 1, cnt, total, low, top)  # 안넣는 문제


def main():
    global n, l, r, x, arr

    n, l, r, x = map(int, input().split())
    arr = list(map(int, input().split()))

    solution(0, 0, 0, 1000000000, 0)
    print(answer)


if __name__ == "__main__":
    main()
