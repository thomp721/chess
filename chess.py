


import pygame
import sys


pygame.init()



#list = ['R', 'N', 'B', 'K', 'Q', 'B', 'N', 'R', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'WP', 'WP', 'WP', 'WP', 'WP', 'WP', 'WP', 'WP', 'WR', 'WN', 'WB', 'WK', 'WQ', 'WB', 'WN', 'WR']
class Piece:
    def __init__(self, index, color, typ):
      self.index = index
      self.color = color
      self.typ = typ

    def get_index(self):
      return self.index

    def set_index(self, new_index):
      self.index = new_index

    def get_type(self):
      return self.typ

    def get_color(self):
      return self.color

    def valid_move(self, new_index):
      return 0

    def move(self, new_index):
      ret = self.valid_move(new_index)
      if (ret == 0):
        return 0
      list[new_index] = list[self.index]
      list[self.index] = 'E'
      self.index = new_index

class Pawn(Piece):
    moved = 0
    def __init__(self, index, color, typ):
      super(Pawn, self).__init__(index, color, typ)

    def pawn_moved(self):
        self.moved = 1

    def valid_move(self, new_index):
      if (new_index < 0):
        return 0
      if (self.color == "white"):
        if ((new_index != self.index - 8) & (new_index != self.index - 16)):
          if ((new_index != self.index - 7) & (new_index != self.index - 9)):
            return 0
          if (list[new_index] == 'E'):
            return 0
          if (list[new_index].get_color() == "black"):
            self.pawn_moved()
            return 1
          return 0


        if (self.moved == 1):
          if (new_index == (self.index - 16)):
            return 0
          if (list[new_index] == 'E'):
            self.pawn_moved()
            return 1
          else:
            return 0
        else:
          if (new_index == (self.index - 16)):
            if ((list[self.index - 8] == 'E') & (list[self.index - 16] == 'E')):
              self.pawn_moved()
              return 1
            else:
              return 0
          else:
            if (list[new_index] == 'E'):
              self.pawn_moved()
              return 1
            else:
              return 0
      if (self.color == "black"):
        if ((new_index != self.index + 8) & (new_index != self.index + 16)):
          if ((new_index != self.index + 7) & (new_index != self.index + 9)):
            return 0
          if (list[new_index] == 'E'):
            return 0
          if (list[new_index].get_color() == "white"):
            self.pawn_moved()
            return 1
          return 0


        if (self.moved == 1):
          if (new_index == (self.index + 16)):
            return 0
          if (list[new_index] == 'E'):
            self.pawn_moved()
            return 1
          else:
            return 0
        else:
          if (new_index == (self.index + 16)):
            if ((list[self.index + 8] == 'E') & (list[self.index + 16] == 'E')):
              self.pawn_moved()
              return 1
            else:
              return 0
          else:
            if (list[new_index] == 'E'):
              self.pawn_moved()
              return 1
            else:
              return 0
      return 0

class Rook(Piece):
    typ = 'R'
    moved = 0
    def __init__(self, index, color, typ):
      super(Rook, self).__init__(index, color, typ)

    def valid_move(self, new_index):
      if (new_index < 0):
        return 0
      blocked = 0
      if (((new_index - self.index) % 8) == 0):
        print(self.index)
        print(new_index)
        if (new_index > self.index):
          for x in range(self.index + 8, new_index, 8):
            print(x)
            if (list[x] != 'E'):
              blocked = 1
        if (new_index < self.index):
          for x in range(self.index - 8, new_index, -8):
            print(x)
            if (list[x] != 'E'):
              blocked = 1
        if (blocked == 1):
          return 0
        if (list[new_index] == 'E'):
          return 1
        if (list[new_index].get_color() == self.get_color()):
          return 0
        return 1
      zero_index = self.index - (self.index % 8)
      print(zero_index)
      horizontal = 0
      for x in range(zero_index, zero_index + 8):
        if (x == new_index):
          horizontal = 1
      if (horizontal != 1):
        return 0
      if (self.index < new_index):
        for x in range(self.index + 1, new_index):
          if (list[x] != 'E'):
            blocked = 1
      if (self.index > new_index):
        for x in range(self.index - 1, new_index, -1):
          if (list[x] != 'E'):
            blocked = 1
      if (blocked == 1):
        print("blocked?")
        return 0
      if (list[new_index] == 'E'):
        return 1
      if (list[new_index].get_color() == self.get_color()):
        return 0
      return 1


class Knight(Piece):
    typ = 'N'
    moved = 0
    def __init__(self, index, color, typ):
      super(Knight, self).__init__(index, color, typ)
    def valid_move(self, new_index):
      placeholder = self.index - 17
      valid = 0
      if (new_index == placeholder):
        valid = 1
      placeholder += 2
      if (new_index == placeholder):
        valid = 1
      placeholder += 5
      if (new_index == placeholder):
        valid = 1
      placeholder += 4
      if (new_index == placeholder):
        valid = 1
      placeholder += 12
      if (new_index == placeholder):
        valid = 1
      placeholder += 4
      if (new_index == placeholder):
        valid = 1
      placeholder += 5
      if (new_index == placeholder):
        valid = 1
      placeholder += 2
      if (new_index == placeholder):
        valid = 1
      if (valid == 0):
        return 0
      if (list[new_index] == 'E'):
        return 1
      if (list[new_index].get_color() == self.color):
        return 0
      return 1


class Bishop(Piece):
    typ = 'B'
    moved = 0
    def __init__(self, index, color, typ):
      super(Bishop, self).__init__(index, color, typ)
    def valid_move(self, new_index):
      if (new_index < 0):
        return 0
      blocked = 0
      if ((((new_index - self.index) % 9) == 0)):
        print(self.index)
        print(new_index)
        if (new_index > self.index):
          for x in range(self.index + 9, new_index, 9):
            print(x)
            if (list[x] != 'E'):
              blocked = 1
        if (new_index < self.index):
          for x in range(self.index - 9, new_index, -9):
            print(x)
            if (list[x] != 'E'):
              blocked = 1
        if (blocked == 1):
          return 0
        if (list[new_index] == 'E'):
          return 1
        if (list[new_index].get_color() == self.get_color()):
          return 0
        return 1
      if ((((new_index - self.index) % 7) == 0)):
        print(self.index)
        print(new_index)
        if (new_index > self.index):
          for x in range(self.index + 7, new_index, 7):
            print(x)
            if (list[x] != 'E'):
              blocked = 1
        if (new_index < self.index):
          for x in range(self.index - 7, new_index, -7):
            print(x)
            if (list[x] != 'E'):
              blocked = 1
        if (blocked == 1):
          return 0
        if (list[new_index] == 'E'):
          return 1
        if (list[new_index].get_color() == self.get_color()):
          return 0
        return 1
      return 0

class Queen(Piece):
    typ = 'Q'
    moved = 0
    def __init__(self, index, color, typ):
      super(Queen, self).__init__(index, color, typ)
    def valid_move(self, new_index):
      if (new_index < 0):
        return 0
      blocked = 0
      if ((((new_index - self.index) % 9) == 0)):
        print(self.index)
        print(new_index)
        if (new_index > self.index):
          for x in range(self.index + 9, new_index, 9):
            print(x)
            if (list[x] != 'E'):
              blocked = 1
        if (new_index < self.index):
          for x in range(self.index - 9, new_index, -9):
            print(x)
            if (list[x] != 'E'):
              blocked = 1
        if (blocked == 1):
          return 0
        if (list[new_index] == 'E'):
          return 1
        if (list[new_index].get_color() == self.get_color()):
          return 0
        return 1
      if ((((new_index - self.index) % 7) == 0)):
        print(self.index)
        print(new_index)
        if (new_index > self.index):
          for x in range(self.index + 7, new_index, 7):
            print(x)
            if (list[x] != 'E'):
              blocked = 1
        if (new_index < self.index):
          for x in range(self.index - 7, new_index, -7):
            print(x)
            if (list[x] != 'E'):
              blocked = 1
        if (blocked == 1):
          return 0
        if (list[new_index] == 'E'):
          return 1
        if (list[new_index].get_color() == self.get_color()):
          return 0
        return 1
      if (new_index < 0):
        return 0
      blocked = 0
      if (((new_index - self.index) % 8) == 0):
        print(self.index)
        print(new_index)
        if (new_index > self.index):
          for x in range(self.index + 8, new_index, 8):
            print(x)
            if (list[x] != 'E'):
              blocked = 1
        if (new_index < self.index):
          for x in range(self.index - 8, new_index, -8):
            print(x)
            if (list[x] != 'E'):
              blocked = 1
        if (blocked == 1):
          return 0
        if (list[new_index] == 'E'):
          return 1
        if (list[new_index].get_color() == self.get_color()):
          return 0
        return 1
      zero_index = self.index - (self.index % 8)
      print(zero_index)
      horizontal = 0
      for x in range(zero_index, zero_index + 8):
        if (x == new_index):
          horizontal = 1
      if (horizontal != 1):
        return 0
      if (self.index < new_index):
        for x in range(self.index + 1, new_index):
          if (list[x] != 'E'):
            blocked = 1
      if (self.index > new_index):
        for x in range(self.index - 1, new_index, -1):
          if (list[x] != 'E'):
            blocked = 1
      if (blocked == 1):
        print("blocked?")
        return 0
      if (list[new_index] == 'E'):
        return 1
      if (list[new_index].get_color() == self.get_color()):
        return 0
      return 1
class King(Piece):
    typ = 'K'
    moved = 0
    def __init__(self, index, color, typ):
      super(King, self).__init__(index, color, typ)
    def valid_move(self, new_index):
      placeholder = self.index - 9
      valid = 0
      if (new_index == placeholder):
        valid = 1
      placeholder += 1
      if (new_index == placeholder):
        valid = 1
      placeholder += 1
      if (new_index == placeholder):
        valid = 1
      placeholder += 6
      if (new_index == placeholder):
        valid = 1
      placeholder += 2
      if (new_index == placeholder):
        valid = 1
      placeholder += 6
      if (new_index == placeholder):
        valid = 1
      placeholder += 1
      if (new_index == placeholder):
        valid = 1
      placeholder += 1
      if (new_index == placeholder):
        valid = 1
      if (valid == 0):
        return 0
      if (list[new_index] == 'E'):
        return 1
      if (list[new_index].get_color() == self.color):
        return 0
      return 1
"""




class Square:
    def __init__(self, p_iece):
      self.piece = p_iece




class Board:
    def __init__(self, squ_ares):
      self.square = squ_ares
    #def draw_board(self):
        #for i in range(len(array)):
          #for j in range(len(a[i])):

"""


print ("initial list: " + str(list))

#board = [[0] * 8] * 8


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
squares = []

empty = Piece(-1, "black", 'E')

br1 = Rook(0, "black", 'R')
bn1 = Knight(1, "black", 'N')
bb1 = Bishop(2, "black", 'B')
bq  = Queen(3, "black", 'Q')
bk  = King(4, "black", 'K')
bb2 = Bishop(5, "black", 'B')
bn2 = Knight(6, "black", 'N')
br2 = Rook(7, "black", 'R')

bp1 = Pawn(8, "black", 'P')
bp2 = Pawn(9, "black", 'P')
bp3 = Pawn(10, "black", 'P')
bp4 = Pawn(11, "black", 'P')
bp5 = Pawn(12, "black", 'P')
bp6 = Pawn(13, "black", 'P')
bp7 = Pawn(14, "black", 'P')
bp8 = Pawn(15, "black", 'P')


wp1 = Pawn(48, "white", 'WP')
wp2 = Pawn(49, "white", 'WP')
wp3 = Pawn(50, "white", 'WP')
wp4 = Pawn(51, "white", 'WP')
wp5 = Pawn(52, "white", 'WP')
wp6 = Pawn(53, "white", 'WP')
wp7 = Pawn(54, "white", 'WP')
wp8 = Pawn(55, "white", 'WP')

wr1 = Rook(56, "white", 'WR')
wn1 = Knight(57, "white", 'WN')
wb1 = Bishop(58, "white", 'WB')
wq  = Queen(59, "white", 'WQ')
wk  = King(60, "white", 'WK')
wb2 = Bishop(61, "white", 'WB')
wn2 = Knight(62, "white", 'WN')
wr2 = Rook(63, "white", 'WR')

list = [br1, bn1, bb1, bq, bk, bb2, bn2, br2, bp1, bp2, bp3, bp4, bp5, bp6, bp7, bp8, 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', wp1, wp2, wp3, wp4, wp5, wp6, wp7, wp8, wr1, wn1, wb1, wq, wk, wb2, wn2, wr2]

draw_list = [br1, bn1, bb1, bq, bk, bb2, bn2, br2, bp1, bp2, bp3, bp4, bp5, bp6, bp7, bp8, 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', wp1, wp2, wp3, wp4, wp5, wp6, wp7, wp8, wr1, wn1, wb1, wq, wk, wb2, wn2, wr2]


end_chess = False;

index1 = -1
index2 = -1


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
    temp = 'P'

  for i in range(8):
    for j in range(8):
      temp = list[((i * 8) + j)]
      if (temp != 'E'):
        temp = list[((i * 8) + j)].get_type()
        if (temp == 'P'):
          screen.blit(bPawn, (j * 100, i * 100))
        if (temp == 'R'):
          screen.blit(bRook, (j * 100, i * 100))
        if (temp == 'N'):
          screen.blit(bKnight, (j * 100, i * 100))
        if (temp == 'B'):
          screen.blit(bBishop, (j * 100, i * 100))
        if (temp == 'K'):
          screen.blit(bKing, (j * 100, i * 100))
        if (temp == 'Q'):
          screen.blit(bQueen, (j * 100, i * 100))
        if (temp == 'WP'):
          screen.blit(wPawn, (j * 100, i * 100))
        if (temp == 'WR'):
          screen.blit(wRook, (j * 100, i * 100))
        if (temp == 'WN'):
          screen.blit(wKnight, (j * 100, i * 100))
        if (temp == 'WB'):
          screen.blit(wBishop, (j * 100, i * 100))
        if (temp == 'WK'):
          screen.blit(wKing, (j * 100, i * 100))
        if (temp == 'WQ'):
          screen.blit(wQueen, (j * 100, i * 100))


  if event.type == pygame.MOUSEBUTTONUP:
    x, y = pygame.mouse.get_pos()
    index = int((x / 100)) + int(((int(y / 100) / 1) * 8))


    if (index1 == -1):
      if (list[index] != 'E'):
        index1 = index
    elif ((index != index1) & (index2 == -1)):
      index2 = index

    if ((index1 != index2) & (index2 != -1)):
      list[index1].move(index2)
      index1 = -1
      index2 = -1







  pygame.display.update()

# Screen setup
