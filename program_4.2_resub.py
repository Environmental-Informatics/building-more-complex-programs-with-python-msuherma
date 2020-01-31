# ABE36500
# Mukhamad Suhermanto 0030930122


""" from polygon - previous task """
import math
import turtle

def polyline(t, n, length, angle):
    """ Drawing n number line segments.
    
    t = Turtle
    n = number of line segments
    length = length of each segment
    angle = degrees of segments angle
    """
    for i in range (n):                 #assigning for loop for n 
        t.fd(length)                    #move Turtle forward as given length
        t.lt(angle)                     #turn Turtle as given angle
def polygon(t,n, length):
    """ Drawing a polygon with n number of sides.
    
    t = Turtle
    r = radius of the arcs
    angle = degree of angle of arcs
    """
    angle = 360.0/n
    polyline(t,n,length,angle)

def arc(t,r,angle):
    """Drawing an arc for given radius and angle.
    
    t = Turtle
    r = radius
    angle = angle subtended by the arc [degrees]
    """
    arc_length = 2 * math.pi * r * abs(angle)/360
    n = int(arc_length/4) + 3
    step_length = arc_length / n
    step_angle = float(angle) / n
    t.lt(step_angle/2)
    polyline(t,n,step_length,step_angle)
    t.rt(step_angle/2)
    
def circle(t,r):
    """ Drawing a circle with given radius.
    
    t = Turtle
    r = radius
    """
    arc(t,r,360)
    

'''
Starting the code for the flowers
'''

def petal(t,r, angle):
    """ Drawing a petal using two arcs.
    
    t = Turtle
    r = radius of the arcs
    angle = degree of angle of arcs
    """
    for i in range (2):
        arc(t, r, angle)                    # the 'arc' here is from the above script (actually from polygon)
        t.lt(180 - angle)                   # To turn the angle of Turtle

def flower(t,n,r, angle):                   # to draw the whole flower
    """ Drawing a flower with n petals.
    
    t = Turtle
    n = number of petal
    r = radius of the arcs
    angle = angle of the arcs [degrees]
    """
    for i in range (n):                     # to assign loop for i
        petal(t,r,angle)                    # to draw the petal of the flower, calling for above defined 'petal'
        t.lt(360.0/n)                       # to make the turning angle of Turtle, hence the petal will be different for each flower

def move(t, length):
    """ to Move the turtle, in here for 3 flowers
    t = Turtle
    length = length of movement
    """
    t.pu()                                  # to command the Turtle pen up (before getting to the point of start the drawing)
    t.fd(length)                            # to command the Turtle to do not draw, for certain length (distance of each flower)
    t.pd()                                  # to command the Turtle pen down, starting the point of drawing (for this case is the center of each flower)

bob = turtle.Turtle()   

# To Draw a sequence of three flowers, as assign in the book
# 1st flower
move(bob, -100)             # tells the point to start for bob
flower(bob, 7, 60.0, 60.0)  # tells bob to draw 7 petals, 60 radius of arc, 60 angle of arc

# 2nd flower
move(bob, 100)              
flower(bob, 10, 40.0, 80.0)

#3rd flower
move(bob, 100)
flower(bob, 20, 140.0, 20.0)

# To hide the tutle
bob.hideturtle()
turtle.mainloop()                           # to 'kill' the tutle, saying that this is done