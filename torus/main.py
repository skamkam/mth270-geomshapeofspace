from graphics import *
from Tavatar import *

WIDTH = 400
HEIGHT = 400

win = GraphWin("Torus", WIDTH, HEIGHT)

def square_creation(): #creates flat torus
  rect = Rectangle(Point(50, 50), Point(350, 350))

  leftedge = Polygon(Point(50, 200), Point(60, 210), Point(40, 210))

  rightedge = Polygon(Point(350, 200), Point(340, 210), Point(360, 210))

  topedge = Line(Point(150, 50), Point(200, 50))
  topedge.setArrow('last')

  bottomedge = Line(Point(150, 350), Point(200, 350))
  bottomedge.setArrow('last')

  kb = [rect, leftedge, rightedge, topedge, bottomedge]
  for obj in kb: #draws objs to window
    obj.setWidth(3)
    obj.draw(win)


def main():
  square_creation()
  avatar = TAvatar()
  avatar.body.draw(win) #draws the avatar to window

  win.getMouse()

  direction = ''
  while direction != 'Q':
    direction = win.checkKey().upper()
    avatar.move_avatar(direction, 5)
    
    if avatar.X < 50: #passes left border
      avatar.move_avatar('D', 300) #moves to the right by width of torus
    elif avatar.X > 350: #passes right border
      avatar.move_avatar('A', 300)
    elif avatar.Y < 50: #passes top border
      avatar.move_avatar('S', 300) #moves to the bottom by height of torus
    elif avatar.Y > 350: #passes bottom border
      avatar.move_avatar('W', 300)


if __name__ == '__main__':
  main() #calls main module
