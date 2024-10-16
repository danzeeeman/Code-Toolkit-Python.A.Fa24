car_x = 0
car_y = 0

def drawLandscape():
    fill(100, 255, 100)
    circle(width/3, height, 500)
    circle(width/3*2, height, 500)
    pass
    
def drawCar():
    fill(255, 0, 0)
    rect(car_x, car_y, width/3, height/3)
    
    
def moveCar(dir_x, dir_y, speed):
    global car_x, car_y
    car_x += dir_x * speed
    car_y += dir_y * speed
