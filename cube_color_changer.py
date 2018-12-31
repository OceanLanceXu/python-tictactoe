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
    for y in range(self.size):
      for x in range(self.size):
        self.fields[x,y] = self.empty
    # copy constructor
    if other:
      self.__dict__ = deepcopy(other.__dict__)
      
  def cycle_color(self,x,y):
    index = self.fields[x,y]
    index = (index + 1) % len(Board.COLOR)
    self.fields[x,y] = index
  

class GUI:

  def __init__(self):
    self.app = Tk()
    self.app.title('Cube Color Changer')
    self.app.resizable(width=False, height=False)
    self.board = Board()
    self.font = Font(family="Helvetica", size=32)
    self.buttons = {}
    for x,y in self.board.fields:
      handler = lambda x=x,y=y: self.cycle_color(x,y)
      button = Button(self.app, command=handler, font=self.font, width=3, height=1)
      button.grid(row=y, column=x)
      self.buttons[x,y] = button
    handler = lambda: self.clear()
    button = Button(self.app, text='clear', command=handler)
    button.grid(row=self.board.size+1, column=0, columnspan=self.board.size, sticky="WE")
    self.update()
    
  def clear(self):
    self.board = Board()
    self.update()
  
  def cycle_color(self,x,y):
    print(x, y)
    self.app.update()
    self.board.cycle_color(x,y)
    self.update_cell(x, y)

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
