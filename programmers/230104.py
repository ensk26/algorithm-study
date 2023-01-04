# 유사 칸토어 비트열

# 0 부터 시작할때 2번째 자리가 0
# 00000 는 위쪽으로 올라가서 2번째 자리가 0인지 확인


def is2(n):
    while n >= 5:
        n //= 5

        if n % 5 == 2:
            return True

    return n == 2


def solution(n, l, r):
    cnt = r - l + 1

    for i in range(l, r + 1):
        if i % 5 == 3 or is2(i - 1):
            cnt -= 1

    return cnt


def main():
    n, l, r = 4, 30, 118
    print(solution(n, l, r))


if __name__ == "__main__":
    main()
