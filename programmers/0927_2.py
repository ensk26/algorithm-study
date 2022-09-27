#방문 길이

#처음 걸어본 길의 길이를 구하는 문제

drs = [-1, 1, 0, 0]
dcs = [0, 0, 1, -1]
dic = {'U': 0, 'D': 1, 'R': 2, 'L': 3}
reverse = {0: 1, 1: 0, 2: 3, 3: 2}
visited = [
    [[False, False, False, False] for _ in range(12)]
    for _ in range(12)
]

def in_range(r, c):
    return r >= -5 and r <= 5 and c >= -5 and c <= 5

def solution(dirs):
    answer = 0
    cnt = 0
    r, c = 0, 0

    for key in dirs:
        d = dic[key]
        nr, nc = r + drs[d], c + dcs[d]

        if not in_range(nr, nc):  # 격자 범위를 넘으면
            continue

        if not visited[nr + 6][nc + 6][d]:  # 현재 온 길을 이전에 방문 했는지
            visited[nr + 6][nc + 6][d] = True  # 현재 -> 다음
            visited[r + 6][c + 6][reverse[d]] = True  # 다음 -> 현재
            cnt += 1

        r, c = nr, nc

    answer = cnt
    return answer

#중복되는 좌표만 지우면 되니까 set 자료형으로도 풀 수 있다.

point = set([])

def solution2(dirs):
    answer = 0
    r, c = 0, 0

    for key in dirs:
        d = dic[key]
        nr, nc = r + drs[d], c + dcs[d]

        if not in_range(nr, nc):  # 격자 범위를 넘으면
            continue

        point.add((nr, nc, r, c))  # 현재 -> 다음
        point.add((r, c, nr, nc))  # 다음 -> 현재

        r, c = nr, nc

    answer = len(point) // 2
    return answer

def main():
    dirs = "ULURRDLLU"
    print(solution(dirs))
    print(solution2(dirs))

if __name__ == "__main__":
    main()