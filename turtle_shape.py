# import turtle

# turtle.shape("turtle")
# turtle.speed(1)

# # turtle.forward(100)
# # turtle.left(90)
# # turtle.forward(100)
# # turtle.left(90)
# # turtle.forward(100)
# # turtle.left(90)
# # turtle.forward(100)
# for i in range(4):
#     turtle.forward(100)
#     turtle.left(90)

# turtle.exitonclick()


# equilateral triangle
import turtle

turtle.shape("arrow")
turtle.speed(2)

# turtle.forward(100)
# turtle.left(120)
# turtle.forward(100)
# turtle.left(120)
# turtle.forward(100)

# turtle.exitonclick()


def draw_triangle(side_length):
    for i in range(4):
        turtle.forward(side_length)
        turtle.left(120)


# import turtle

# turtle.shape('turtle')
# turtle.speed(1)

# for i in range(4):
#     turtle.forward(100)
#     turtle.left(90)

# turtle.exitonclick()


# import turtle

# turtle.shape("arrow")
# turtle.speed(8)
# turtle.color("red")


# def draw_square(side_length):
#     for i in range(4):
#         turtle.forward(side_length)
#         turtle.left(90)


# counter = 0
# while counter < 90:
#     draw_square(100)
#     turtle.right(4)
#     counter += 1


draw_triangle(200)