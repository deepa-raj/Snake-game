

# TODO 1: Create a snake body
# TODO 2: Move the snake
# TODO 3: Control the snake
# TODO 4: Detect Collision with food
# TODO 5: Create a Scoreboard
# TODO 6: Detect collision with wall
# TODO 7: Detect collision with tail

# -----------------------------------------------------------------------------------------
from turtle import Screen, Turtle
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0) # So the tracer is a method in the screen class
                 # and in order to turn it off, we're going to set it to zero.

snake = Snake()
food = Food()
scoreboard = Scoreboard()
                                                                # "tracer()" is one of the screen class's method.
                                                                # this takes a number as an input, and it turns the animation on or off.
                                                                # And when the tracer() method is 'off', we can use the "update() method
                                                                # to tell our program when to refresh and redraw the screen "
                                                                # Once we write the call the tracer() method, un-till the update() method is called,
                                                                # the screen is not going to show us what's been happening our code
screen.listen()
"""To start listen for keystrokes"""
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

"""This is the code that will get our snake to automatically move forward👇"""
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1) #So this basically just add a 0.1 second delay after each segment moves.
    snake.move()

    # Detect collision with food.
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()     # The distance method works by comparing the distance from this turtle to whatever
                                        # it is that you put inside the parentheses. So the X could be a pair of numbers, X and Y,
                                        # or it could simply just be a turtle instance. So you're comparing this turtle against another turtle,
                                        # and you're trying to get hold of the distance between the two turtles.
                                        # So what that means is we can check to see if the distance from the first segment of the snake,
                                        # so it remember that would be snake.head.distance,
    # Detect collision with wall.
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.reset()
        snake.reset()

    # Detect collision with tail.
    for segment in snake.segments[1:]: # slicing
        # if segment == snake.head:
        #     pass
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()


        # if head collides with any segment in the tail:
        #trigger game_over()


screen.exitonclick()








# starting_position = [(0, 0), (-20, 0), (-40, 0)]
# """this list will contain tuples which is x and y values"""
#
# segments = []
# for position in starting_position:
#     new_segment = Turtle("square")
#     new_segment.color("white")
#     new_segment.penup()
#     new_segment.goto(position)
#     segments.append(new_segment)
#
#
#
#
#     for seg_num in range(len(segments) - 1, 0, -1):
#         new_x = segments[seg_num - 1].xcor()
#         new_y = segments[seg_num - 1].ycor()
#         segments[seg_num].goto(new_x, new_y)
#     segments[0].forward(20)

"""This is the code that will get our snake to automatically move forward👆"""

"""for seg_num in range(start=2, stop=0, step=-1)"""
"""this range function has no keyword arguments in python, since it came from C language.
if we actually want it to work, we have to delete these,
but before that we longer using these hard-code numbers like 2, 1, 0
so, instead of going to 2 to 0, we want to go to the 'length of the segments'
so in the future, if we had 10 segments or 20 segments then our code will still work
the length of the segment is 3 to begin with, and we know that list starts counting from 0,
so, 0,1,2.... the last position is going to be the length-1
And we going to stop at the 0 segment, and we can delete the 'stop' named argument"""


"""The number going to be 2, then 1 and finally 0.
so we are going to use that to hold of the last segment from our list of segments.
so we can tap into that list and then get hold of the last one using the 'seg_num'.
and then we are going to set it to go to a particular X and Y position.
 Now, the X and Y position that we want it to go to is second to the last segment position."""

"""Then how to hold of second to the last segment position?
----- we are going to get hold of the segment and then pass in seg_num but then -1
so when we first start out, we start out with 2, so the segment at position 2 is going to be the last segment.
and then the segment at 2-1 is hing to be the second to last segment
 and that one going to hold the X coordinate"""

"""We are going to set this into the new variable called new_x
and we're going to do the same and get hold of the new_y.
so, we  are going to get hold of the second to last segment Y coordinate,"""

"""And we are going to use thees coordinates,
new_x, new_y to tell this last segment to go to the position of the second to last segment"""


"""We have to move the very first segment to move forward to 20 paces. So, at the very end of the code
outside of the for loop, we have to hold the first segment, so segment at position 0,
and then we are going to get it to move forward by 20 paces"""

"""This is the code that will get our snake to automatically move forward👆"""


    # for seg in segments:
    #     seg.forward(20)
    # screen.update()
    # time.sleep(0.1)

# segment_1 = Turtle("square")
# segment_1.color("white")

# segment_2 = Turtle("square")
# segment_2.color("white")
# segment_2.goto(-20, 0)
#
# segment_3 = Turtle("square")
# segment_3.color("white")
# segment_3.goto(-40, 0)



