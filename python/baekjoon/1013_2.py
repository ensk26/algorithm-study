# 유성

def solution(r, s, arr):
    answer = ''
    diff = r
    star = -1
    isStar = False

    temp = [['.' for _ in range(s)] for _ in range(r)]

    for j in range(s):
        for i in range(r):
            if arr[i][j] == 'X':
                star = i
                isStar = True  # 해당 줄에 별이 있는지

            elif isStar and arr[i][j] == '#':
                diff = min(diff, i - star - 1)  # 땅과 유성의 차이
                isStar = False
                break

    for j in range(s - 1, -1, -1):
        for i in range(r - 1, -1, -1):
            if arr[i][j] == 'X':
                arr[i + diff][j] = 'X'
                arr[i][j] = '.'

    for a in arr:
        answer += ''.join(a) + '\n'

    return answer


def main():
    r, s = map(int, input().split())
    arr = [list(map(str, input())) for _ in range(r)]
    print(solution(r, s, arr))


if __name__ == "__main__":
    main()
