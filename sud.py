board = [
        [7, 8, 0, 4, 0, 0, 1, 2, 0],
        [6, 0, 0, 0, 7, 5, 0, 0, 9],
        [0, 0, 0, 6, 0, 1, 0, 7, 8],
        [0, 0, 7, 0, 4, 0, 2, 6, 0],
        [0, 0, 1, 0, 5, 0, 9, 3, 0],
        [9, 0, 4, 0, 6, 0, 0, 0, 5],
        [0, 7, 0, 3, 0, 0, 0, 1, 2],
        [1, 2, 0, 0, 0, 7, 4, 0, 0],
        [0, 4, 9, 2, 0, 6, 0, 0, 7]
    ]

board2 = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 1, 7, 9]
    ]

def solve(bd): 
    find = find_empty(bd)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1,10):
        if valid(bd, i, (row,col)):
            bd[row][col] = i

            if solve(bd):
                return True

            bd[row][col] = 0
    return False



def valid(bd, num, pos):

#check row
    for i in range(len(bd[0])):
        if bd[pos[0]][i] == num and pos[1] != i:
            return False
#check col
    for i in range(len(bd)):
        if bd[i][pos[1]] == num and pos[0] != i:
            return False

#check box
    box_x = pos [1] // 3
    box_y = pos [0] // 3

    for i in range(box_y * 3, box_y*3 + 3):
        for j in range(box_x * 3, box_x*3 + 3):
            if bd[i][j] == num and (i,j) != pos:
                return False

    return True

def print_board(bd) :

        for i in range(len(bd)):
            if i % 3 == 0 and i != 0:
                print("- - - - - - - - - - - - -")

            for j in range(len(bd[0])):
                if j % 3== 0 and j != 0:
                    print(" | ", end = "")

                if j == 8:
                        print(bd[i][j])
                else:
                        print(str(bd[i][j]) + " ", end="" )


def find_empty(bd):
    for i in range (len(bd)):
        for j in range(len(bd[0])):
            if bd[i][j] == 0:
                return (i,j)    #row, col

    return None


boardnum = input("Input which board to solve (1 or 2):\n")

if boardnum == '1':
    print_board(board)
    solve(board)
    print('__________________________\n')
    print_board(board)

if boardnum == '2':
    print_board(board2)
    solve(board2)
    print('__________________________\n')
    print_board(board2)
