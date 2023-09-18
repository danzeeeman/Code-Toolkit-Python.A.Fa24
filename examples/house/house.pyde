size(2048, 2048)
background(255)

#color
color_house = color(10, 142, 240)
color_window = color(184, 204, 219)
color_door = color(234, 17, 71)
color_roof = color(211, 5, 234)

#sizes
house_width = 3.0*width/7.0
window_width = house_width/4.5
door_width = house_width/5.5
door_height = door_width*2.0
roof_over_hange = house_width/10.0

noStroke()
fill(color_house)
rect(width/2.0-house_width/2.0, height/2.0-house_width/2.0, house_width, house_width)

fill(color_window)
rect(width/2.0-window_width/2.0-house_width/3.5, height/2.0-window_width/2.0+house_width/5.0, window_width, window_width)
rect(width/2.0-window_width/2.0+house_width/3.5, height/2.0-window_width/2.0+house_width/5.0, window_width, window_width)
rect(width/2.0-window_width/2.0-house_width/3.5, height/2.0-window_width/2.0-house_width/5.0, window_width, window_width)
rect(width/2.0-window_width/2.0+house_width/3.5, height/2.0-window_width/2.0-house_width/5.0, window_width, window_width)

fill(color_door)
rect(width/2.0-door_width/2.0, (height/2.0-door_height/2.0)+house_width/2.0-door_height/2.0, door_width, door_height)

fill(color_roof)
triangle(width/2.0-house_width/2.0-roof_over_hange, height/2.0-house_width/2.0, width/2.0, height/7.0, width/2.0+house_width/2.0+roof_over_hange, height/2.0-house_width/2.0) 
