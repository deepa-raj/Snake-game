# Our snake should be able to head a piece of food,
#
# which is just going to be a blue circle. And every time it touches the food,
#
# the circle moves to a new, random location on the screen.
#
# If we take a look at our code,
#
# you can see that the main.py controls the entire game.
#
# It dictates how the screen should behave and how the snake behaves.
#
# Now, everything that's to do with a snake,
#
# it's a parent's and behavior, is all captured inside a class.
#
# So everything snake related is inside the snake class.
#
# So what we want to be able to do is to create a new food.py file
#
# and this food.py is going to be its own class.
#
# And the food class is going to know how to render itself as a small circle on
#
# the screen. And then every time the snake touches the food,
#
# then that food is going to move to a new random location.

from turtle import Turtle
import random



# what we want to be able to do is we actually want this class, food, to inherit
#
# from the turtle class.
#
# So that way this food class is going to have all of the capabilities of the
#
# turtle class,
#
# but it's also going to have some specific things that we're going to tell it
#
# how to do so that it behaves like an actual piece of food.
class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)


#------------------------------------------------------ TODO: Workout example-----------------------------------------------------

# class Animal:
#     def __init__(self):
#         self.num_eyes = 2
#
#     def breathe(self):
#         print("Inhale, Exhale.")
#
# class Fish(Animal):
#     def __init__(self):
#         super().__init__()
#     def breathe(self):
#         super().breathe()
#         print("Doing this underwater")      # By learning about inheritance,
#                                             # what it allows us to do is to take an existing class that we've created or
#                                             # somebody else has created,
#                                             # and then build on top of it without having to reinvent the wheel and redefine
#                                             # everything that's in that class.
#     def swim(self):
#         print("Moving in water.")
#
#
# nemo = Fish()
# nemo.swim()
# nemo.breathe()