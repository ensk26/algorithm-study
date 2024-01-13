# 미세먼지 안녕!

# 공기청정기 바람이 불면서 미세먼지를 날림
# 공기 순환해 공기청정기로 오면 미세먼지 사라짐
# 미세먼지는 상하좌우로 퍼짐
# 한 빈칸에 여러 미세먼지 퍼진 합이 된수 있음
# 미세먼지/5의 값이 4방향으로 퍼지고 퍼진수에서 기존 수를 빼준다.
# 공기청정기 있는 칸은 이동 안함
# 끝에만 이동을 함
import sys

input = sys.stdin.readline


def solution(m, n, t, arr):
    answer = 0
    p1 = 0
    p2 = 0

    temp = [[0 for _ in range(n)] for _ in range(m)]

    # 공기 청정기가 있는 칸 탐색
    for i in range(2, m - 2):
        if arr[i][0] == -1:
            p1 = i
            p2 = i + 1
            break

    for time in range(t):  # 주어진 시간

        # 미세먼지 퍼짐
        for r in range(m):
            for c in range(n):

                if arr[r][c] > 0:
                    d = (arr[r][c] // 5)
                    pre = arr[r][c]

                    if r > 0 and arr[r - 1][c] != -1:
                        temp[r - 1][c] += d
                        pre -= d

                    if r < m - 1 and arr[r + 1][c] != -1:
                        temp[r + 1][c] += d
                        pre -= d

                    if c > 0 and arr[r][c - 1] != -1:
                        temp[r][c - 1] += d
                        pre -= d

                    if c < n - 1 and arr[r][c + 1] != -1:
                        temp[r][c + 1] += d
                        pre -= d

                    arr[r][c] = pre

        for i in range(m):
            for j in range(n):
                arr[i][j] += temp[i][j]

        # 공기 청정기
        for i in range(p1 - 1, 0, -1):  # 상 좌
            arr[i][0] = arr[i - 1][0]

        for i in range(p2 + 1, m - 1):  # 하 좌
            arr[i][0] = arr[i + 1][0]

        for i in range(n - 1):  # 상 하
            arr[0][i] = arr[0][i + 1]
            arr[m - 1][i] = arr[m - 1][i + 1]

        for i in range(p1):  # 상 우
            arr[i][n - 1] = arr[i + 1][n - 1]

        for i in range(m - 1, p2, -1):  # 하 우
            arr[i][n - 1] = arr[i - 1][n - 1]

        for i in range(n - 1, 0, -1):  # p1,p2
            arr[p1][i] = arr[p1][i - 1]
            arr[p2][i] = arr[p2][i - 1]

        arr[p1][1] = 0
        arr[p2][1] = 0

        if time < t - 1:
            for i in range(m):  # 초기화
                for j in range(n):
                    temp[i][j] = 0

    for i in range(m):
        for j in range(n):
            answer += arr[i][j]

    answer += 2  # 공기 청정기

    return answer


def main():
    r, c, t = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(r)]
    print(solution(r, c, t, arr))


if __name__ == "__main__":
    main()
