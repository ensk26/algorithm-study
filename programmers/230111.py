# 구명보트

def solution(people, limit):
    answer = 0
    left = 0
    right = len(people) - 1
    people.sort()
    boat = 0

    while left < right:

        while left < right and boat + people[right] <= limit:
            boat += people[right]
            right -= 1

        while left < right and boat + people[left] <= limit:
            boat += people[left]
            left += 1

        if left == right and boat + people[left] > limit:
            answer += 1

        boat = 0
        answer += 1

    return answer


def main():
    people = [70, 80, 50]
    limit = 100
    print(solution(people, limit))


if __name__ == "__main__":
    main()
