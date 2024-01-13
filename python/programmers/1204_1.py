# 2개 이하로 다른 비트

# 각 끝 2(1),4(3),8(7), 앞에 비트 1->0, 0->1
# 나머지 0->1
# 1100, 0111 xor
# 111,1011
# 101,110

def getNum(n):
    binNum = format(n, 'b')

    if n > 0 and n & (n + 1) == 0:
        result = '10' + binNum[1:]
        return int(result, 2)

    if n % 2 == 1:
        for i in range(len(binNum) - 1, 0, -1):
            if binNum[i] == '0':
                result = binNum[:i] + '10' + binNum[i + 2:]
                return int(result, 2)

    return n + 1


def solution(numbers):
    answer = []
    for n in numbers:
        answer.append(getNum(n))

    return answer


def main():
    numbers = [i for i in range(10, 20)]
    print(solution(numbers))


if __name__ == "__main__":
    main()
