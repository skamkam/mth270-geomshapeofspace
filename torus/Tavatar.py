from graphics import *

class TAvatar:
  def __init__(self): #defines avatar and its center, initializes at the upper left corner and pointing upper left
    self.X = 115
    self.Y = 115
    self.body = Image(Point(self.X, self.Y), "upleft.png")

  def move_avatar(self, key, amount):
    if key == 'W': #moves up [amount] pixels
      self.body.move(0, -1*amount)
      self.Y -= amount
    elif key == 'A': #move left [amount] pix
      self.body.move(-1*amount, 0)
      self.X -= amount
    elif key == 'S': #move down [amount] pix
      self.body.move(0, amount)
      self.Y += amount
    elif key == 'D': #move right [amount] pix
      self.body.move(amount, 0)
      self.X += amount
