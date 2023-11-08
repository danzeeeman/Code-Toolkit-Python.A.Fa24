def setup():
    size(1024, 1024)
    global strokes, gml, screen_width, screen_height, scale_factor_y, scale_factor_x, drawing
    strokes = []
    gml = loadXML("69599.gml")
    screen = xml.getChildren("tag")[0].getChildren("environment")[0].getChildren("screenBounds")[0]
    screen_width = float(screen.getChildren("x")[0].getContent())
    screen_height = float(screen.getChildren("y")[0].getContent())
    drawing = xml.getChildren("tag")[0].getChildren("drawing")[0].getChildren("stroke")
    
    dw = 1024
    dh = dw * screen_height/screen_width
    
    i = 0
    for _stroke in drawing:
        strokes.append([])
        for pt in _stroke.getChildren("pt"):
            strokes[i].append([float(pt.getChildren('x')[0].getContent())*dw, float(pt.getChildren('y')[0].getContent())*dh])
        i += 1
    
    strokeWeight(10) 
    
    

def draw():
    background(255)
    diff = 1
    pre_point = [0, 0]
    for _stroke in strokes:
        noFill()
        beginShape()
        # print("new line")
        for pt in _stroke:
            if pre_point[0] == 0 and pre_point[1] == 0:
                pre_point = pt
            # print(pt)
            diff_a = pt[0] - pre_point[0]
            diff_b = pt[1] - pre_point[1]
            diff = sqrt(diff_a*diff_a + diff_b*diff_b)
            diff = min(diff, 15)
            strokeWeight(diff)
            vertex(pt[0], pt[1])
            pre_point = pt
        endShape()
