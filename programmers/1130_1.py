# 연속 부분 수열 합의 개수

def solution(elements):
    answer = set()

    for k in range(len(elements)):  # 크기
        total = 0
        cnt = 0
        left = 0

        for right in range(len(elements) + k):  # 요소
            right %= len(elements)
            total += elements[right]
            cnt += 1

            if cnt == k:
                answer.add(total)

            while cnt == k:
                total -= elements[left]
                left = (left + 1) % len(elements)
                cnt -= 1

    answer.add(sum(elements))

    return len(answer)


def main():
    elements = [7, 9, 1, 1, 4]
    print(solution(elements))


if __name__ == "__main__":
    main()
