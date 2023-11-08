car_x = 0
def move_car():
    global car_x
    car_x += 5
    if car_x > width:
        car_x = -380
    return car_x


def drawCar(x):
    pushStyle()
    pushMatrix()
    translate(x, height/2-50)
    fill('#0734E3')
    rect(0, 0, 300, 150)
    fill(0)
    circle(10, 150, 90)
    circle(290, 150, 90)
    popMatrix()
    popStyle()
    pass
