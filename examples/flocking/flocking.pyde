x = []
y = []
speed = []
rect_color = []


def setup():
    global x, y, speed, rect_color
    size(1024, 512)
    rectMode(CENTER)
    
    i = 0
    while i < 1000:
        x.append(random(0, width))
        y.append(random(0, height))
        speed.append(random(25, 50))
        rect_color.append([0,0,0]) 
        i+=1 
        
def draw():
    background(255)
    global x, y, speed, rect_color
    i = 0
    while i < len(y):
        dir_x = (mouseX - x[i])/width
        dir_y = (mouseY - y[i])/height
        x[i] += dir_x * speed[i]
        y[i] += dir_y * speed[i]
        
        
        fill(rect_color[i][0],rect_color[i][1], rect_color[i][2])
        circle(x[i], y[i], 10)
        i = i + 1 
        
