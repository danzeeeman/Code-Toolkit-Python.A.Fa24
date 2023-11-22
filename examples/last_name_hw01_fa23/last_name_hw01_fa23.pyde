def setup():
    size(600,600)
    rectMode(CENTER)

def draw():
    background(255)
    rect(300,300, 50,50)

def keyPressed():
    if key == 'e':
        ellipse(300,300, 50,50)

    if key == 'r':
        rect(300,300, 50,50)
        
def mousePressed():
    if mouseX > 275 and mouseX <= 325 and mouseY > 275 and mouseY < 325:
        print("mouseX "+str(mouseX)+" mouseY "+str(mouseY)) 
