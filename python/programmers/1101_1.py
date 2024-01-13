# 야간 전술 보행

# distance 거리
# scope 경비병 감시 구간
# times 근무시간, 휴식시간

def solution(distance, scope, times):
    answer = 0
    position = [False for _ in range(distance)]

    # 경비병이 있는 경우
    for k in range(len(scope)):
        i, j = scope[k][0], scope[k][1]
        if i > j:
            i, j = j, i
        for d in range(i - 1, j):
            if times[k][0] > d % (times[k][0] + times[k][1]):
                position[d] = True

    for i in range(distance):
        answer += 1
        if position[i]:
            break

    return answer


def main():
    distance = 12
    scope = [[7, 8], [4, 6], [11, 10]]
    times = [[2, 2], [2, 4], [3, 3]]
    print(solution(distance, scope, times))


if __name__ == "__main__":
    main()
