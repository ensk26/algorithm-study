# 개업

def solution(n, m):
    dp = [-1 for _ in range(n + 1)]  # index: 짜장면 수, 값: 요리 횟수

    # 초기값
    for i in range(m):  # 윅을 한개 사용
        dp[arr[i]] = 1
        for j in range(i + 1, m):  # 윅을 두개 사용
            if arr[i] + arr[j] <= n:  # n이하 짜장면 수
                dp[arr[i] + arr[j]] = 1

    for i in range(1, n + 1):
        for j in range(1, i // 2 + 1):
            if dp[j] == -1 or dp[i - j] == -1:  # 가능한 값이 없다.
                continue

            if dp[i] == -1 or dp[i] > dp[j] + dp[i - j]:  # 최솟값
                dp[i] = dp[j] + dp[i - j]

    return dp[n]


def main():
    global arr
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))

    print(solution(n, m))


if __name__ == "__main__":
    main()
