# 수


def getNum(cur, num):  # 숫자를 하나만 사용해서 조합을 만들어야 함

    if k == cur:
        number.append(int(''.join(num)))
        return

    for i in range(10):
        if not (cur == 0 and i == 0) and not visited[i]:
            visited[i] = True
            num.append(str(i))
            getNum(cur + 1, num)
            num.pop()
            visited[i] = False


def isAddPrime(n):  # n이 나올수 있는 소수의 합이 있는지
    for i in range(2, n // 2 + 1):
        if i != n - i and prime[i] and prime[n - i]:  # 같은 수는 안됨, 소수 합인지
            return True
    return False


def isDivPrime(m, n):  # n이 나올수 있는 소수의 곱이 있는지
    while n % m == 0:  # m으로 나눌수 있을때까지 나누기
        n //= m

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0 and prime[i] and prime[n // i]:  # 나눌수 있는 수인가, 소수 곱인지
            return True
    return False


def main():
    global prime, k, visited, number

    k, m = map(int, input().split())

    maxNum = pow(10, k)  # k 자리수 최대값

    prime = [True for _ in range(maxNum)]
    visited = [False for _ in range(10)]
    number = []
    answer = 0

    prime[0] = False
    prime[1] = False
    for i in range(2, int(maxNum ** 0.5) + 1):  # maxNum 까지의 소수를 구한다.
        if prime[i]:
            for j in range(i * i, maxNum, i):  # 배수는 소수가 아님
                prime[j] = False

    getNum(0, [])

    for i in number:
        if isAddPrime(i) and isDivPrime(m, i):
            answer += 1

    print(answer)


if __name__ == "__main__":
    main()
