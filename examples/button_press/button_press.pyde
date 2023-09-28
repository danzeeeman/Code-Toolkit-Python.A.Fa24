def setup():
    size(600,600)
    # noFill()
    rectMode(CENTER)
 
def draw():
    background(255)
    fill(255, 255, 255)
    rect(300,300, 50,50)
    pushStyle()
    if mouseX > 275 and mouseX <= 325 and mouseY > 275 and mouseY < 325:
        if mousePressed:
            fill(255, 0, 255)
            circle(300, 300, 50)
        else:
            fill(255, 255, 0)
            circle(300, 300, 50)
    popStyle()
