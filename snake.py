from turtle import Screen, Turtle

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

"""In python Constants are represent in caps in this case STARTING_POSITION is a constant """
class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]


    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def reset(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def extend(self):
        self.add_segment(self.segments[-1].position())  # if [1,2,3] the -1 position is the last item in the list.
                                                        # then we have to hold the position() method
                                                        # this is a method that comes from the turtle class and we can call it by writing
                                                        # position and then parentheses and we'll get the position of that segment.
                                                        # And then we're going to add this new segment
                                                        # to the same position as the last segment.
    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1): # Its going to loop through each of the segments going from the last
                                                             # segment to the first segment, so basically in reverse order.
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)        # be really careful here because it's not just self.head.heading,
                                            # it's actually heading as a method (heading()) because remember that the head of the snake is
                                            # the first segment of our list of segments and each segment is a individual turtle.
                                            # The turtle has a heading method which will give you
                                            # a direction in terms of these 360-degree numbers,
                                            # and then we can use that to check to see if it's equal to down.
                                            # And if it is, then it's not allowed to go up. So using this logic,

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)


# So the process of inheriting behavior and appearance from an existing class is
#
# known as class inheritance. When we're talking about class inheritance,
#
# you can inherit both appearance, so attributes,
#
# like for example, if you inherited the same eyes as your mother,
#
# or if you inherited the same nose as your grandfather,
#
# but you can also inherit behavior.
#
# So maybe you chop tomatoes in the same way that your dad chops tomatoes.



# how does inheritance actually work in terms of the code? Well,
#
# we can define a class, let's call it Fish,
#
# and it has an initializer.
#
# Now in order to get this Fish class to inherit from another class,
#
# all we have to do is to
#
# add a set of parentheses after the name of the class and then provide the
#
# class that we want to inherit from.
#
# So in this case our fish is inheriting from the animal class.
#
# And then in order to get a hold of everything that an animal has and is, so its
#
# attributes and methods, all we have to do is inside the init,
#
# add this super().__init__().
#
# And the super refers to the superclass.
# And the super refers to the superclass.
#
# So basically, initialize everything that the superclass can do in our fish
#
# class.