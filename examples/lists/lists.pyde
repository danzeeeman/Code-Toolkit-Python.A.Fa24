y = []
x = []
size_of_our_list = 10
def setup():
    size(1025, 500)
    stroke(50, 50, 250)
    fill(150, 150, 250)
    rectMode(CENTER)
    global y
    i = 0
    while i < size_of_our_list:
        y.append(200)
        x.append(100+100*i)
        i = i +1

def draw():
    background(255)
    global y
    i = 0
    while i < size_of_our_list:
        rect(x[i], y[i], 100, 100)
        if mouseX > x[i] - 50 and mouseX < x[i] + 50:
            if mouseY > y[i] - 50 and mouseY < y[i] + 50:
                y[i] = y[i] + random(-15,15)
                x[i] = x[i] + random(-5, 5)
        i = i + 1
        
