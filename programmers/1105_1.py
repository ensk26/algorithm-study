# 카펫
from math import sqrt


def solution(brown, yellow):
    answer = []
    for i in range(1, int(sqrt(yellow)) + 1):
        if yellow % i == 0:
            r, c = (yellow // i) + 2, i + 2
            if r * c == (yellow + brown):
                answer.append(r)
                answer.append(c)
                break

    return answer


def main():
    brown = 10
    yellow = 2
    print(solution(brown, yellow))


if __name__ == "__main__":
    main()
