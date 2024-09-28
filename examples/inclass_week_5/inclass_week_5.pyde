circle_x = 300
circle_y = 300
circle_dir_x = 0
circle_dir_y = 0

def setup():
    size(600, 600)
    frameRate(60)

def draw():
    global circle_x, circle_y, circle_dir_x, circle_dir_y
    # background(255)
    ellipse(circle_x, circle_y, 100, 100)
    circle_x = circle_x + circle_dir_x
    circle_y = circle_y + circle_dir_y
     
    if circle_x > width-50:
        circle_dir_x = -0.5
    if circle_x < 50:
        circle_dir_x = 0.5
        
    if circle_y > height-50:
        circle_dir_y = -1
    if circle_y < 50:
        circle_dir_y = 1
    
    pass
      
def keyPressed():
    global circle_dir_x, circle_dir_y
    if key == 'a':
        circle_dir_x = -1
    if key == 'd':
        circle_dir_x = 1
    if key == 'w':
        circle_dir_y = 1
    if key == 's':
        circle_dir_y = -1
    pass

def keyReleased():
    global circle_dir_x, circle_dir_y
    if key == 'a':
        circle_dir_x = 0
    if key == 'd':
        circle_dir_x = 0
    if key == 'w':
        circle_dir_y = 0
    if key == 's':
        circle_dir_y = 0
    pass
    
def mousePressed():
    global circle_dir_x
    circle_dir_x = circle_dir_x * -1
    global circle_dir_y
    circle_dir_y = circle_dir_y * -1
    pass
