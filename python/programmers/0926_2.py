#순위 검색

def solution(info, query):
    answer = []
    dic = {}

    for i in range(len(info)):  # info 값 정리
        temp = info[i].split()
        for a in (temp[0],'-'): # 모든 조합
            for b in (temp[1],'-'):
                for c in (temp[2],'-'):
                    for d in (temp[3],'-'):
                        key=(a,b,c,d)
                        if not dic.get(key, False):
                            dic[key] = [int(temp[4])]
                        else:
                            dic[key].append(int(temp[4]))

    for key in dic:  # 이분탐색을 위한 정렬
        dic[key].sort()

    for q in query: #query 값 정리
        q = q.replace("and ", "")
        temp = q.split()

        key = (temp[0],temp[1],temp[2],temp[3])

        if not dic.get(key, False): #해당 key가 없을때
            answer.append(0)
            continue

        num = dic[key]

        k = len(num)
        left = 0
        right = len(num) - 1
        while left <= right:    #이분탐색
            mid = (left + right) // 2

            if num[mid] >= int(temp[4]):
                right = mid - 1
                k = mid
            else:
                left = mid + 1

        answer.append(len(num) - k)
    return answer

def main():
    info = ["java backend junior pizza 150", "python frontend senior chicken 210", "python frontend senior chicken 150",
            "cpp backend senior pizza 260", "java backend junior chicken 80", "python backend senior chicken 50"]
    query = ["java and backend and junior and pizza 100", "python and frontend and senior and chicken 200",
             "cpp and - and senior and pizza 250", "- and backend and senior and - 150", "- and - and - and chicken 100",
             "- and - and - and - 150"]
    print(solution(info, query))

if __name__ == "__main__":
    main()