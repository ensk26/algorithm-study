# 숫자 카드 나누기

def gcd(a, b):
    while b != 0:
        a, b = b, a % b

    return a


def isAnswer(arr, num):
    for a in arr:
        if a % num == 0:
            return False

    return True


def getGcd(arr):
    num = arr[0]

    for k in range(1, len(arr)):
        num = gcd(num, arr[k])
        if num == 0:
            return 0

    return num


def solution(arrayA, arrayB):
    a = getGcd(arrayA)
    b = getGcd(arrayB)

    if a == b:
        return 0
    if a > b:
        if not isAnswer(arrayB, a):
            return 0
        return a
    else:
        if not isAnswer(arrayA, b):
            return 0
        return b


def main():
    arrayA, arrayB = [14, 35, 119], [18, 30, 102]
    print(solution(arrayA, arrayB))


if __name__ == "__main__":
    main()
