circle_x = 300
circle_speed = 5
circle_direction = circle_speed
circle_width = 50
def setup():
    size(600, 600)
    stroke(50, 50, 150)
    fill(200, 200, 255)
    rectMode(CENTER)
    pass
    
def draw():
    background(255)
    global circle_x
    global circle_direction
    circle_x += circle_direction
    if circle_x > width - circle_width/2:
        circle_direction = -circle_speed
    if circle_x < circle_width/2:
        circle_direction = circle_speed
    ellipse(circle_x, 300, circle_width, circle_width)
    

def keyPressed():
    global circle_direction
    global circle_speed
    if key == 'f':
        circle_direction = -1*circle_speed
    if key == 'h':
        circle_direction = circle_speed
        
    if key == '=':
        circle_speed += 1
    if key == '-':
        circle_speed -= 1
        if(circle_speed <= 0):
            circle_speed = 1
