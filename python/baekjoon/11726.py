# 2×n 타일링

def solution(n):
    dp = [0 for _ in range(n + 1)]

    dp[1] = 1
    dp[2] = 2
    for i in range(3, n + 1):
        dp[i] = (dp[i - 1] + dp[i - 2]) % 10007

    return dp[n]


def main():
    n = int(input())
    print(solution(n) if n > 1 else 1)


if __name__ == "__main__":
    main()
