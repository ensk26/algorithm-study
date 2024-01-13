# 01타일

def solution(n):
    if n < 4:
        return n

    arr = [0 for _ in range(n + 1)]

    arr[1] = 1
    arr[2] = 2
    for i in range(3, n + 1):
        arr[i] = (arr[i - 1] + arr[i - 2]) % 15746

    return arr[n]


def main():
    n = int(input())
    print(solution(n))


if __name__ == "__main__":
    main()
