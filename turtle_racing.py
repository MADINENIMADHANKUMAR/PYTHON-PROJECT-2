import turtle
import random
WIDTH,HEIGHT=400,400
color_list=["red","green","orange","pink","blue","black","yellow","grey","purple","olive"]
def no_of_turtles():
  count=0
  while True:
    count=input("How many turtles are you want to participate in the Race (2-10):")
    if count.isdigit():
      count=int(count)
    else:
      print("Please enter a numeric values between 2 to 10")
      continue
    if 2<=count<=10:
      return count
    else:
      print("Input is not given in range.........Try again!")
turtles=no_of_turtles()
print(f"Number of turtles racing {turtles}")
s=turtle.Screen()
s.setup(400,400)
x_spacing=WIDTH//(turtles+1)
turtle_list=[]
for i in range(1,turtles+1):
  new_t=turtle.Turtle()
  new_t.shape("turtle")
  new_t.left(90)
  new_t.color(color_list[i-1])
  new_t.penup()
  new_t.goto(-WIDTH//2+(i*x_spacing),-HEIGHT//(2+10))
  turtle_list.append(new_t)
def race():
  m=True
  while m:
    for i in turtle_list:
      distance=random.randrange(1,20)
      i.forward(distance)
      x,y=i.pos()
      if y>=HEIGHT//2-20:
        print(f"Winner is {i.pencolor()} turtle!")
        m=False
        break
race()
turtle.done()