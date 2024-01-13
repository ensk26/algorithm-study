# 오리

def solution(duck):
    sound = {'q': 0, 'u': 1, 'a': 2, 'c': 3, 'k': 4}
    cnt = 0
    dic = {}

    for d in duck:
        pre = (sound[d] - 1) % 5  # 이전 단어
        for i in range(1, cnt + 1):
            if dic[i] == pre:  # 기존에 있는 오리 소리에서 이어갈수 있는지
                dic[i] = sound[d]
                break

        else:
            if d == 'q':  # 처음 소리
                cnt += 1
                dic[cnt] = 0
            else:  # 녹음 소리가 잘못 되었을때
                return -1

    for i in dic:  # 녹음 소리가 quack로 완성이 안될때
        if dic[i] != 4:
            return -1

    return cnt


def main():
    duck = input()
    print(solution(duck))


if __name__ == "__main__":
    main()
