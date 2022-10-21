# 롤케이크 자르기

from collections import Counter


def solution(topping):
    answer = 0
    dic = Counter(topping)
    temp = set()

    for i in topping:
        dic[i] -= 1
        if dic[i] == 0:
            dic.pop(i)
        temp.add(i)
        if len(dic) == len(temp):
            answer += 1

    return answer


def main():
    topping = [1, 2, 1, 3, 1, 4, 1, 2]
    print(solution(topping))


if __name__ == "__main__":
    main()
