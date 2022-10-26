# 전기가 부족해

import sys

input = sys.stdin.readline


def find(n):
    global parent

    if parent[n] == n:
        return n
    else:
        return find(parent[n])


def solution(weight, power):
    global parent
    answer = 0

    for u, v, w in weight:
        # 부모가 같으면 고리가 생김으로 안됨
        # 각 부모가 둘다 power도 안됨
        # 한쪽 부모가 power면 같이 따라가기
        uf = find(u)
        vf = find(v)

        if uf in power and vf in power:
            continue
        if uf == vf:
            continue
        if uf in power:
            parent[vf] = uf
        elif vf in power:
            parent[uf] = vf
        else:
            parent[uf] = v

        answer += w

    return answer


def main():
    global parent
    n, m, k = map(int, input().split())
    power = list(map(int, input().split()))
    parent = [i for i in range(n + 1)]

    weight = [list(map(int, input().split())) for _ in range(m)]
    weight.sort(key=lambda x: x[2])

    print(solution(weight, power))


if __name__ == "__main__":
    main()
