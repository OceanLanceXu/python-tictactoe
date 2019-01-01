# coding=UTF8

import sys
if sys.version_info >= (3, 0):
  from tkinter import Tk, Button
  from tkinter.font import Font
else:
  from Tkinter import Tk, Button
  from tkFont import Font
from copy import deepcopy

class Board:
  COLOR = ['red', 'orange', 'blue', 'green', 'yellow', 'white']

  def __init__(self,other=None):
    self.empty = -1
    self.size = 3
    self.fields = {}
    self.clear()

    # copy constructor
    if other:
      self.__dict__ = deepcopy(other.__dict__)

  def cycle_color(self,x,y):
    index = self.fields[x,y]
    index = (index + 1) % len(Board.COLOR)
    self.fields[x,y] = index

  def clear(self):
    for y in range(self.size):
      for x in range(self.size):
        self.fields[x,y] = self.empty

class GUI:

  def __init__(self):
    self.app = Tk()
    self.app.title('Cube Color Changer')
    self.app.resizable(width=False, height=False)
    self.boards = []
    for c in range(4):
      self.boards.append(Board())
    self.board_index = 0
    self.board = self.boards[self.board_index]
    self.font = Font(family="Helvetica", size=64)
    self.buttons = {}
    for x,y in self.board.fields:
      handler = lambda x=x,y=y: self.cycle_color(x,y)
      button = Button(self.app, command=handler, font=self.font, width=3, height=1)
      button.grid(row=y, column=x)
      self.buttons[x,y] = button

    handler = lambda: self.clear()
    self.clear_button = Button(self.app, text='clear 0', command=handler)
    self.clear_button.grid(row=self.board.size+1, column=1, columnspan=1, sticky="WE")

    handler = lambda: self.change_board('left')
    button = Button(self.app, text='<==', command=handler)
    button.grid(row=self.board.size+1, column=0, columnspan=1, sticky="WE")

    handler = lambda: self.change_board('right')
    button = Button(self.app, text='==>', command=handler)
    button.grid(row=self.board.size+1, column=2, columnspan=1, sticky="WE")


    self.update()


  def change_board(self, direction):
    if direction == 'right':
      self.board_index += 1
      self.board_index = self.board_index % 4

    elif direction == 'left':
      self.board_index -= 1
      self.board_index = self.board_index % 4
    self.board = self.boards[self.board_index]
    self.clear_button['text'] = 'clear ' + str(self.board_index)

    print('change_board:', self.board_index)
    self.update()
    #self.app.update()

  def clear(self):
    self.board.clear()
    self.update()

  def cycle_color(self,x,y):
    self.app.update()
    self.board.cycle_color(x,y)
    self.update_cell(x, y)
    print('cycle_color:', self.board_index, x, y, self.buttons[x,y]['bg'])

  def update_cell(self, x, y):
    color_index = self.board.fields[x,y]
    self.buttons[x,y]['bg'] = Board.COLOR[color_index]

  def update(self):
    for (x,y) in self.board.fields:
      self.update_cell(x, y)

  def mainloop(self):
    self.app.mainloop()

if __name__ == '__main__':
  GUI().mainloop()
