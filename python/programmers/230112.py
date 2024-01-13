# 크기가 작은 부분문자열

def solution(t, p):
    answer = 0
    size = len(p)
    for i in range(len(t) - size + 1):
        if int(p) >= int(t[i:i + size]):
            answer += 1

    return answer


def main():
    t = "3141592"
    p = "271"
    print(solution(t, p))


if __name__ == "__main__":
    main()
