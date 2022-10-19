# 혼자 놀기의 달인

def solution(cards):
    answer = 1
    visited = [False for _ in range(len(cards))]
    group = []

    for i in range(len(cards)):

        if not visited[i]:
            k = cards[i] - 1  # 배열 0번째 부터
            cnt = 0
            while not visited[k]:  # 방문한 번호가 없을때 까지
                visited[k] = True
                k = cards[k] - 1  # 배열 0번째 부터
                cnt += 1

            group.append(cnt)

    if len(group) > 1:
        group.sort(reverse=True)
        answer = group[0] * group[1]

    else:
        answer = 0

    return answer


def main():
    cards = [8, 6, 3, 7, 2, 5, 1, 4]
    print(solution(cards))


if __name__ == "__main__":
    main()
