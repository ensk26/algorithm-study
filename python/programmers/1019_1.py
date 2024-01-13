# 택배상자

def solution(order):

    answer = 0
    stack=[]
    k=1
    for i in order:

        if k<=i:
            while k<i:
                stack.append(k)
                k+=1
            k+=1    #같을때

        else:   #k>i
            if stack[-1]!=i:    #컨테이너와 보조 컨테이너에도 없을때
                break

            stack.pop() #보조 컨테이터에 해당 숫자가 있을때

        answer+=1   #만족하는 숫자가 있을때

    return answer

def main():
    order = [4, 3, 1, 2, 5]
    print(solution(order))

if __name__ == "__main__":
    main()