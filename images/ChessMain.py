# this is our main driver file
#handling user input
# desplaying current game state object

import pygame as p
from images import ChessEngine

WIDTH = 512
HEIGHT = 512
DIMENSION = 8
SQ_SIZE = HEIGHT // DIMENSION #square size
MAX_FPS = 15 #frames per second
IMAGES = {}

'''
Initialse a global dictionairy of images , this will be called exactly once
'''
def loadImages():
    pieces = ['wp','wR','wN','wB','wK','wQ', 'bp', 'bR', 'bN', 'bB','bK','bQ']
    for piece in pieces:
        IMAGES[piece] = p.transform.scale(p.image.load('images/' + piece + '.png'),(SQ_SIZE,SQ_SIZE))
    # we can acces an image by saying fe  IMAGES['wp']

'''
the main driver for our code, this will handle user input and updating the graphics
'''
def main():
    p.init()
    screen = p.display.set_mode((WIDTH,HEIGHT))
    clock = p.time.Clock()
    screen.fill(p.Color("white"))
    gs = ChessEngine.GameState()
    #print(gs.board)
    loadImages() #only do this once, before the while loop
    running=True
    sqSelected = () #keep track of the last click of the user
    playerClicks = [] # keeps track of player clicks, fe row6column4, to row7column5
    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False
            elif e.type ==p.MOUSEBUTTONDOWN:
                location = p.mouse.get_pos() #x,y coordinates of mouse
                col = location[0]//SQ_SIZE
                row = location[1]//SQ_SIZE
                if sqSelected == (row,col): #use clicked same square twice ,exception, do nothing here
                    sqSelected = () #deselect
                    playerClicks = [] #clear player clicks
                else:
                    sqSelected= (row,col)
                    playerClicks.append(sqSelected) #append of for 1st e 2nd click
                    #was that the user second click?
                if len(playerClicks) == 2:
                        # after second click so -> make a move with a piece
                        move = ChessEngine.Move(playerClicks[0],playerClicks[1],gs.board)
                        print(move.getChessNotation())
                        gs.makeMove(move)
                        sqSelected = () # reset user clicks
                        playerClicks = []

                #key handlers
                

            drawGameState(screen,gs)
            clock.tick(MAX_FPS)
            p.display.flip()


#responsible for all the graphics in the current gamestate
def drawGameState(screen, gs):
    drawBoard(screen) #draw squares on the board
    # add in pieces highlights etc later
    drawPieces(screen,gs.board) #draw pieces on top of the squares

#draw squares on the board (top left square is always white)
def drawBoard(screen):
    colors= [p.Color('white'),p.Color('gray')]
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            color = colors[((r+c) % 2)]
            p.draw.rect(screen,color,p.Rect(c*SQ_SIZE, r*SQ_SIZE,SQ_SIZE,SQ_SIZE))



#draw pieces on the board using current gamestate.board variable
def drawPieces(screen,board):
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            piece = board[r][c]
            if piece != '--': #is not an empty square
                screen.blit(IMAGES[piece],p.Rect(c*SQ_SIZE, r*SQ_SIZE,SQ_SIZE,SQ_SIZE))




if __name__ == "__main__":
    main()