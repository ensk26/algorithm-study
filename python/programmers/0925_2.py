#삼각 달팽이

drs = [1, 0, -1]
dcs = [0, 1, -1]


def solution(n):
    answer = []
    arr = [
        [0 for _ in range(n)]
        for _ in range(n)
    ]
    r = 0
    c = 0
    cnt = n
    i = 1
    k = 0
    d = 0
    while True:

        arr[r][c] = i
        i += 1
        k += 1

        if k == cnt:
            cnt -= 1
            k = 0
            d = (d + 1) % 3

        if cnt == 0:
            break

        r, c = r + drs[d], c + dcs[d]

    for i in range(n):
        for j in range(n):
            if arr[i][j] != 0:
                answer.append(arr[i][j])

    return answer

def main():
    n=7
    print(solution(n))

if __name__ == "__main__":
    main()