#쿼드 트리

def equal(n,r,c):   #해당 영역에 모든수가 같은지
    temp = arr[r][c]

    for i in range(r,r+n):
        for j in range(c,c+n):
            if temp != arr[i][j]:
                return False

    return True

def solution(n,r,c):

    if n==1:    #칸 개수가 하나일때
        answer.append(arr[r][c])
        return

    if not equal(n,r,c):    # 모든 수가 같지 않으면
        answer.append("(")
        n//=2
        solution(n,r,c)     #1사분면
        solution(n,r,c+n)   #2사분면
        solution(n,r+n,c)   #3사분면
        solution(n,r+n,c+n) #4사분면

        answer.append(")")

    else:   #모든 수가 같을 때
        answer.append(arr[r][c])
        return

def main():
    global arr,answer
    answer = []
    n = int(input())
    arr = [
        list(map(int,input()))
        for _ in range(n)
    ]
    solution(n, 0, 0)
    print(''.join(map(str,answer)))

if __name__ == "__main__":
    main()