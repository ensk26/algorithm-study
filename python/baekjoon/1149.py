# RGB거리

def solution(n, arr):
    dp = [[0 for _ in range(3)] for _ in range(n)]

    for i in range(3):
        dp[0][i] = arr[0][i]

    for i in range(1, n):
        dp[i][0] = min(dp[i - 1][1] + arr[i][0], dp[i - 1][2] + arr[i][0])
        dp[i][1] = min(dp[i - 1][0] + arr[i][1], dp[i - 1][2] + arr[i][1])
        dp[i][2] = min(dp[i - 1][0] + arr[i][2], dp[i - 1][1] + arr[i][2])

    return min(dp[n - 1][0], dp[n - 1][1], dp[n - 1][2])


def main():
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    print(solution(n, arr))


if __name__ == "__main__":
    main()
