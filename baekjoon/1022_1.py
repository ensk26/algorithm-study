# 과자 나눠주기

def solution(n, m, arr):
    answer = 0
    left = 1
    right = 1000000000

    def check(mid):
        cnt = 0
        for i in arr:
            cnt += i // mid
        return cnt >= n

    while left <= right:
        mid = (left + right) // 2

        if check(mid):
            left = mid + 1
        else:
            right = mid - 1

    answer = left - 1
    return answer


def main():
    m, n = map(int, input().split())
    arr = list(map(int, input().split()))
    print(solution(m, n, arr))


if __name__ == "__main__":
    main()
