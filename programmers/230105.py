# 디펜스 게임

def gettotal(n, k, enemy, m):
    total = 0
    temp = enemy[:m]
    temp.sort(reverse=True)

    for i in temp[k:]:
        total += i
    return n >= total


def solution(n, k, enemy):
    left = 0
    right = len(enemy)
    while left <= right:
        mid = (left + right) // 2

        if gettotal(n, k, enemy, mid):
            left = mid + 1

        else:
            right = mid - 1

    return left - 1


def main():
    n, k = 7, 3
    enemy = [4, 2, 4, 5, 3, 3, 1]
    print(solution(n, k, enemy))


if __name__ == "__main__":
    main()
