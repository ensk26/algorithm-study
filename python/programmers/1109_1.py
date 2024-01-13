# 단어 변환
from collections import deque

q = deque()


def isValid(word1, word2):
    cnt = 0

    for w1, w2 in zip(word1, word2):
        if w1 == w2:
            cnt += 1

    return cnt == len(word1) - 1


def solution(begin, target, words):
    visited = [False for _ in range(len(words))]
    q.append((begin, 0))

    while q:
        cur, d = q.popleft()

        for i in range(len(words)):
            if not visited[i] and isValid(cur, words[i]):
                if words[i] == target:
                    return d + 1
                visited[i] = True
                q.append((words[i], d + 1))

    return 0


def main():
    begin, target, words = "hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]
    print(solution(begin, target, words))


if __name__ == "__main__":
    main()
