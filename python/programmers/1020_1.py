# 가장 큰 정사각형 찾기

def solution(board):
    answer = 0
    arr = [[0 for _ in range(len(board[0]))] for _ in range(len(board))]

    for i in range(len(board)):
        arr[i][0] = board[i][0]

    for i in range(len(board[0])):
        arr[0][i] = board[0][i]

    for i in range(1, len(board)):
        for j in range(1, len(board[0])):
            if board[i][j] == 1:
                arr[i][j] = min(arr[i - 1][j - 1], arr[i - 1][j], arr[i][j - 1]) + 1
            else:
                arr[i][j] = 0

    for a in arr:
        answer = max(answer, max(a))

    return answer * answer


def main():
    board = [[0, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [0, 0, 1, 0]]
    print(solution(board))


if __name__ == "__main__":
    main()
