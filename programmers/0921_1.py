#숫자 블록

import math

def find(i):
    if i == 1:
        return 0

    for j in range(2, int(math.sqrt(i)) + 1):
        if i % j == 0 and i // j <= 10000000:
            return i // j

    return 1


def solution(begin, end):
    answer = []
    for i in range(begin, end + 1):
        answer.append(find(i))

    return answer

def main():
    begin=1
    end=10
    print(solution(begin, end))

if __name__ == "__main__":
    main()