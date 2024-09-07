A = []
for i in range(3):
    A.append([])
    for j in range(3):
        A[i].append(' ')

def board():
    print(f'{A[0]}\n{A[1]}\n{A[2]}')

def referee(x):
    result = False
    board()
    if A[B-1][C-1] == A[B-1][C-2] == A[B-1][C-3] == x:
        print(A[B-1][C-1], "VICTORY!")
        result = True
    elif A[B-1][C-1] == A[B-2][C-1] == A[B-3][C-1] == x:
        print(A[B-1][C-1], "VICTORY!")
        result = True
    elif A[0][0] == A[1][1] == A[2][2] == x:
        print(A[0][0], "VICTORY!")
        result = True
    elif A[0][2] == A[1][1] == A[2][0] == x:
        print(A[0][2], "VICTORY!")
        result = True
    return result

num = 0
board()
# print(f'{A[0]}\n{A[1]}\n{A[2]}')
while True:
    B, C = map(int, input().split())
    if (B > 3 or C > 3) or (B < 1 or C < 1):
        print("자리 번호가 초과 혹은 미만입니다.\n다시 선택하십시오.")
    elif A[B-1][C-1] == ('O' or 'X'):
        print("이미 선택된 자리입니다.\n다른 곳을 선택하십시오.")
    elif num % 2 == 0:
        A[B-1][C-1] = 'O'
        num += 1
        if referee('O'):
            break
        # print(f'{A[0]}\n{A[1]}\n{A[2]}')
        # if A[B-1][C-1] == A[B-1][C-2] == A[B-1][C-3] == 'O':
        #     print(A[B-1][C-1], "VICTORY!")
        #     break
        # elif A[B-1][C-1] == A[B-2][C-1] == A[B-3][C-1] == 'O':
        #     print(A[B-1][C-1], "VICTORY!")
        #     break
        # elif A[0][0] == A[1][1] == A[2][2] == 'O':
        #     print(A[0][0], "VICTORY!")
        #     break
        # elif A[0][2] == A[1][1] == A[2][0] == 'O':
        #     print(A[0][2], "VICTORY!")
        #     break
    elif num % 2 == 1:
        A[B-1][C-1] = 'X'
        num += 1
        if referee('X'):
            break
        # print(f'{A[0]}\n{A[1]}\n{A[2]}')
        # if A[B-1][C-1] == A[B-1][C-2] == A[B-1][C-3] == 'X':
        #     print(A[B-1][C-1], "VICTORY!")
        #     break
        # elif A[B-1][C-1] == A[B-2][C-1] == A[B-3][C-1] == 'X':
        #     print(A[B-1][C-1], "VICTORY!")
        #     break
        # elif A[0][0] == A[1][1] == A[2][2] == 'X':
        #     print(A[0][0], "VICTORY!")
        #     break
        # elif A[0][2] == A[1][1] == A[2][0] == 'X':
        #     print(A[0][2], "VICTORY!")
        #     break
    if num == 9:
        print("무승부!!\n리겜???")
        num = 0
        one_more = input()
        if one_more == "yes":
            print("LET'S DO IT AGAIN!!")
            for i in range(3):
                for j in range(3):
                    A[i][j] = ' '
            board()
            # print(f'{A[0]}\n{A[1]}\n{A[2]}')
        elif one_more == "no":
            print("GG")
            break