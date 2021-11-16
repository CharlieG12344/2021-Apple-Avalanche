#   a123_apple_1.py
import turtle as trtl
import random as rand

#-----setup-----
apple_image = "apple.gif" # Store the file name of your shape

wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
wn.addshape(apple_image) # Make the screen aware of the new file
wn.bgpic("background.gif")
apple = trtl.Turtle()
xOffset = -25
yOffset = -50
wn.tracer(False)
screen_width = 300
screen_length = 300
letter_list = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
current_letter = "A"

#-----functions-----
# given a turtle, set that turtle to be shaped by the image file
def reset_apple(active_apple):
  length = len(letter_list)
  if(length != 0):
    index = rand.randint(0, length)
    active_apple.goto(rand.randint(-screen_width/2, screen_width/2), rand.randint(-screen_length/2, screen_length/2))
    current_letter = letter_list.pop(index)
    draw_apple(active_apple, current_letter)

def draw_apple(active_apple, letter):
  active_apple.shape(apple_image)
  active_apple.showturtle()
  draw_letter(letter, active_apple)
  wn.update()

def appledrop():
  wn.tracer(True)
  apple.penup()
  apple.goto(apple.xcor(), -250)
  apple.clear()
  apple.hideturtle()
  wn.tracer(False)
  reset_apple(apple)

def draw_letter(letter, active_apple):
  active_apple.color("white")
  active_apple.penup()
  remember_pos = active_apple.position()
  active_apple.setpos(active_apple.xcor() + xOffset, active_apple.ycor() + yOffset)
  active_apple.write(letter, font=("Arial", 48, "bold"))
  active_apple.setpos(remember_pos)

def checkA():
  if(current_letter == "A")
    appledrop()


#-----function calls-----
draw_apple(apple, "G")
wn.onkeypress(checkA, "a")

wn.listen()

wn.mainloop()