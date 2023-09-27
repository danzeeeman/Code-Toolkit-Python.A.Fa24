def setup():
    size(600,600)
    rectMode(CENTER)

def draw():
    background(255)
    if mouseX < width/3:
        circle(width/2, width/2, 100)
    elif mouseX > width/3 and mouseX <= 2*width/3:
        rect(width/2, height/2, 100, 100)
    else:
        triangle(width/2-50, height/2-50, width/2, height/2+50, width/2+50, height/2-50)
