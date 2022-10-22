# 로또
import sys

input = sys.stdin.readline


def solution(n, m):
    arr = [[0 for _ in range(n)] for _ in range(m + 1)]
    answer = 0

    for i in range(1, m + 1):
        arr[i][0] = 1

    for i in range(1, n):
        for j in range(pow(2, i), m + 1):
            if j % 2 == 0:
                arr[j][i] = arr[j // 2][i - 1] + arr[j - 1][i]  # 이전 2의 배수, 이전 값 (1,2)->(2,4) (2,3)->(2,4)
            else:
                arr[j][i] = arr[j - 1][i]  # 이전값

    for i in range(1, m + 1):
        answer += arr[i][n - 1]
    return answer


def main():
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        print(solution(n, m))


if __name__ == "__main__":
    main()
