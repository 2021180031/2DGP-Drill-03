from pico2d import *
import math

open_canvas()

boy = load_image('character.png')


def move_top():
    print('Moving top')
    for x in range(15,785,5):
        draw_boy(x,550)
    pass


def move_right():
    print('Moving right')
    for y in range(550,90,-5):
        draw_boy(785,y)
    pass


def move_bottom_of_rectangle():
    print('Moving bottom')
    for x in range(785, 15, -5):
        draw_boy(x, 90)
    pass


def move_left():
    print('Moving left')
    for y in range(90, 550, 5):
        draw_boy(15, y)
    pass


def move_rectangle():
    print("Moving rectangle")

    move_top()
    move_right()
    move_bottom_of_rectangle()
    move_left()
    
    
    pass


def move_left_diagonal():
    print("Moving left diagonal")
    y=90
    x=785

    while 400<x:
        draw_boy(x, y)
        y+=5
        x-=5


    pass


def move_right_diagonal():
    print("Moving left diagonal")
    x=400
    y=475
    while 15 < x <= 400:
        draw_boy(x, y)
        y -= 5
        x -= 5
    pass


def move_bottom_of_triangle():
    print('Moving bottom')
    for x in range(15, 785, 5):
        draw_boy(x, 90)
    pass


def move_triangle():
    print("Moving triangle")
    move_bottom_of_triangle()
    move_left_diagonal()
    move_right_diagonal()

    pass


def move_circle():
    print("Moving circle")

    r = 200
    for deg in range(0,360):
        x = r * math.cos(math.radians(deg))+400
        y = r * math.sin(math.radians(deg))+300

        draw_boy(x, y)
    pass


def draw_boy(x: float, y: float):
    clear_canvas_now()
    boy.draw_now(x, y)
    delay(0.1)





while True:
    move_rectangle()
    move_triangle()
    move_circle()



    # break
    pass


close_canvas()




