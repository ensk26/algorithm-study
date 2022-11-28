# 귤 고르기

from collections import Counter


def solution(k, tangerine):
    answer = 0
    cnt = 0
    count = Counter(tangerine).most_common()

    for c in count:
        cnt += c[1]
        answer += 1
        if cnt >= k:
            break

    return answer


def main():
    k = 6
    tangerine = [1, 3, 2, 5, 4, 5, 2, 3]
    print(solution(k, tangerine))


if __name__ == "__main__":
    main()
