# 최고의 집합

def solution(n, s):
    answer = []
    if n > s:
        return [-1]
    for i in range(n, 1, -1):
        answer.append(s // i)
        s -= s // i

    answer.append(s)
    return answer


def main():
    n, s = 3, 8
    print(solution(n, s))


if __name__ == "__main__":
    main()
