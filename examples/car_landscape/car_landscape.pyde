from landscape import *
from car import *
from character import *
car_x = 0
character_x = 0
def setup():
    size(600,600)
    setupCharacter()

def draw():
    global character_x
    drawLandscape()
    drawCar(car_x)
    character_x -= 1
    if character_x < -300*1.4:
        character_x = width
    drawCharacter(character_x)
    pass
    
def keyPressed():
    global car_x
    
    if key == ' ':
        car_x = move_car()
    
