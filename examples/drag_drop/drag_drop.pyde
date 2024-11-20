x = []
y = []
rect_width = []
rect_height = []
is_pressed = []
is_rect_selected = False
mouse_pressed = False
def setup():
    size(1024, 1024)
    rectMode(CENTER)
    for i in range(0, 10):
        x.append(width/10 + width/10*i)
        y.append(height/10 + height/10*i)
        rect_width.append(150)
        rect_height.append(150)
        is_pressed.append(False)
    
def draw():
    global x, y, is_rect_selected
    background(255)
    for i in range(0, len(x)):
        rect(x[i], y[i], rect_width[i], rect_height[i])
        if not is_rect_selected and mouse_pressed:
            is_pressed[i] = checkBounds(x[i], y[i], rect_width[i], rect_height[i])
            if is_pressed[i]:
                is_rect_selected = True
        
        if not mouse_pressed:
            is_pressed[i] = False
            is_rect_selected = False
            
        if is_pressed[i]:
            x[i], y[i] = moveRect(x[i], y[i])
    
def moveRect(x, y):    
    x += mouseX - pmouseX
    y += mouseY - pmouseY
    return x, y

def checkBounds(x, y, rect_w, rect_h):
    if mouse_pressed:
        if mouseX > x - rect_w/2 and mouseX < x + rect_w/2:
            if mouseY > y - rect_h/2 and mouseY < y + rect_h/2:
                return True
    return False
                    
def mousePressed():
    global mouse_pressed
    mouse_pressed = True
    
def mouseReleased():
    global mouse_pressed
    mouse_pressed = False
