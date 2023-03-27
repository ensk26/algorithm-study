# 입국심사

# 최소 시간 기준이 아닌 총 시간 기준으로 탐색
# 최소 시간은 사람마다 탐색을 해야한다.
# 최소 힙을 사용해도 결국 사람마다 연산이 이루어짐으로 시간초과가 발생한다.
# 총 시간 기준은 이분탐색으로 구하고, 구한 시간에 주어진 사람(m)만큼 처리가 가능한지 확인함으로 연산이 더 적음으로 해결할 수 있다.

import sys

input = sys.stdin.readline

arr = []


def isAvailable(time, m):
    cnt = 0

    for n in arr:
        cnt += time // n

    return cnt >= m


def solution(maxTime, m):
    left = 0
    right = maxTime

    while left <= right:
        mid = (left + right) // 2

        if isAvailable(mid, m):
            right = mid - 1
        else:
            left = mid + 1

    return right + 1


def main():
    n, m = map(int, input().split())

    for _ in range(n):
        arr.append(int(input()))

    maxTime = max(arr) * m
    print(solution(maxTime, m))


if __name__ == "__main__":
    main()
