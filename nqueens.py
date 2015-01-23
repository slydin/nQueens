#An attempt at the Nqueens problem in python.

def start():
    #Ask the user for the desired number of Queens.
    while True:
        userInput = input('Please input the number of queens desired:')
        intCheck = True
        try:
            numberOfQueens = int(userInput)
        except ValueError:
            intCheck = False
            print('Please insert a positive integer.')
        finally:
            if intCheck:
                if numberOfQueens < 1:
                    print('Please insert a positive integer.')
                else:
                    break
    print("N = " + str(numberOfQueens))
    return numberOfQueens

def createBoard(numberOfQueens):
    #Make the chessboard with each empty space represented by a zero.
    chessBoard = []
    for i in range(numberOfQueens):
        chessRow = []
        for j in range(numberOfQueens):
            chessRow.append(0)
        chessBoard.append(chessRow)
    print("Clear Board: " + "\n")
    for i in range(numberOfQueens):
        print(chessBoard[i])
    return chessBoard

def isValid(chessBoard, row, col):
    if row < 0 or col < 0:
        return False
    if row >= len(chessBoard) or col >= len(chessBoard):
        return False
    return True

def verticalCheck(chessBoard, position):
    empty = True
    for i in range(len(chessBoard)):
        if chessBoard[i][position] != 0:
            empty = False
            break
    return empty

def leftDiagonalCheck(chessBoard, row, col):
    if not isValid(chessBoard, row, col):
        return False
    for i in range(len(chessBoard)):
        if isValid(chessBoard, row - i, col - i):
            if chessBoard[row-i][col-i] == 1:
                return False
        if isValid(chessBoard, row + i, col + i):
            if chessBoard[row+i][col+i] == 1:
                return False
    return True

def rightDiagonalCheck(chessBoard, row, col):
    if not isValid(chessBoard, row, col):
        return False
    for i in range(len(chessBoard)):
        if isValid(chessBoard, row + i, col - i):
            if chessBoard[row+i][col-i] == 1:
                return False
        if isValid(chessBoard, row - i, col + i):
            if chessBoard[row-i][col+i] == 1:
                return False
    return True

def check(chessBoard, row, col):
    if not verticalCheck(chessBoard, col):
        return False
    if not leftDiagonalCheck(chessBoard, row, col):
        return False
    if not rightDiagonalCheck(chessBoard, row, col):
        return False
    return True
    
#Nqueens algorithm
def nQueens(chessBoard, row):
    #Base cases
    if numQueens(chessBoard) == len(chessBoard):
        return True

    if row < len(chessBoard):
        for j in range(len(chessBoard)):
            # First check to see if the position is clear and valid
            # If it is set a queen on the position
            if check(chessBoard, row, j):
                chessBoard[row][j] = 1
                if not nQueens(chessBoard, row + 1): # Check the next row
                    chessBoard[row][j] = 0 # If we cannot place a queen reset the current position
                if numQueens(chessBoard) == len(chessBoard):
                    return True
    
    return False

#Queen counter
def numQueens(checkBoard):
    #go through each row and column to locate queens
    numberOfQueens = 0
    for i in range(len(checkBoard)):
        for j in range(len(checkBoard)):
            if checkBoard[i][j] == 1:
                numberOfQueens = numberOfQueens + 1
                break
    return numberOfQueens

#chessBoard = createBoard(start())

#print verticalCheck(chessBoard, 0)
#print leftDiagonalCheck(chessBoard, 0, 0)
#print rightDiagonalCheck(chessBoard, 0, 0)

#print check(chessBoard, 0, 0)
#print nQueens(chessBoard, 0)
#Queens will be represented by an 1.

# #  0 1 2 3
#    - - - -
# 0 |0 0 1 0
# 1 |1 0 0 0
# 2 |0 0 0 1
# 3 |0 1 0 0

#test = [[0, 0, 1, 0], [1, 0, 0, 0], [0, 0, 0, 1], [0, 1, 0, 0]]
#print rightDiagonalCheck(test, 3, 0) # should be true
#print rightDiagonalCheck(test, 2, 0) # should be false
#print leftDiagonalCheck(test, 3, 3) # should be true
#print leftDiagonalCheck(test, 3, 2) # should be false

def main():
    chessBoard = createBoard(start())
    nQueens(chessBoard,0)
    print("Solution: " + "\n")
    for i in range(len(chessBoard)):
        print(chessBoard[i])

if __name__ == '__main__':
    main()
