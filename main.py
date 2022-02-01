import turtle, random
krasas = ["red", "magenta", "purple", "pink"]
Rafael = turtle.Turtle()
Rafael.shape("turtle") #circle, arrow, classic

for i in range(0,12):
  Rafael.circle(100)
  Rafael.circle(100, steps=4)
  Rafael.right(30)
  Rafael.color(random.choice(krasas))