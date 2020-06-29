


import pygame
import sys


pygame.init()

class Piece:
    def __init__(self, x_pos, y_pos):
      self.x = x_pos
      self.y = y_pos

class Square:
    def __init__(self, p_iece):
      self.piece = p_iece



class Board:
    def __init__(self, pieces):
      self.pieces = pieces
    def draw_board(self):
        for i in range(len(array)):
            for j in range(len(a[i])):



board = [[0] * 8] * 8


WIDTH = 800
HEIGHT = 800
bKnight = pygame.image.load('bknight.png')
bRook = pygame.image.load('brook.png')
bBishop = pygame.image.load('bbishop.png')
bKing = pygame.image.load('bking.png')
bQueen = pygame.image.load('bqueen.png')
bPawn = pygame.image.load('bpawn.png')

wKnight = pygame.image.load('wknight.png')
wRook = pygame.image.load('wrook.png')
wBishop = pygame.image.load('wbishop.png')
wKing = pygame.image.load('wking.png')
wQueen = pygame.image.load('wqueen.png')
wPawn = pygame.image.load('wpawn.png')


screen = pygame.display.set_mode((WIDTH, HEIGHT))

board = board()

end_chess = False;
pawn = Piece(50, 50)
while not end_chess:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        sys.exit()

    for x in range(8):
      for y in range(8):
        if (((x + y) % 2) == 0):
            pygame.draw.rect(screen, (105,42,42), (x * 100, y * 100, 100, 100))
        else:
            pygame.draw.rect(screen, (255,255,255), (x * 100, y * 100, 100, 100))


    screen.blit(bRook, (0, 0))
    screen.blit(bKnight, (100, 0))
    screen.blit(bBishop, (200, 0))
    screen.blit(bKing, (300, 0))
    screen.blit(bQueen, (400, 0))
    screen.blit(bBishop, (500, 0))
    screen.blit(bKnight, (600, 0))
    screen.blit(bRook, (700, 0))

    screen.blit(bPawn, (0, 100))
    screen.blit(bPawn, (100, 100))
    screen.blit(bPawn, (200, 100))
    screen.blit(bPawn, (300, 100))
    screen.blit(bPawn, (400, 100))
    screen.blit(bPawn, (500, 100))
    screen.blit(bPawn, (600, 100))
    screen.blit(bPawn, (700, 100))


    screen.blit(wRook, (0, 700))
    screen.blit(wKnight, (100, 700))
    screen.blit(wBishop, (200, 700))
    screen.blit(wKing, (300, 700))
    screen.blit(wQueen, (400, 700))
    screen.blit(wBishop, (500, 700))
    screen.blit(wKnight, (600, 700))
    screen.blit(wRook, (700, 700))

    screen.blit(wPawn, (0, 600))
    screen.blit(wPawn, (100, 600))
    screen.blit(wPawn, (200, 600))
    screen.blit(wPawn, (300, 600))
    screen.blit(wPawn, (400, 600))
    screen.blit(wPawn, (500, 600))
    screen.blit(wPawn, (600, 600))
    screen.blit(wPawn, (700, 600))

    pygame.display.update()




# Screen setup

