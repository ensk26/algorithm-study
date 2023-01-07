# 가장 가까운 같은 글자

def solution(s):
    arr = [-1 for _ in range(26)]
    answer = []
    for i in range(len(s)):
        pos = ord(s[i]) - 97
        if arr[pos] > -1:
            answer.append(i - arr[pos])
        else:
            answer.append(-1)

        arr[pos] = i

    return answer


def main():
    s = "abcda"
    print(solution(s))


if __name__ == "__main__":
    main()
