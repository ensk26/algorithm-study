# 빗물

def solution(h,w,hight):

    answer = 0
    for i in range(1,w-1):  #특정 위치를 지정

        left = max(hight[:i])     #현재 위치에서 왼쪽에 가장 높은 높이
        right = max(hight[i:])    #현재 위치에서 오른쪽에 가장 높은 높이

        minH = min(left,right)

        if hight[i] < minH:   #현재 위치의 높이가 left, right 보다 낮을때
            answer += minH-hight[i]   #현재 위치에서 물이 찰 수 있는 칸의 크기

    return answer

def main():
    h,w = map(int,input().split())
    hight = list(map(int,input().split()))
    print(solution(h,w,hight))

if __name__ == "__main__":
    main()