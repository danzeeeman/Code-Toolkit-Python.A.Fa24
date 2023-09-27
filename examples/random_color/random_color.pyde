def setup():
    size(400,400)
    background(255)
    r = random(0,255)
    g = random(0,255)
    b = random(0,255)
    fill(r,g,b)

def draw():
    rect(mouseX,150,100,100)
