def drawLandscape():
    background(255)
    fill('#80E7F0')
    noStroke()
    #sky
    rect(0, 0, width, height/2)
    #ground
    fill('#892E34')
    rect(0, height/2, width, height/2)
    drawClouds()
    
    pass
        # Pretend that in here
        # I have many many commands
        # to draw a landscape.
        
def drawClouds():
    pushStyle()
    fill(255)
    
    for i in range(3):
        pushMatrix()
        translate(0, i*15)
        for i in range(20):
            circle(width/3+i*15+noise(0.1+i)*25*sin(noise(0.1+i)), height/6+noise(0.01+i)*35, 35)
        popMatrix()
    popStyle()
    pass
    
