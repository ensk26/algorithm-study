#소수 찾기

import math

def is_prime(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False

    return n > 1    #소수는 2이상부터이다.

def solution(numbers):
    answer = 0
    num = set([])
    temp = []
    visited = [False for _ in range(len(numbers))]

    def dfs(cur):
        if cur == len(numbers) + 1:
            return

        if cur > 0:
            num.add(int(''.join(temp)))

        for i in range(len(numbers)):
            if not visited[i]:
                visited[i] = True
                temp.append(numbers[i])
                dfs(cur + 1)
                temp.pop()
                visited[i] = False

    dfs(0)
    for n in num:
        if is_prime(n):
            answer += 1

    return answer

def main():
    numbers = 	"17"
    print(solution(numbers))

if __name__ == "__main__":
    main()