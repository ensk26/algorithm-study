# 마법의 엘리베이터

def dfs(n, cnt):
    global answer
    if n < 10:
        answer = min(answer, cnt + n % 10, cnt + (10 - n % 10) + 1)
        return

    dfs(n // 10, cnt + n % 10)  # 더하기
    dfs(n // 10 + 1, cnt + (10 - n % 10))  # 빼기


def solution(storey):
    global answer
    answer = storey
    dfs(storey, 0)

    return answer


def main():
    storey = 2554
    print(solution(storey))


if __name__ == "__main__":
    main()
