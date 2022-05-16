def moveLeft (newMatrix,PlayerPos=[0,0]):
    check = False
    goalFound = False
    for row in range(0, len(newMatrix)):
        for col in range(0, len(newMatrix[row])):
            if newMatrix[row][col] == "S":
                if col > 0:
                    if newMatrix[row][col-1] == "X" or newMatrix[row][col-1] == "E":
                        if newMatrix[row][col - 1] == "E":
                            goalFound = True
                        temp = newMatrix[row][col - 1]
                        newMatrix[row][col - 1] = "S"
                        newMatrix[row][col] = "Z"
                        check = True

            if (check == True):
                break
        if (check == True):
            break
    if check == False:
        return None,False,PlayerPos
    elif check == True:
        PlayerPos[1] = PlayerPos[1]-1
        return newMatrix,goalFound, PlayerPos

def moveRight(newMatrix,PlayerPos=[0,0]):
    check = False
    goalFound = False
    for row in range(0, len(newMatrix)):
        for col in range(0, len(newMatrix[row])):
            if newMatrix[row][col] == "S":
                if col < len(newMatrix[row]) - 1:
                    if newMatrix[row][col+1]=="X" or newMatrix[row][col+1] == "E":
                        if newMatrix[row][col+1]=="E":
                            goalFound=True
                        temp = newMatrix[row][col + 1]
                        newMatrix[row][col + 1] = "S"
                        newMatrix[row][col] = "Z"
                        check = True

            if (check == True):
                break
        if (check == True):
            break
    if check == False:
        return None,False,PlayerPos
    elif check == True:
        PlayerPos[1] = PlayerPos[1] + 1
        return newMatrix,goalFound, PlayerPos

def moveUp(newMatrix,PlayerPos=[0,0]):
    check = False
    goalFound = False
    for row in range(0, len(newMatrix)):
        for col in range(0, len(newMatrix[row])):
            if newMatrix[row][col] == "S":
                if row > 0:
                    if (newMatrix[row-1][col]=="X" or newMatrix[row-1][col] == "E"):
                        if newMatrix[row-1][col] == "E":
                            goalFound=True
                        temp = newMatrix[row - 1][col]
                        newMatrix[row - 1][col] = "S"
                        newMatrix[row][col] = "Z"
                        check = True

            if (check == True):
                break
        if (check == True):
            break
    if check == False:
        return None,False,PlayerPos
    elif check == True:
        PlayerPos[0] = PlayerPos[0] - 1
        return newMatrix,goalFound, PlayerPos

def moveDown(newMatrix,PlayerPos=[0,0]):
    check = False
    goalFound = False
    for row in range(0, len(newMatrix)):
        for col in range(0, len(newMatrix[row])):
            if newMatrix[row][col] == "S":
                if row < len(newMatrix) - 1:
                    if newMatrix[row+1][col]=="X" or newMatrix[row+1][col] == "E":
                        if newMatrix[row+1][col]=="E":
                            goalFound=True
                        temp = newMatrix[row + 1][col]
                        newMatrix[row + 1][col] = "S"
                        newMatrix[row][col] = "Z"
                        check = True

            if (check == True):
                break
        if (check == True):
            break
    if check == False:
        return None,False,PlayerPos
    elif check == True:
        PlayerPos[0] = PlayerPos[0] + 1
        return newMatrix,goalFound, PlayerPos