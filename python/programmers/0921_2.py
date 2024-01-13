# 양궁대회

# 점수가 같으면 어피치, 최종 점수 같아도 어피치
# 우승 할수 없으면 [-1]
# 최종 점수 차가 가장 높은 점수를 return
# 최종 점수 차가 같은게 두개 이상이면, 가장 낮은 점수를 많이 맞춘 점수를 retrun
score = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

def dfs(cur, result, cnt, total, info, diff):
    global ans, answer
    # print(cur,cnt)
    if (cur == 10 or cnt == 0) and ans <= total - diff:
        result[10] += cnt
        if ans < total - diff:
            # print(total)
            ans = total - diff
            answer = result[:]
        else:
            for i in range(10, -1, -1):
                if answer[i] < result[i]:
                    answer = result[:]
                    ans = total - diff
                    break
                elif answer[i] > result[i]:
                    break

        result[10] -= cnt
        return

    if cur == 10:
        return

        # 값 변경
    if cnt - (info[cur] + 1) >= 0:
        result[cur] = info[cur] + 1
        if info[cur] > 0:
            dfs(cur + 1, result, cnt - (info[cur] + 1), total + score[cur], info, diff - score[cur])
        else:
            dfs(cur + 1, result, cnt - (info[cur] + 1), total + score[cur], info, diff)
        result[cur] = 0

    dfs(cur + 1, result, cnt, total, info, diff)


def solution(n, info):
    global check, answer, ans
    answer = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ans = 0
    diff = 0
    for i in range(10):
        if info[i] > 0:
            diff += score[i]

    dfs(0, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], n, 0, info, diff)
    if ans == 0:
        return [-1]
    return answer

def main():
    n=5
    info=[2,1,1,1,0,0,0,0,0,0,0]
    print(solution(n,info))

if __name__ == "__main__":
    main()