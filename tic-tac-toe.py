grid = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

locationGrid = [
    ["0,0", "0,1", "0,2"],
    ["1,0", "1,1", "1,2"],
    ["2,0", "2,1", "2,2"]
]

player = 1

line = " ------------- "
def printLine():
    print(line)

def printGrid(grid):
    printLine()
    textGrid = " | "

    for r in range(3):
        for c in range(3):
            textGrid = textGrid + grid[r][c] + " | "
        if r < 2:
            textGrid = textGrid + "\n" + " | "
        
    print(textGrid)
    printLine()

def informGameOver(victor):
    if victor == 0:
        print("No further moves can be made.")
    else:
        print("Player " + str(victor) + " has won the game!")
    printGrid(grid)
    exit(0) 

def isPlayerEntry(entry):
    if entry == 'X':
        return True
    if entry == "O":
        return True
    return False

def isUncoupied(x, y):
    if grid[x][y] == " ":
        return True
    return False

def isValidLocation(entry):
    isValidCoords = False
    for row in locationGrid:
        for cell in row:
            if cell == entry:
                isValidCoords = True
    
    if isValidCoords:
        return isUncoupied(int(entry[0]), int(entry[2]))
    

def threeInARow():
    for row in grid:
        if row[0] == row[1] == row[2] and isPlayerEntry(row[0]):
                return True
    return False

def threeInAColumn():
    for c in range(3):
        if grid[0][c] == grid[1][c] == grid[2][c] and isPlayerEntry(grid[0][c]):
            return True
    return False

def threeInADiagonal():
    if grid[0][0] == grid[1][1] == grid[2][2] and isPlayerEntry(grid[1][1]):
        return True
    if grid[0][2] == grid[1][1] == grid[2][0] and isPlayerEntry(grid[1][1]):
        return True
    return False

def gridIsFull():
    for r in range(3):
        for c in range(3):
            if grid[r][c] == " ":
                return False
    return True

def checkForGameOver():
    # three in a row
    if threeInARow():
        informGameOver(player)

    # three in a column
    if threeInAColumn():
        informGameOver(player)

    # three in a diagonal
    if threeInADiagonal():
        informGameOver(player)

    if gridIsFull():
        informGameOver(0)


# Play the game

print("Welcome to Tic Tac Toe." + "\n")
print("Players have already been assigned markings.")
print("Player 1's moves will be maked with an X.")
print("Player 2's moves will be maked with an O.")
print("\n")
print("Moves are made by specifying the location in the grid where a player wants their mark" + "\n")
print("The grid locations are as follows")
printGrid(locationGrid)

print("Player " + str(player) + ", please make the first move." + "\n")

while not gridIsFull():
    print("Player " + str(player) + ", enter desired location: ")
    move = input().strip()

    while not isValidLocation(move):
        print("Please enter an unoccupoed desired location as it is in this grid:")
        printGrid(locationGrid)
        move = input().strip()

    moveX = int(move[0])
    moveY = int(move[2])

    if player == 1:
        grid[moveX][moveY] = "X"
    else: 
        grid[moveX][moveY]  = "O"

    locationGrid[moveX][moveY] = "   "

    printGrid(grid)

    checkForGameOver()

    if player == 1:
        player = 2
    else:
        player = 1