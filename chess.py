


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

    def set_type(self, new_type):
      self.typ = new_type


    def get_type(self):
      return self.typ

    def get_color(self):
      return self.color

    def valid_move(self, new_index):
      return 0

    def in_checkk(self, index_1, index_2, color):

      check = 0
      moved = 0
      print("index 1:")
      print(index_1)
      print("index 2:")
      print(index_2)
      for y in range(index_1, index_2):
        for x in range(len(list)):
          if (list[x] != 'E'):
            moved = list[x].moved
            if ((list[x].valid_move(y) != 0) & (list[x].color != color)):
              print("x that worked:")
              print(x)
              print("y that worked:")
              print(y)
              print("in the chekc thing?")
              check = 1
            list[x].moved = moved
      if (check == 1):
        if (self.typ == 'WK'):
          self.typ = 'WKC'
        if (self.typ == 'K'):
          self.typ = 'KC'
      else:
        if (self.typ == 'WKC'):
          self.typ = 'WK'
        if (self.typ == 'KC'):
          self.typ = 'K'
      return check

    def move(self, new_index):
      #does en passant stuff
      global noo_index
      noo_index = new_index
      print("start")
      if (turn == "white"):
        for x in range(len(list)):
          if (list[x] != 'E'):
            if (list[x].typ == 'WP'):
              list[x].first_two_mov()
      else:
        for x in range(len(list)):
          if (list[x] != 'E'):
            if (list[x].typ == 'P'):
              list[x].first_two_mov()

      #checks if move is valid
      ret = self.valid_move(new_index)
      bet = ret
      if (ret == 0):
        print("its returning in here ///")
        return 0
      global promote
      global pro_index
      global pro_color

      if ((self.typ == 'P') | (self.typ == 'WP')):
        if (self.typ == 'P'):
          if (new_index > 55):
            promote = True
            pro_index = new_index
            pro_color = self.color
        else:
          if (new_index < 8):
           promote = True
           pro_index = new_index
           pro_color = self.color

      #covers castling with king moving to the right
      if (ret == 2):

        old_index = self.index
        for x in range(old_index, old_index + 7):
          rook_index = x
          if (list[x] != 'E'):
            if ((list[x].typ == 'R') | (list[x].typ == 'WR')):
              break
        checkk = self.in_checkk(self.index, rook_index, self.color)
        if (checkk == 1):
          return 0
        if (list[rook_index].moved != 0):
          return 0
        if (list[self.index].moved != 0):
          return 0
        list[new_index - 1] = list[self.index]
        list[new_index - 2] = 'E'
        if (list[new_index - 1].in_check() == 1):
          list[new_index - 2] = list[new_index - 1]
          list[new_index - 1] = 'E'
          return 0
        list[new_index - 2] = list[new_index - 1]
        list[new_index - 1] = 'E'
        list[new_index] = list[self.index]
        list[old_index] = 'E'

        if (list[new_index].in_check() == 1):
          list[new_index - 2] = list[new_index]
          list[new_index] = 'E'
          return 0
        list[new_index - 2] = list[new_index]
        list[new_index] = 'E'
        rook_index = 0
        for x in range(old_index, old_index + 7):
          rook_index = x
          if (list[x] != 'E'):
            if ((list[x].typ == 'R') | (list[x].typ == 'WR')):
              break
        list[new_index - 1] = list[rook_index]
        list[new_index - 1].index = new_index - 1
        self.index = new_index
        list[new_index] = list[new_index - 2]
        list[new_index - 2] = 'E'

        list[new_index].index = new_index
        list[new_index - 1].has_moved()
        list[rook_index] = 'E'


      #covers castling with king moving to the left
      if (ret == 3):
        old_index = self.index
        for x in range(old_index, old_index - 7, -1):
          rook_index = x
          if (list[x] != 'E'):
            if ((list[x].typ == 'R') | (list[x].typ == 'WR')):
              break
        checkk = self.in_checkk(rook_index, self.index, self.color)
        if (checkk == 1):
          return 0
        if (list[rook_index].moved != 0):
          return 0
        if (list[self.index].moved != 0):
          return 0
        list[new_index + 1] = list[self.index]
        list[new_index + 2] = 'E'
        if (list[new_index + 1].in_check() == 1):
          list[new_index + 2] = list[new_index + 1]
          list[new_index + 1] = 'E'
          return 0
        list[new_index + 2] = list[new_index + 1]
        list[new_index + 1] = 'E'

        list[new_index] = list[self.index]
        list[old_index] = 'E'
        if (list[new_index].in_check() == 1):
          list[new_index + 2] = list[new_index]
          list[new_index] = 'E'
          return 0
        list[new_index + 2] = list[new_index]
        list[new_index] = 'E'
        rook_index = 0
        for x in range(old_index, old_index - 7, -1):
          rook_index = x
          if (list[x] != 'E'):
            if ((list[x].typ == 'R') | (list[x].typ == 'WR')):
              break
        list[new_index + 1] = list[rook_index]
        list[new_index + 1].index = new_index + 1
        self.index = new_index
        list[new_index] = list[new_index + 2]
        list[new_index + 2] = 'E'

        list[new_index].index = new_index
        list[new_index + 1].has_moved()
        list[rook_index] = 'E'


      #checks for check
      if ((ret != 2) & (ret != 3)):
        placeholder = list[new_index]
        placeholder_index = self.index
        list[new_index] = list[self.index]
        list[self.index] = 'E'
        self.index = new_index
      else:
        if (turn == "white"):
           for x in range(len(list)):
             if (list[x] != 'E'):
               if ((list[x].typ == 'K') | (list[x].typ == 'KC')):
                 ret = x
           list[ret].in_check()
        else:
          for x in range(len(list)):
            if (list[x] != 'E'):
              if ((list[x].typ == 'WK') | (list[x].typ == 'WKC')):
                ret = x
          list[ret].in_check()
        return 1



      if (turn == "white"):
        for x in range(len(list)):
          if (list[x] != 'E'):
            if ((list[x].typ == 'WK') | (list[x].typ == 'WKC')):
              ret = x
        #checks if a check happens, and if so undoes the move and its effects
        if (list[ret].in_check() == 1):
          list[placeholder_index] = list[self.index]
          list[self.index] = placeholder
          self.index = placeholder_index
          for x in range(len(list)):
            if (list[x] != 'E'):
              if ((list[x].typ == 'WP') | (list[x].typ == 'P') | (list[x].typ == 'WR') | (list[x].typ == 'R') | (list[x].typ == 'WK') | (list[x].typ == 'K')):
                if (list[x].moved == 1):
                  list[x].moved = 0
                if (list[x].typ == 'WP'):
                  if (list[x].first_two_move == 1):
                    list[x].first_two_move = 0
          if (bet == 2):
            list[rook_index] = list[new_index - 1]
            list[new_index - 1] = 'E'
          if (bet == 3):
            list[rook_index] = list[new_index + 1]
            list[new_index + 1] = 'E'
          return 0

        for x in range(len(list)):
          if (list[x] != 'E'):
            if ((list[x].typ == 'K') | (list[x].typ == 'KC')):
              ret = x
        list[ret].in_check()

      else:
        for x in range(len(list)):
          if (list[x] != 'E'):
            if ((list[x].typ == 'K')  | (list[x].typ == 'KC')):
              ret = x
        if (list[ret].in_check() == 1):
          list[placeholder_index] = list[self.index]
          list[self.index] = placeholder
          self.index = placeholder_index
          for x in range(len(list)):
            if (list[x] != 'E'):
              if ((list[x].typ == 'WP') | (list[x].typ == 'P') | (list[x].typ == 'WR') | (list[x].typ == 'R') | (list[x].typ == 'WK') | (list[x].typ == 'K')):
                if (list[x].moved == 1):
                  list[x].moved = 0
                if (list[x].typ == 'P'):
                  if (list[x].first_two_move == 1):
                    list[x].first_two_move = 0
            if (bet == 2):
              list[rook_index] = list[new_index - 1]
              list[new_index - 1] = 'E'
            if (bet == 3):
              list[rook_index] = list[new_index + 1]
              list[new_index + 1] = 'E'
            return 0
        for x in range(len(list)):
          if (list[x] != 'E'):
            if ((list[x].typ == 'WK') | (list[x].typ == 'WKC')):
              ret = x
        list[ret].in_check()
      print("end")
      if ((self.typ == 'P') | (self.typ == 'WP')):
        self.has_moved()

      return 1


class Pawn(Piece):
    moved = 0
    first_two_move = 0
    def __init__(self, index, color, typ):
      super(Pawn, self).__init__(index, color, typ)

    def has_moved(self):
        print("pawn moved")
        if (self.moved == 1):
          self.moved = 2
        else:
          self.moved = 1

    def first_two_mov(self):
        print("got in hererer")
        if (self.first_two_move == 1):
          self.first_two_move = 2
        print(self.first_two_move)
    def valid_move(self, new_index):
      ret = 0

      if (new_index < 0):
        return 0

      if (self.color == "white"):
        if ((new_index != self.index - 8) & (new_index != self.index - 16)):
          if ((new_index != self.index - 7) & (new_index != self.index - 9)):
            return 0
          if ((self.index % 8) == 0):
            if (new_index == (self.index - 9)):
              return 0
          if ((self.index % 8) == 7):
            if (new_index == (self.index - 7)):
              return 0
          if (list[new_index + 8] != 'E'):
            if (list[new_index + 8].typ == 'P'):
              if (list[new_index + 8].first_two_move == 1):
                list[new_index + 8] = 'E'
                return 1
          if (list[new_index] == 'E'):
            return 0
          if (list[new_index].get_color() == "black"):
            return 1
          return 0

        if (self.moved == 1):
          if (new_index == (self.index - 16)):
            return 0
          if (list[new_index] == 'E'):
            return 1
          else:
            return 0
        else:
          if (new_index == (self.index - 16)):
            if ((list[self.index - 8] == 'E') & (list[self.index - 16] == 'E')):
              self.first_two_move = 1
              return 1
            else:
              return 0
          else:
            if (list[new_index] == 'E'):
              return 1
            else:
              return 0
      if (self.color == "black"):
        if ((new_index != self.index + 8) & (new_index != self.index + 16)):
          if ((new_index != self.index + 7) & (new_index != self.index + 9)):
            return 0
          if ((self.index % 8) == 0):
            if (new_index == (self.index + 7)):
              return 0
          if ((self.index % 8) == 7):
            if (new_index == (self.index + 9)):
              return 0
          if (list[new_index - 8] != 'E'):
            if (list[new_index - 8].typ == 'WP'):
              if (list[new_index - 8].first_two_move == 1):
                list[new_index - 8] = 'E'
                return 1
          if (list[new_index] == 'E'):
            return 0
          if (list[new_index].get_color() == "white"):
            return 1
          return 0


        if (self.moved == 1):
          if (new_index == (self.index + 16)):
            return 0
          if (list[new_index] == 'E'):
            return 1
          else:
            return 0
        else:
          if (new_index == (self.index + 16)):
            if ((list[self.index + 8] == 'E') & (list[self.index + 16] == 'E')):
              self.first_two_move = 1
              return 1
            else:
              return 0
          else:
            if (list[new_index] == 'E'):
              return 1
            else:
              return 0
      return 0

    def draw(self):
      y = int(self.index / 8)
      x = int(self.index % 8)
      #draws white
      if (self.typ == 'WP'):
        screen.blit(wPawn, (x * 100, y * 100))
      #draws black
      if (self.typ == 'P'):
        screen.blit(bPawn, (x * 100, y * 100))
      #draws highlighted white
      if (self.typ == 'BLP'):
        screen.blit(blPawn, (x * 100, y * 100))
      #draws highlighted black
      if (self.typ == 'GP'):
        screen.blit(gPawn, (x * 100, y * 100))

    def change_light(self):
      if (self.typ == 'WP'):
        self.set_type('BLP')
        return
      if (self.typ == 'BLP'):
        self.typ = 'WP'
        return
      if (self.typ == 'P'):
        self.typ = 'GP'
        return
      if (self.typ == 'GP'):
        self.typ = 'P'
        return

class Rook(Piece):
    typ = 'R'
    moved = 0
    def __init__(self, index, color, typ):
      super(Rook, self).__init__(index, color, typ)

    def has_moved(self):
      if (self.moved == 1):
        self.moved = 2
      else:
        self.moved = 1


    def valid_move(self, new_index):
      if (new_index < 0):
        return 0
      blocked = 0
      if (((new_index - self.index) % 8) == 0):
        if (new_index > self.index):
          for x in range(self.index + 8, new_index, 8):
            if (list[x] != 'E'):
              blocked = 1
        if (new_index < self.index):
          for x in range(self.index - 8, new_index, -8):
            if (list[x] != 'E'):
              blocked = 1
        if (blocked == 1):
          return 0
        if (list[new_index] == 'E'):
          self.has_moved()
          return 1
        if (list[new_index].get_color() == self.get_color()):
          return 0
        self.has_moved()
        return 1
      zero_index = self.index - (self.index % 8)
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
        return 0
      if (list[new_index] == 'E'):
        self.has_moved()
        return 1
      if (list[new_index].get_color() == self.get_color()):
        return 0
      self.has_moved()
      return 1

    def draw(self):
      y = int(self.index / 8)
      x = int(self.index % 8)
      #draws white
      if (self.typ == 'WR'):
        screen.blit(wRook, (x * 100, y * 100))
      #draws black
      if (self.typ == 'R'):
        screen.blit(bRook, (x * 100, y * 100))
      #draws highlighted white
      if (self.typ == 'BLR'):
        screen.blit(blRook, (x * 100, y * 100))
      #draws highlighted black
      if (self.typ == 'GR'):
        screen.blit(gRook, (x * 100, y * 100))

    def change_light(self):
      if (self.typ == 'WR'):
        self.typ = 'BLR'
        return
      if (self.typ == 'BLR'):
        self.typ = 'WR'
        return
      if (self.typ == 'R'):
        self.typ = 'GR'
        return
      if (self.typ == 'GR'):
        self.typ = 'R'
        return


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

    def draw(self):
      y = int(self.index / 8)
      x = int(self.index % 8)
      #draws white
      if (self.typ == 'WN'):
        screen.blit(wKnight, (x * 100, y * 100))
      #draws black
      if (self.typ == 'N'):
        screen.blit(bKnight, (x * 100, y * 100))
      #draws highlighted white
      if (self.typ == 'BLN'):
        screen.blit(blKnight, (x * 100, y * 100))
      #draws highlighted black
      if (self.typ == 'GN'):
        screen.blit(gKnight, (x * 100, y * 100))

    def change_light(self):
      if (self.typ == 'WN'):
        self.typ = 'BLN'
        return
      if (self.typ == 'BLN'):
        self.typ = 'WN'
        return
      if (self.typ == 'N'):
        self.typ = 'GN'
        return
      if (self.typ == 'GN'):
        self.typ = 'N'
        return

class Bishop(Piece):
    typ = 'B'
    moved = 0
    def __init__(self, index, color, typ):
      super(Bishop, self).__init__(index, color, typ)
    def valid_move(self, new_index):
      x = int(self.index % 8)
      x_new = int(new_index % 8)
      y = int(self.index / 8)
      y_new = int(new_index / 8)
      if (new_index < 0):
        return 0
      blocked = 0
      if ((((new_index - self.index) % 9) == 0) & (((y_new > y) & (x_new > x)) | ((y_new < y) & (x_new < x)))):
        if (new_index > self.index):
          for x in range(self.index + 9, new_index, 9):
            if (list[x] != 'E'):
              blocked = 1
        if (new_index < self.index):
          for x in range(self.index - 9, new_index, -9):
            if (list[x] != 'E'):
              blocked = 1
        if (blocked == 1):
          return 0
        if (list[new_index] == 'E'):
          return 1
        if (list[new_index].get_color() == self.get_color()):
          return 0
        return 1
      if ((((new_index - self.index) % 7) == 0) & (((y_new < y) & (x_new > x)) | ((y_new > y) & (x_new < x)))):
        if (new_index > self.index):
          for x in range(self.index + 7, new_index, 7):
            if (list[x] != 'E'):
              blocked = 1
        if (new_index < self.index):
          for x in range(self.index - 7, new_index, -7):
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

    def draw(self):
      y = int(self.index / 8)
      x = int(self.index % 8)
      #draws white
      if (self.typ == 'WB'):
        screen.blit(wBishop, (x * 100, y * 100))
      #draws black
      if (self.typ == 'B'):
        screen.blit(bBishop, (x * 100, y * 100))
      #draws highlighted white
      if (self.typ == 'BLB'):
        screen.blit(blBishop, (x * 100, y * 100))
      #draws highlighted black
      if (self.typ == 'GB'):
        screen.blit(gBishop, (x * 100, y * 100))

    def change_light(self):
      if (self.typ == 'WB'):
        self.typ = 'BLB'
        return
      if (self.typ == 'BLB'):
        self.typ = 'WB'
        return
      if (self.typ == 'B'):
        self.typ = 'GB'
        return
      if (self.typ == 'GB'):
        self.typ = 'B'
        return

class Queen(Piece):
    typ = 'Q'
    moved = 0
    def __init__(self, index, color, typ):
      super(Queen, self).__init__(index, color, typ)
    def valid_move(self, new_index):
      x = int(self.index % 8)
      x_new = int(new_index % 8)
      y = int(self.index / 8)
      y_new = int(new_index / 8)
      if (new_index < 0):
        return 0
      blocked = 0
      if ((((new_index - self.index) % 9) == 0) & (((y_new > y) & (x_new > x)) | ((y_new < y) & (x_new < x)))):
        if (new_index > self.index):
          for x in range(self.index + 9, new_index, 9):
            if (list[x] != 'E'):
              blocked = 1
        if (new_index < self.index):
          for x in range(self.index - 9, new_index, -9):
            if (list[x] != 'E'):
              blocked = 1
        if (blocked == 1):
          return 0
        if (list[new_index] == 'E'):
          return 1
        if (list[new_index].get_color() == self.get_color()):
          return 0
        return 1
      if ((((new_index - self.index) % 7) == 0) & (((y_new < y) & (x_new > x)) | ((y_new > y) & (x_new < x)))):

        if (new_index > self.index):
          for x in range(self.index + 7, new_index, 7):
            if (list[x] != 'E'):
              blocked = 1
        if (new_index < self.index):
          for x in range(self.index - 7, new_index, -7):
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
        if (new_index > self.index):
          for x in range(self.index + 8, new_index, 8):
            if (list[x] != 'E'):
              blocked = 1
        if (new_index < self.index):
          for x in range(self.index - 8, new_index, -8):
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
        return 0
      if (list[new_index] == 'E'):
        return 1
      if (list[new_index].get_color() == self.get_color()):
        return 0
      return 1


    def draw(self):
      y = int(self.index / 8)
      x = int(self.index % 8)
      #draws white
      if (self.typ == 'WQ'):
        screen.blit(wQueen, (x * 100, y * 100))
      #draws black
      if (self.typ == 'Q'):
        screen.blit(bQueen, (x * 100, y * 100))
      #draws highlighted white
      if (self.typ == 'BLQ'):
        screen.blit(blQueen, (x * 100, y * 100))
      #draws highlighted black
      if (self.typ == 'GQ'):
        screen.blit(gQueen, (x * 100, y * 100))

    def change_light(self):
      if (self.typ == 'WQ'):
        self.typ = 'BLQ'
        return
      if (self.typ == 'BLQ'):
        self.typ = 'WQ'
        return
      if (self.typ == 'Q'):
        self.typ = 'GQ'
        return
      if (self.typ == 'GQ'):
        self.typ = 'Q'
        return

class King(Piece):
    typ = 'K'
    moved = 0

    def __init__(self, index, color, typ):
      super(King, self).__init__(index, color, typ)

    def has_moved(self):
      if (self.moved == 1):
        self.moved = 2
      else:
        self.moved = 1

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
  #castling checker
        if (self.color == "white"):
          if (new_index == (self.index + 2)):
            if (list[self.index + 3] != 'E'):
              if (list[self.index + 3].typ == 'WR'):
                if ((list[self.index + 3].moved == 0) & (list[self.index].moved == 0)):
                  for x in range(self.index + 1, new_index):
                    if (list[x] != 'E'):
                      return 0
                return 2
          if (new_index == (self.index - 2)):
            if (list[self.index - 4] != 'E'):
              if (list[self.index - 4].typ == 'WR'):
                if ((list[self.index - 4].moved == 0) & (list[self.index].moved == 0)):
                  for x in range(self.index - 1, new_index, -1):
                    if (list[x] != 'E'):
                      return 0
                return 3
        else:
          if (new_index == (self.index + 2)):
            if (list[self.index + 3] != 'E'):
              if (list[self.index + 3].typ == 'R'):
                if ((list[self.index + 3].moved == 0) & (list[self.index].moved == 0)):
                  for x in range(self.index + 1, new_index, 1):
                    if (list[x] != 'E'):
                      return 0
                  return 2
          if (new_index == (self.index - 2)):
            if (list[self.index - 4] != 'E'):
              if (list[self.index - 4].typ == 'R'):
                if ((list[self.index - 4].moved == 0) & (list[self.index].moved == 0)):
                  for x in range(self.index - 1, new_index, -1):
                    if (list[x] != 'E'):
                      return 0
                  return 3
        return 0
      if (list[new_index] == 'E'):
        self.has_moved()
        return 1
      if (list[new_index].get_color() == self.color):
        return 0
      return 1

    def draw(self):
      y = int(self.index / 8)
      x = int(self.index % 8)
      #draws white
      if (self.typ == 'WK'):
        screen.blit(wKing, (x * 100, y * 100))
      #draws black
      if (self.typ == 'K'):
        screen.blit(bKing, (x * 100, y * 100))
      #draws highlighted white
      if (self.typ == 'BLK'):
        screen.blit(blKing, (x * 100, y * 100))
      #draws highlighted black
      if (self.typ == 'GK'):
        screen.blit(gKing, (x * 100, y * 100))
      if (self.typ == 'WKC'):
        screen.blit(wKingCheck, (x * 100, y * 100))
      if (self.typ == 'KC'):
        screen.blit(bKingCheck, (x * 100, y * 100))
    def change_light(self):
      if (self.typ == 'WK'):
        self.typ = 'BLK'
        return
      if (self.typ == 'BLK'):
        self.typ = 'WK'
        return
      if (self.typ == 'K'):
        self.typ = 'GK'
        return
      if (self.typ == 'GK'):
        self.typ = 'K'
        return
    def in_check(self):
      check = 0
      global list
      list_2 = list.copy()
      for x in range(len(list)):
        if (list[x] != 'E'):
          if ((list[x].valid_move(self.index)) & (list[x].color != self.color)):
            check = 1
      if (check == 1):
        if (self.typ == 'WK'):
          self.typ = 'WKC'
        if (self.typ == 'K'):
          self.typ = 'KC'
      else:
        if (self.typ == 'WKC'):
          self.typ = 'WK'
        if (self.typ == 'KC'):
          self.typ = 'K'

      king_valid = 0
      king_index = self.index
      if (check == 1):
        for x in range(len(list)):
          if (list[self.index].valid_move(x) == 1):
            print("valid square:")
            print(x)
            king_valid = 1
            if (list[x] == 'E'):
              for y in range(len(list)):
                if (list[y] != 'E'):
                  if (list[y].color != self.color):
                    if (list[y].valid_move(x) != 0):
                      king_valid = 0
              if (king_valid == 1):
                king_valid = 2
            else:
              placeholder = list[x]
              list[x] = 'E'
              for y in range(len(list)):
                if (list[y] != 'E'):
                  if (list[y].color != self.color):
                    print("piece square")
                    print(y)
                    if (list[y].valid_move(x) != 0):
                      king_valid = 0
              list[x] = placeholder
              if (king_valid == 1):
                king_valid = 2
        if (king_valid == 2):
          check = 2
        king_valid = 0
        for x in range(self.index, 0, -8):
          for y in range(len(list)):
            if (list[y] != 'E'):
              if (list[y].color == self.color):
                if (list[y].valid_move(x)):
                  list[x] = list[y]
                  list[y] = 'E'
                  list[x].index = x
                  king_valid = 1
                  for z in range(len(list)):
                    if (list[z] != 'E'):
                      if (list[z].color != self.color):
                        if (list[z].valid_move(king_index) != 0):
                          print("this onee")
                          print("z:")
                          print(z)
                          king_valid = 0
                  list[y] = list[x]
                  list[x] = 'E'
                  list[y].index = y
                  if (king_valid == 1):
                    print("x wrong:")
                    print(x)
                    print("y wrong:")
                    print(y)
                    king_valid = 2
        if (king_valid == 2):
          check = 2
          print("the one actually fucked it up :/")
        king_valid = 0
        for x in range(self.index, len(list), 8):
          for y in range(len(list)):
            if (list[y] != 'E'):
              if (list[y].color == self.color):
                if (list[y].valid_move(x)):
                  list[x] = list[y]
                  list[y] = 'E'
                  list[x].index = x
                  if (self.in_checkk(self.index, self.index + 1, self.color) == 0):
                    print("y:")
                    print(y)
                    print("this twoo")
                    check = 2
                  list[y] = list[x]
                  list[x] = 'E'
                  list[y].index = y
        for x in range(self.index, 8 - (self.index - ((len(list) - self.index) % 8))):
          for y in range(len(list)):
            if (list[y] != 'E'):
              if (list[y].color == self.color):
                if (list[y].valid_move(x)):
                  list[x] = list[y]
                  list[y] = 'E'
                  list[x].index = x
                  if (self.in_checkk(self.index, self.index + 1, self.color) == 0):
                    print("this threee")
                    check = 2
                  list[y] = list[x]
                  list[x] = 'E'
                  list[y].index = y
        for x in range(self.index, self.index - ((len(list) - self.index) % 8), -1):
          for y in range(len(list)):
            if (list[y] != 'E'):
              if (list[y].color == self.color):
                if (list[y].valid_move(x)):
                  list[x] = list[y]
                  list[y] = 'E'
                  list[x].index = x
                  if (self.in_checkk(self.index, self.index + 1, self.color) == 0):
                    print("this fourrr")
                    check = 2
                  list[y] = list[x]
                  list[x] = 'E'
                  list[y].index = y
      if (check == 1):
        global checkmate
        checkmate = 1
      if (check != 0):
        check = 1
      list = list_2.copy()

      return check



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

blKnight = pygame.image.load('blknight.png')
blRook = pygame.image.load('blrook.png')
blBishop = pygame.image.load('blbishop.png')
blKing = pygame.image.load('blking.png')
blQueen = pygame.image.load('blqueen.png')
blPawn = pygame.image.load('blpawn.png')

gKnight = pygame.image.load('gknight.png')
gRook = pygame.image.load('grook.png')
gBishop = pygame.image.load('gbishop.png')
gKing = pygame.image.load('gking.png')
gQueen = pygame.image.load('gqueen.png')
gPawn = pygame.image.load('gpawn.png')

wKingCheck = pygame.image.load('wkingcheck.png')
bKingCheck = pygame.image.load('bkingcheck.png')

pScreen = pygame.image.load('promote screen.png')

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

#draw_list = [br1, bn1, bb1, bq, bk, bb2, bn2, br2, bp1, bp2, bp3, bp4, bp5, bp6, bp7, bp8, 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', wp1, wp2, wp3, wp4, wp5, wp6, wp7, wp8, wr1, wn1, wb1, wq, wk, wb2, wn2, wr2]

turn = "white"

valid_1 = 0

end_chess = False
promote = False
pro_index = -1
pro_color = "white"
checkmate = 0

index1 = -1
index2 = -1
noo_index = 0

while not end_chess:

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      sys.exit()

  if (checkmate == 1):
    pygame.time.wait(25)
    if (list[noo_index] != 'E'):
      if ((list[noo_index].typ == 'WKC') | (list[noo_index].typ == 'KC') | (list[noo_index].typ == 'WK') | (list[noo_index].typ == 'K')):
        checkmate = 0
    print("poop")

  if (promote == True):
    pygame.time.wait(250)
    screen.blit(pScreen, (75, 50))
    if event.type == pygame.MOUSEBUTTONDOWN:
      x, y = pygame.mouse.get_pos()
      print("x:")
      print(x)
      print("y:")
      print(y)
      if ((x >= 150) & (x <= 259)):
        if ((y >= 175) & (y <= 214)):
          if (pro_color == "black"):
            list[pro_index] = Queen(pro_index, pro_color, 'Q')
            promote = False
          else:
            list[pro_index] = Queen(pro_index, pro_color, 'WQ')
            promote = False
        if ((y >= 264) & (y <= 302)):
          if (pro_color == "black"):
            list[pro_index] = Rook(pro_index, pro_color, 'R')
            promote = False
          else:
            list[pro_index] = Rook(pro_index, pro_color, 'WR')
            promote = False
        if ((y >= 351) & (y <= 389)):
          if (pro_color == "black"):
            list[pro_index] = Knight(pro_index, pro_color, 'N')
            promote = False
          else:
            list[pro_index] = Knight(pro_index, pro_color, 'WN')
            promote = False
        if ((y >= 439) & (y <= 477)):
          if (pro_color == "black"):
            list[pro_index] = Bishop(pro_index, pro_color, 'B')
            promote = False
          else:
            list[pro_index] = Bishop(pro_index, pro_color, 'WB')
            promote = False

    pygame.display.update()

  else:
    for x in range(8):
      for y in range(8):
        if (((x + y) % 2) != 0):
          pygame.draw.rect(screen, (105,42,42), (x * 100, y * 100, 100, 100))
        else:
          pygame.draw.rect(screen, (255,255,255), (x * 100, y * 100, 100, 100))
      temp = 'P'

    for i in range(64):
      if (list[i] != 'E'):
        list[i].draw()

      promote = False

  if event.type == pygame.MOUSEBUTTONDOWN:
    x, y = pygame.mouse.get_pos()
    index = int((x / 100)) + int(((int(y / 100) / 1) * 8))



    if (index1 == -1):
      if ((list[index] != 'E')):
        if (turn == list[index].get_color()):
          index1 = index
          list[index1].change_light()
    elif ((index != index1) & (index2 == -1)):
      list[index1].change_light()
      index2 = index


    if ((index1 != index2) & (index2 != -1)):
      valid_1 = list[index1].move(index2)
      if (valid_1 == 1):
        if (turn == "white"):
          turn = "black"
        else:
          turn = "white"
      index1 = -1
      index2 = -1
      index = -1
      #draw_list = list







  pygame.display.update()

# Screen setup
