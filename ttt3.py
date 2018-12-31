# coding=UTF8

# Python TicTacToe game with Tk GUI and minimax AI
# Author: Maurits van der Schee <maurits@vdschee.nl>

import sys
if sys.version_info >= (3, 0):
  from tkinter import Tk, Button
  from tkinter.font import Font
else:
  from Tkinter import Tk, Button
  from tkFont import Font
from copy import deepcopy

class Board:
  
  def __init__(self,other=None):
    self.player = 'x'
    self.empty = ''
    self.size = 3
    self.fields = {}
    for y in range(self.size):
      for x in range(self.size):
        self.fields[x,y] = self.empty
    # copy constructor
    if other:
      self.__dict__ = deepcopy(other.__dict__)
      
  def move(self,x,y):
    board = Board(self)
    board.fields[x,y] = board.player
    return board
  

class GUI:

  def __init__(self):
    self.app = Tk()
    self.app.title('Button Toggle')
    self.app.resizable(width=False, height=False)
    self.board = Board()
    self.font = Font(family="Helvetica", size=32)
    self.buttons = {}
    for x,y in self.board.fields:
      handler = lambda x=x,y=y: self.move(x,y)
      button =  Button(self.app, command=handler, font=self.font, width=3, height=1)
      button.grid(row=y, column=x)
      self.buttons[x,y] = button
    handler = lambda: self.clear()
    button = Button(self.app, text='clear', command=handler)
    button.grid(row=self.board.size+1, column=0, columnspan=self.board.size, sticky="WE")
    self.update()
    
  def clear(self):
    self.board = Board()
    self.update()
  
  def move(self,x,y):
    print(x, y)
    self.app.update()
    self.board = self.board.move(x,y)
    self.update()

   
            
  def update(self):
    for (x,y) in self.board.fields:
      text = self.board.fields[x,y]
      self.buttons[x,y]['text'] = 'text'
      self.buttons[x,y]['disabledforeground'] = 'black'
      if text==self.board.empty:
        self.buttons[x,y]['state'] = 'normal'
      else:
        self.buttons[x,y]['text'] = ''

  def mainloop(self):
    self.app.mainloop()

if __name__ == '__main__':
  GUI().mainloop()
