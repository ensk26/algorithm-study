# 1로 만들기

def solution(x):
    if x in dp:
        return dp[x]

    if x % 3 == 0 and x % 2 == 0:
        dp[x] = min(solution(x // 3) + 1, solution(x / 2) + 1)

    elif x % 3 == 0:
        dp[x] = min(solution(x // 3) + 1, solution(x - 1) + 1)

    elif x % 2 == 0:
        dp[x] = min(solution(x // 2) + 1, solution(x - 1) + 1)

    else:
        dp[x] = solution(x - 1) + 1

    return dp[x]


def main():
    global dp

    dp = {1: 0}
    x = int(input())

    solution(x)
    print(dp[x])


if __name__ == "__main__":
    main()
