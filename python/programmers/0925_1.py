#숫자의 표현

def solution(n):
    answer = 0
    total = 0
    start = 1
    for end in range(1, n + 1):
        total += end
        while total > n:
            total -= start
            start += 1

        if total == n:
            answer += 1

    return answer

def main():
    n=15
    print(solution(n))

if __name__ == "__main__":
    main()