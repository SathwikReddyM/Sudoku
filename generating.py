def generating():
    board = [
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0]
    ]

    from random import sample
    def shuffle(s):
        return sample(s,len(s))
    board[0] = shuffle(range(1,10)) 

    def solve(bo):
        find = find_empty(bo)#finding empty boxes
        #print_board(bo)
        #print("-----------------------")
        if not find:
            return True
        else:
            row, col = find

        for i in range(1,10):# we are looping through 9 numbers
            if valid(bo, i, (row, col)):#checking valid or not if its not valid we will go to next number
                bo[row][col] = i # if its valid we will assign it 

                if solve(bo): # we will go to next elements this will be false if nothing in loop works
                    return True

                bo[row][col] = 0# we will assign the number to zero and loop for the previous thing and thos will go on

        return False


    def valid(bo, num, pos):
        # Checking row (first challenge)
        for i in range(len(bo[0])):
            if bo[pos[0]][i] == num and pos[1] != i:
                return False

        # Checking column (first challenge)
        for i in range(len(bo)):
            if bo[i][pos[1]] == num and pos[0] != i:
                return False

        # Check box (second challenge)
        box_x = pos[1] // 3
        box_y = pos[0] // 3

        for i in range(box_y*3, box_y*3 + 3):
            for j in range(box_x * 3, box_x*3 + 3):
                if bo[i][j] == num and (i,j) != pos:
                    return False

        return True


    def print_board(bo):
        """for i in bo:
            print(i)"""
        for i in range(len(bo)):
            if i % 3 == 0 and i != 0:
                print("- - - - - - - - - - - - ")

            for j in range(len(bo[i])):
                if j % 3 == 0 and j != 0:
                    print(" | ", end="")

                if j == 8:
                    print(bo[i][j])
                else:
                    print(str(bo[i][j]) + " ", end="")


    def find_empty(bo):
        for i in range(len(bo)):
            for j in range(len(bo[0])):
                if bo[i][j] == 0:
                    return (i, j)  # row, col

        return None

    #print_board(board)
    solve(board)
    #print("___________________")
    x = ""
    for i in board: 
        for j in i:
            x = x + str(j) + " "
    return(x)