# 마법사 상어와 파이어볼

# i번 파이어볼의 위치는 (ri, ci), 질량은 mi이고, 방향은 di, 속력은 si
# 파이어볼의 정보는 다섯 정수 ri, ci, mi, si, di

from collections import deque

q=deque()


def move(r,c,s,d,n):
    if d == 0:
        r = r - s

    elif d == 1:
        r, c = r - s, c + s

    elif d == 2:
         c =  c + s

    elif d == 3:
        r, c = r + s, c + s

    elif d == 4:
        r = r + s

    elif d == 5:
        r, c = r + s, c - s

    elif d == 6:
        c = c - s

    elif d == 7:
        r, c = r - s, c - s

    return (r%n,c%n)

def solution(n,k,fire):

    answer = 0

    arr=[[[] for i in range(n)] for _ in range(n)]   #질량, 속력, 방향

    #초기값
    for r,c,m,s,d in fire:
        q.append((r-1,c-1,m,s,d))

    for _ in range(k):
        #파이어볼 이동
        while q:
            r,c,m,s,d=q.popleft()

            nr,nc=move(r, c, s, d,n)
            arr[nr][nc].append((m,s,d))

        for i in range(n):
            for j in range(n):
                if len(arr[i][j])>1:    #2이상
                    nm,ns,odd,even,cnt=0,0,0,0,len(arr[i][j])
                    while arr[i][j]:
                        m,s,d=arr[i][j].pop(0)
                        nm+=m
                        ns+=s
                        if d%2==1:
                            odd+=1
                        else:
                            even+=1

                    if odd==cnt or even==cnt:
                        nd=[0, 2, 4, 6]
                    else:
                        nd=[1, 3, 5, 7]

                    if nm//5!=0:
                        for d in nd:
                            q.append((i,j,nm//5,ns//cnt,d))

                if len(arr[i][j])==1:
                    m, s, d = arr[i][j].pop()
                    q.append((i,j,m,s,d))

    while q:
        r,c,m,s,d=q.pop()
        answer+=m

    return answer

def main():
    n,m,k = map(int,input().split())
    fire = [list(map(int,input().split())) for _ in range(m)]
    print(solution(n,k,fire))

if __name__ == "__main__":
    main()