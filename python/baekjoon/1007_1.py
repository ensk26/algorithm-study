# 기차가 어둠을 헤치고 은하수를

def solution(n, m, arr):
    answer = 0
    train = [0 for _ in range(n)]

    for i in range(m):
        if arr[i][0] == 1:  # 해당 위치 탑승
            train[arr[i][1] - 1] |= (1 << arr[i][2] - 1)  # 0부터 시작

        elif arr[i][0] == 2:  # 해당 위치 하차
            train[arr[i][1] - 1] &= ~(1 << arr[i][2] - 1)

        elif arr[i][0] == 3:  # 뒤로
            train[arr[i][1] - 1] = train[arr[i][1] - 1] << 1
            train[arr[i][1] - 1] &= ~(1 << 20)  # 20자리

        else:  # 앞으로
            train[arr[i][1] - 1] = train[arr[i][1] - 1] >> 1

    answer = len(set(train))

    return answer


def main():
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(m)]
    print(solution(n, m, arr))


if __name__ == "__main__":
    main()
