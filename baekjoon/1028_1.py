# 합 구하기
import sys
input=sys.stdin.readline

def main():
    n=int(input())
    dp=[0 for _ in range(n+1)]
    arr = list(map(int,input().split()))
    m=int(input())

    dp[1]=arr[0]
    for i in range(2,n+1):
        dp[i]=dp[i-1]+arr[i-1]

    for _ in range(m) :
        i,j=map(int, input().split())
        print(dp[j]-dp[i-1])

if __name__ == "__main__":
    main()