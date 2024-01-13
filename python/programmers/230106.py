# 콜라 문제

def solution(a, b, n):
    answer = 0
    while a <= n:
        cnt = n // a
        answer += cnt * b
        n = n - cnt * a + cnt * b
    return answer


def main():
    a, b, n = 3, 1, 20
    print(solution(a, b, n))


if __name__ == "__main__":
    main()
