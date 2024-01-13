# 차이를 최대로


def solution(n, arr):
    global answer
    temp = []
    visited = [False for _ in range(n)]
    answer = 0

    def dfs(cur):
        global answer

        if cur == n:
            ans = 0
            for t in range(n - 1):
                ans += abs(temp[t] - temp[t + 1])
            answer = max(answer, ans)
            return

        for i in range(n):
            if not visited[i]:
                temp.append(arr[i])
                visited[i] = True
                dfs(cur + 1)
                visited[i] = False
                temp.pop()

    dfs(0)

    return answer


def main():
    n = int(input())
    arr = list(map(int, input().split()))
    print(solution(n, arr))


if __name__ == "__main__":
    main()
