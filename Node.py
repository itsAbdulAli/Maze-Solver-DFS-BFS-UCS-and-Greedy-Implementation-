import copy
class MapNode():
    children = []
    matrix=[[]]
    RowsCount=0
    ColsCount=0
    PlayerPos = [0,0]

    def __init__(self, matrix, parent,Rows,Cols,PlayerPos=[0,0]):
        self.matrix = matrix
        self.parent = parent
        self.RowsCount=Rows
        self.ColsCount=Cols
        self.children=[]
        self.PlayerPos=PlayerPos


    def addChildren(self, Node):
        self.children.append(Node)

    def printMatrix(self):
        print("")
        for row in self.matrix:
            print(row)

    def searchChildren(self, Node):
        check = False
        for x in self.children:
            if x == Node.matrix:
                check = True
        return check

    def printChildren(self):
        for x in self.children:
            x.printMatrix()
            print("")

    def checkMatrix(self,matrix):
        if self.matrix==matrix:
            return True
        else:
            return False

    def returnMatrix(self):
        return copy.deepcopy(self.matrix)

class MapNodewithCost():
        children = []
        matrix = [[]]
        RowsCount = 0
        ColsCount = 0
        Cost=0
        PlayerPos = [0,0]

        def __init__(self, matrix, parent, Rows, Cols,Cost,PlayerPos = [0,0]):
            self.matrix = matrix
            self.parent = parent
            self.RowsCount = Rows
            self.ColsCount = Cols
            self.children = []
            self.cost=Cost
            self.PlayerPos=PlayerPos

        def addChildren(self, Node):
            self.children.append(Node)

        def printMatrix(self):
            print("")
            for row in self.matrix:
                print(row)

        def searchChildren(self, Node):
            check = False
            for x in self.children:
                if x == Node.matrix:
                    check = True
            return check

        def printChildren(self):
            for x in self.children:
                x.printMatrix()
                print("")

        def checkMatrix(self, matrix):
            if self.matrix == matrix:
                return True
            else:
                return False

        def returnMatrix(self):
            return copy.deepcopy(self.matrix)