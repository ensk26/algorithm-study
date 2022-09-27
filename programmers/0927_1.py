#모음사전

# A,E,I,O,U로 길이가 5이하의 모든 단어

temp = []
dic = {}
cnt = 0  # 처음은 공백이 나온다.

def dfs(cur):
    global cnt
    if cur == 6:
        return

    dic[''.join(temp)] = cnt
    cnt += 1

    for w in ('A', 'E', 'I', 'O', 'U'):
        temp.append(w)
        dfs(cur + 1)
        temp.pop()

def solution(word):
    answer = 0
    dfs(0)
    answer = dic[word]
    return answer

def main():
    word = "EIO"
    print(solution(word))

if __name__ == "__main__":
    main()