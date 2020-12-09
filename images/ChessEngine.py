# where we store data about the current state of the chess game
# determening the valid moves at the current state
# move log (undo moves etc)

class GameState():
    def __init__(self): #constructor , whites perspective, each array is row
        self.board = [ #the board is 8x8 2 dimenisonal list, 1st character = color, 2nd character = type of piece
            ['bR','bN','bB','bQ','bK','bB','bN','bR'], # row black
            ["bp","bp","bp","bp","bp","bp","bp","bp"], #pawn row black
            ['--','--','--','--','--','--','--','--'],
            ['--','--','--','--','--','--','--','--'],
            ['--','--','--','--','--','--','--','--'],
            ['--','--','--','--','--','--','--','--'],
            ['wp','wp','wp','wp','wp','wp','wp','wp'],
            ['wR','wN','wB','wQ','wK','wB','wN','wR'],
        ]
        self.whiteToMove = True
        self.moveLog = []

    # takes a move as a parameter and executes it (will not work for castling, en passant en pawn promotion
    def makeMove(self, move):
        self.board[move.startRow][move.startRow] = '--'
        self.board[move.endRow][move.endCol] = move.pieceMoved
        self.moveLog.append(move) #log the move (so we can undo it later), or reply game in history
        self.whiteToMove = not self.whiteToMove #switch turns

    def undoMove(self):
        if len(self.moveLog) != 0: #make sure there is a move to undo
            move= self.moveLog.pop()
            self.board[move.startRow][move.startCol] = move.pieceMoved
            self.board[move.endRow][move.endCol] = move.pieceCaptured
            self.whiteToMove = not self.whiteToMove #switch turns

class Move():
    #maps keys to values
    # key : value
    ranksToRows = {'1':7,'2':6,'3':5,'4':4, '5':3,'6':2,'7':1,'8':0}
    rowsToRanks = {v : k for k,v in ranksToRows.items()}
    filesToCols = {'a':0,'b':1,'c':2,'d':3,'e':4,'f':5,'g':6,'h':7}
    colsToFiles = { v : k for k,v in filesToCols.items()}

    def __init__(self,startSq,endSq,board):
        self.startRow = startSq[0]
        self.startCol = startSq[1]
        self.endRow = endSq[0]
        self.endCol = endSq[1]
        self.pieceMoved = board[self.startRow][self.startCol]
        self.pieceCaptured = board[self.endRow][self.endCol]

    def getChessNotation(self):
        return self.getRankFile(self.startRow,self.startCol) + self.getRankFile(self.endRow,self.endCol)

    def getRankFile(self,r ,c):
        return self.colsToFiles[c] + self.rowsToRanks[r]

        
