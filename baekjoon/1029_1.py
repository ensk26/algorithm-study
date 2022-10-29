# 수들의 합 4

def solution(k, arr):
    dic = {0: 1}
    total = 0
    cnt = 0

    for a in arr:
        total += a
        if total - k in dic:
            cnt += dic[total - k]

        if total in dic:
            dic[total] += 1
        else:
            dic[total] = 1

    return cnt


def main():
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    print(solution(k, arr))


if __name__ == "__main__":
    main()
