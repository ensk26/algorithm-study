# 과일 장수

def solution(k, m, score):

    answer = 0
    pos=len(score)
    score.sort()
    for i in range(len(score)):
        if score[i]>k:
            pos=i
            break

    score=score[:pos]

    for i in range(len(score)-m,-1,-m):
        answer+=score[i]*m

    return answer

def main():
    k,m=3,4
    score=[1, 2, 3, 1, 2, 3, 1]
    print(solution(k, m, score))

if __name__ == "__main__":
    main()