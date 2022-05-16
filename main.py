
#Take input from file "input.txt"
#Format:
#No of Rows
#No of Cols
#Map (S -> Start E -> End/Goal O -> Obstacles X -> Empty(Explorable) Space)
#Goal Position
#Start Position
######################
#Path Explored denoted with Z
#Uncomment calls RunDFS()/RunBFS()/RunUCS()/RunGreedy() and Run
from Node import MapNode
from Node import MapNodewithCost
import playerMovement
from collections import deque
from queue import PriorityQueue
from itertools import count
from math import dist
import copy

ExploredNodes = []
global goalFound


def PopulateMap(filename, Map):
    Goal=[0,0]
    Start=[0,0]
    inputFile = open(filename, 'r')
    Rows = inputFile.read(1)
    Rows = ord(Rows) - 48
    inputFile.read(1)
    Cols = inputFile.read(1)
    Cols = ord(Cols) - 48
    inputFile.read(1)
    Map = []
    for r in range(0, Rows):
        Map_Row = []
        for c in range(0, Cols):
            Map_Row.append(inputFile.read(1))
        Map.append(Map_Row)
        inputFile.read(1)
    Goal[0]=ord(inputFile.read(1))-48
    Goal[1] = ord(inputFile.read(1)) - 48
    inputFile.read(1)
    Start[0]=ord(inputFile.read(1))-48
    Start[1] = ord(inputFile.read(1)) - 48
    return Map, Rows, Cols, Goal, Start


def PrintMap(Map):
    print("")
    for x in (Map):
        print(x)


def RunDFS(Node: MapNode):
    goalFound = False
    myStack = deque()
    myStack.append(Node)
    while (myStack):
        poppedNode = myStack.pop()
        if (goalFound == True):  # goal node
            PrintMap(poppedNode.matrix)
            print("Found Goal")
            return
        else:
            PrintMap(poppedNode.matrix)
            leftExplored = False
            rightExplored = False
            upExplored = False
            downExplored = False
            LeftMat, goalFound, P = playerMovement.moveLeft(poppedNode.returnMatrix())
            if goalFound == True:
                PrintMap(LeftMat)
                print("Found Goal")
                return
            RightMat, goalFound, P = playerMovement.moveRight(poppedNode.returnMatrix())
            if goalFound == True:
                PrintMap(RightMat)
                print("Found Goal")
                return
            UpMat, goalFound, P = playerMovement.moveUp(poppedNode.returnMatrix())
            if goalFound == True:
                PrintMap(UpMat)
                print("Found Goal")
                return
            DownMat, goalFound,P = playerMovement.moveDown(poppedNode.returnMatrix())
            if goalFound == True:
                PrintMap(DownMat)
                print("Found Goal")
                return
            LeftMatrix = MapNode(LeftMat, Node, Node.RowsCount, Node.ColsCount)
            RightMatrix = MapNode(RightMat, Node, Node.RowsCount, Node.ColsCount)
            UpMatrix = MapNode(UpMat, Node, Node.RowsCount, Node.ColsCount)
            DownMatrix = MapNode(DownMat, Node, Node.RowsCount, Node.ColsCount)
            for x in ExploredNodes:
                if x == LeftMatrix.matrix:
                    leftExplored = True
                    # print("Left explored")
                if x == RightMatrix.matrix:
                    rightExplored = True
                    # print("Right explored")
                if x == UpMatrix.matrix:
                    upExplored = True
                    # print("Up explored")
                if x == DownMatrix.matrix:
                    downExplored = True
                    # print("Down explored")

            if leftExplored == False and LeftMatrix.matrix != None:
                ExploredNodes.append(LeftMatrix.matrix)
                LeftMatrix.printMatrix()
                myStack.append(LeftMatrix)

            if rightExplored == False and RightMatrix.matrix != None:
                ExploredNodes.append(RightMatrix.matrix)
                RightMatrix.printMatrix()
                myStack.append(RightMatrix)

            if upExplored == False and UpMatrix.matrix != None:
                ExploredNodes.append(UpMatrix.matrix)
                UpMatrix.printMatrix()
                myStack.append(UpMatrix)

            if downExplored == False and DownMatrix.matrix != None:
                ExploredNodes.append(DownMatrix.matrix)
                DownMatrix.printMatrix()
                myStack.append(DownMatrix)


def RunBFS(Node: MapNode):
    goalFound = False
    myStack = deque()
    myStack.append(Node)
    while (myStack):
        poppedNode = myStack.popleft()
        if (goalFound == True):  # goal node
            PrintMap(poppedNode.matrix)
            print("Found Goal")
            return
        else:
            PrintMap(poppedNode.matrix)
            leftExplored = False
            rightExplored = False
            upExplored = False
            downExplored = False
            LeftMat, goalFound, P = playerMovement.moveLeft(poppedNode.returnMatrix())
            if goalFound == True:
                PrintMap(LeftMat)
                print("Found Goal")
                return
            RightMat, goalFound, P = playerMovement.moveRight(poppedNode.returnMatrix())
            if goalFound == True:
                PrintMap(RightMat)
                print("Found Goal")
                return
            UpMat, goalFound, P = playerMovement.moveUp(poppedNode.returnMatrix())
            if goalFound == True:
                PrintMap(UpMat)
                print("Found Goal")
                return
            DownMat, goalFound, P = playerMovement.moveDown(poppedNode.returnMatrix())
            if goalFound == True:
                PrintMap(DownMat)
                print("Found Goal")
                return
            LeftMatrix = MapNode(LeftMat, Node, Node.RowsCount, Node.ColsCount)
            RightMatrix = MapNode(RightMat, Node, Node.RowsCount, Node.ColsCount)
            UpMatrix = MapNode(UpMat, Node, Node.RowsCount, Node.ColsCount)
            DownMatrix = MapNode(DownMat, Node, Node.RowsCount, Node.ColsCount)
            for x in ExploredNodes:
                if x == LeftMatrix.matrix:
                    leftExplored = True
                    # print("Left explored")
                if x == RightMatrix.matrix:
                    rightExplored = True
                    # print("Right explored")
                if x == UpMatrix.matrix:
                    upExplored = True
                    # print("Up explored")
                if x == DownMatrix.matrix:
                    downExplored = True
                    # print("Down explored")

            if leftExplored == False and LeftMatrix.matrix != None:
                ExploredNodes.append(LeftMatrix.matrix)
                LeftMatrix.printMatrix()
                myStack.append(LeftMatrix)

            if rightExplored == False and RightMatrix.matrix != None:
                ExploredNodes.append(RightMatrix.matrix)
                RightMatrix.printMatrix()
                myStack.append(RightMatrix)

            if upExplored == False and UpMatrix.matrix != None:
                ExploredNodes.append(UpMatrix.matrix)
                UpMatrix.printMatrix()
                myStack.append(UpMatrix)

            if downExplored == False and DownMatrix.matrix != None:
                ExploredNodes.append(DownMatrix.matrix)
                DownMatrix.printMatrix()
                myStack.append(DownMatrix)


def RunUCS(Node: MapNodewithCost):
    unique = count() # using this for ties in comparision in Priority Queue
    goalFound = False
    myStack = PriorityQueue()
    myStack.put((Node.Cost,next(unique),Node))
    while (myStack):
        poppedNode = (myStack.get())[2]
        if (goalFound == True):  # goal node
            PrintMap(poppedNode.matrix)
            print("Found Goal")
            return
        else:
            PrintMap(poppedNode.matrix)
            leftExplored = False
            rightExplored = False
            upExplored = False
            downExplored = False
            LeftMat, goalFound, P = playerMovement.moveLeft(poppedNode.returnMatrix())
            if goalFound == True:
                PrintMap(LeftMat)
                print("Found Goal")
                return
            RightMat, goalFound, P = playerMovement.moveRight(poppedNode.returnMatrix())
            if goalFound == True:
                PrintMap(RightMat)
                print("Found Goal")
                return
            UpMat, goalFound, P = playerMovement.moveUp(poppedNode.returnMatrix())
            if goalFound == True:
                PrintMap(UpMat)
                print("Found Goal")
                return
            DownMat, goalFound, P = playerMovement.moveDown(poppedNode.returnMatrix())
            if goalFound == True:
                PrintMap(DownMat)
                print("Found Goal")
                return
            LeftMatrix = MapNodewithCost(LeftMat, Node, Node.RowsCount, Node.ColsCount,poppedNode.Cost+1)
            RightMatrix = MapNodewithCost(RightMat, Node, Node.RowsCount, Node.ColsCount,poppedNode.Cost+1)
            UpMatrix = MapNodewithCost(UpMat, Node, Node.RowsCount, Node.ColsCount,poppedNode.Cost+1)
            DownMatrix = MapNodewithCost(DownMat, Node, Node.RowsCount, Node.ColsCount,poppedNode.Cost+1)
            for x in ExploredNodes:
                if x == LeftMatrix.matrix:
                    leftExplored = True
                    # print("Left explored")
                if x == RightMatrix.matrix:
                    rightExplored = True
                    # print("Right explored")
                if x == UpMatrix.matrix:
                    upExplored = True
                    # print("Up explored")
                if x == DownMatrix.matrix:
                    downExplored = True
                    # print("Down explored")

            if leftExplored == False and LeftMatrix.matrix != None:
                ExploredNodes.append(LeftMatrix.matrix)
                myStack.put((LeftMatrix.Cost,next(unique),LeftMatrix))

            if rightExplored == False and RightMatrix.matrix != None:
                ExploredNodes.append(RightMatrix.matrix)
                myStack.put((RightMatrix.Cost,next(unique),RightMatrix))

            if upExplored == False and UpMatrix.matrix != None:
                ExploredNodes.append(UpMatrix.matrix)
                myStack.put((UpMatrix.Cost,next(unique),UpMatrix))

            if downExplored == False and DownMatrix.matrix != None:
                ExploredNodes.append(DownMatrix.matrix)
                myStack.put((DownMatrix.Cost,next(unique),DownMatrix))


def RunGreedy(Node: MapNodewithCost,GoalPos):
    unique = count() # using this for ties in comparision in Priority Queue
    goalFound = False
    myStack = PriorityQueue()
    myStack.put((Node.Cost,next(unique),Node))
    while (myStack):
        poppedNode = (myStack.get())[2]
        if (goalFound == True):  # goal node
            PrintMap(poppedNode.matrix)
            print("Found Goal")
            return
        else:
            PrintMap(poppedNode.matrix)
            leftExplored = False
            rightExplored = False
            upExplored = False
            downExplored = False
            LeftMat, goalFound, PlayerPosleft = playerMovement.moveLeft(poppedNode.returnMatrix(),copy.deepcopy(poppedNode.PlayerPos))
            if goalFound == True:
                PrintMap(LeftMat)
                print("Found Goal")
                return
            RightMat, goalFound, PlayerPosright = playerMovement.moveRight(poppedNode.returnMatrix(),copy.deepcopy(poppedNode.PlayerPos))
            if goalFound == True:
                PrintMap(RightMat)
                print("Found Goal")
                return
            UpMat, goalFound, PlayerPosup = playerMovement.moveUp(poppedNode.returnMatrix(),copy.deepcopy(poppedNode.PlayerPos))
            if goalFound == True:
                PrintMap(UpMat)
                print("Found Goal")
                return
            DownMat, goalFound, PlayerPosdown = playerMovement.moveDown(poppedNode.returnMatrix(),copy.deepcopy(poppedNode.PlayerPos))
            if goalFound == True:
                PrintMap(DownMat)
                print("Found Goal")
                return
            LeftMatrix = MapNodewithCost(LeftMat, Node, Node.RowsCount, Node.ColsCount,dist(GoalPos,PlayerPosleft),PlayerPosleft)
            print("Left Position = ", PlayerPosleft)
            print("Left Heuristic = ", dist(GoalPos,PlayerPosleft))
            RightMatrix = MapNodewithCost(RightMat, Node, Node.RowsCount, Node.ColsCount,dist(GoalPos,PlayerPosright),PlayerPosright)
            print("Right Position = ", PlayerPosright)
            print("Right Heuristic = ", dist(GoalPos, PlayerPosright))
            UpMatrix = MapNodewithCost(UpMat, Node, Node.RowsCount, Node.ColsCount,dist(GoalPos,PlayerPosup),PlayerPosup)
            print("Up Position = ", PlayerPosup)
            print("Up Heuristic = ", dist(GoalPos, PlayerPosup))
            DownMatrix = MapNodewithCost(DownMat, Node, Node.RowsCount, Node.ColsCount,dist(GoalPos,PlayerPosdown),PlayerPosdown)
            print("Down Position = ", PlayerPosdown)
            print("Down Heuristic = ", dist(GoalPos, PlayerPosdown))
            for x in ExploredNodes:
                if x == LeftMatrix.matrix:
                    leftExplored = True
                    # print("Left explored")
                if x == RightMatrix.matrix:
                    rightExplored = True
                    # print("Right explored")
                if x == UpMatrix.matrix:
                    upExplored = True
                    # print("Up explored")
                if x == DownMatrix.matrix:
                    downExplored = True
                    # print("Down explored")

            if leftExplored == False and LeftMatrix.matrix != None and LeftMatrix.cost<=RightMatrix.cost and LeftMatrix.cost<=UpMatrix.cost and LeftMatrix.cost<=DownMatrix.cost:
                ExploredNodes.append(LeftMatrix.matrix)
                myStack.put((LeftMatrix.Cost,next(unique),LeftMatrix))

            elif rightExplored == False and RightMatrix.matrix != None and RightMatrix.cost<=LeftMatrix.cost and RightMatrix.cost<=UpMatrix.cost and RightMatrix.cost<=DownMatrix.cost:
                ExploredNodes.append(RightMatrix.matrix)
                myStack.put((RightMatrix.Cost,next(unique),RightMatrix))

            elif upExplored == False and UpMatrix.matrix != None and UpMatrix.cost<=RightMatrix.cost and UpMatrix.cost<=LeftMatrix.cost and UpMatrix.cost<=DownMatrix.cost:
                ExploredNodes.append(UpMatrix.matrix)
                myStack.put((UpMatrix.Cost,next(unique),UpMatrix))

            elif downExplored == False and DownMatrix.matrix != None and DownMatrix.cost<=RightMatrix.cost and DownMatrix.cost<=UpMatrix.cost and DownMatrix.cost<=LeftMatrix.cost:
                ExploredNodes.append(DownMatrix.matrix)
                myStack.put((DownMatrix.Cost,next(unique),DownMatrix))

            else:
                print("No shortest way forward!")
                return


Map = []
Goal = []
Start = []
Map, Rows, Cols, Goal, Start = PopulateMap("input.txt", Map)
Root = MapNode(Map, None, Rows, Cols,Start)
RootwithCost = MapNodewithCost(Map, None, Rows, Cols,dist(Goal,Start),Start)
#RunDFS(Root)
#RunBFS(Root)
#RunUCS(RootwithCost)
RunGreedy(RootwithCost,Goal)
print("Nodes Explored: ", len(ExploredNodes))
