#Stoplight in python 3
import turtle
import time

wn = turtle.Screen()
wn.title("Stoplight")
wn.bgcolor("black")

# Draw box around stoplight
pen = turtle.Turtle()
pen.color("yellow")
pen.width(3)
pen.hideturtle()
pen.penup()
pen.goto(-30, 60)
pen.pendow()
pen.fd(60)
pen.rt(90)
pen.fd(120)
pen.rt(90)
pen.fd(60)
pen.rt(90)
pen.fd(120)
#lines of stoplight

#Red light
red_light = turtle.Turtle()
red_light.shape("circle")
red_light.color("grey")
red_light.penup()
red_light.goto(0, 40)

#Yellow light
yellow_light = turtle.Turtle()
yellow_light.shape("circle")
yellow_light.color("grey")
yellow_light.penup()
yellow_light.goto(0, 0)

#Green light
green_light = turtle.Turtle()
green_light.shape("circle")
green_light.color("grey")
green_light.penup()
green_light.goto(0, -40)


while True:
  yellow_light.color("grey")
  red_light.color("red")
  time.sleep(4)

  red.color("grey")
  green_light("green")
  time.sleep(3)

  green_light.color("grey")
  yellow_light("yellow")
  time.sleep(2)

wn.mainloop()

#CLASS STOPLIGHT

import turtle

wn = turtle.Screen()
wn.title("Stoplight")
wn.bgcolor("black")

class Stoplight()
  def _init_(self, x, y):
    #draw the  border/is actually the turtle instance
    self.pen = turtle.Turtle()
    self.pen.penup()
    self.pen.hideturtle()
    self.pen.speed(0)
    self.pen.color("yellow")
    self.pen.goto(x-30, y+60)
    self.pen.dow()
    self.pen.fd(60)
    self.pen.rt(90)
    self.pen.fd(120)
    self.pen.rt(90)
    self.pen.fd(60)
    self.pen.rt(90)
    self.pen.fd(120)

    self.color = ""

    self.red_light = turtle.Turtle()
    self.yellow_light = turtle.Turtle()
    self.green_light = turtle.Turtle()

    self.red_light.speed(0)
    self.yellow_light.speed(0)
    self.green_light.speed(0)

    self.red_light.color("grey")
    self.yellow_light.color("grey")
    self.green_light.color("grey")

    self.red_light.shape("circle")
    self.yellow_light.shape("circle")
    self.green_light.shape("circle")

    self.red_light.penup()
    self.yellow_light.penup()
    self.green_light.penup()

    self.red_light.goto(x, y + 40)
    self.yellow_light.goto(x, y)
    self.green_light.goto(x, y - 40)

    
    def change_color(self, color):
      self.red_light.color("grey")
      self.yellow_light.color("grey")
      self.green_light.color("grey")
#They are diffrend from one another
  if color == "red":
    self.red_light.color("red")
    self.color = "red"
  elif color == "yellow":
    self.red_light.color("yellow")
    self.color("yellow")
  elif color == "green":
    self.red_light.color("green")
    self.color("green")
  else
    print("Error: Unknow color {}" .format(color))
    
  def timer(self):
    if self.color == "red"
        self.change_color("green")
        wn.ontimer(self.timer, 3000)
      #after 2.000 mil sec it calls itself again
      elif self.color == "yellow":
        self.change_color("red")
        wn.ontimer(self, timer 2000)
      elif self.color == "green":
        self.change_color("yellow")
        wn.ontimer(self, timer 1000)

#is actually calling to it's own pen self
stoplight = Stoplight(0, 0)
stoplight.change_color("red")
stoplight.timer()
#self comes from stoplight

stoplight2 = Stoplight(-100, 0)
stoplight2.change_color("yellow")
stoplight2.timer()

stoplight3 = Stoplight(100, 0)
stoplight3.change_color("green")
stoplight3.timer()

#They all have a pen



wn.mainloop()
