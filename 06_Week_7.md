# Code Toolkit: Python, Fall 2024
## Week 7 — Class notes
## Timing and State
We've already seen how to draw shapes and make them move on their own. This motion would typically start when the program started running and continue forever. Or maybe it would be triggered or changed by user interaction in some way. Today we are going to talk about timing: how to create motion that is in some way scheduled, chorreographed, triggered with some delay, or that repeats at some interval.

Time-based media are most typically thought of as sound and the moving image, although digital media like video games and motion graphics are also grouped in. Today we will see explicitly how software operates in a time-based manner, and think about how to work with the domain of time, as we have thus far mainly been working within the domain of space.

## History and inspiration

![Oskar Fischinger](images/large_fischinger04_800.jpg)

One incredible example of early time-based media is the work of Oskar Fischinger. Fischinger was an artist in the first part of the 20th century and a pioneer in animation and motion graphics. A classic example of his work is the animated film [Studie nr 8, 1931](https://vimeo.com/35735682).

You might be inclined to think of the history of animation as preceding that of cinema, but in fact there is a historical case to be made for understanding these in the opposite order. Several modern artists and illustrators in the early 20th century were inspired by cinema to create animation, and used the principle of cinema — a continuous strip of film, divided into cells of static imagery that flicker by the viewer's eyes — to create early animation and motion graphics. In fact, many of these innovators actually worked on film strips, drawing and etching into the cells by hand.

Fischinger actually contributed to Disney's Fantasia but quit uncredited because of creative differences. In 2012, the Whitney museum showed an exhibition of his artwork called "Space Light Art". [There is great documentation for this show online and I highly recommend taking a look!](https://whitney.org/exhibitions/oskar-fischinger)

## A numeric timeline with ```millis()```

In week 4 ("Making Things Move") we saw how you could use variables and some basic arithmetic to make things move "on their own".

We looked at this pattern:

```
circleX = 300
def setup():
    size(600,600)
    stroke(50,50,150)
    fill(200,200,255)

def draw():
    global circleX
    background(255)
    ellipse( circleX,300, 50,50)
    circleX = circleX + 1
```

That draws a single circle, and to make the circle move horizontally, it create a variable which gets used to specify the x position of the circle. The value of this variable is then changed a little every frame, by incrementing or decrementing the variable.
We expanded on this example using conditionals to ask questions about the position of the circle, and changed its movement based on that. For example:

```
circleX = 300
def setup():
    size(600,600)
    stroke(50,50,150)
    fill(200,200,255)

def draw():
    global circleX
    background(255)
    ellipse( circleX,300, 50,50)
    circleX = circleX + 1
    if circleX > width:
        circleX = 0
```

Today we are going to build on this, but instead of using conditionals to ask questions about movement in space, we're going to use them to ask questions about time.

Unlike other time-based digital tools — like Adobe Premiere, After Effects, Audacity, or others — Processing does not give you an explicit, visual timeline. If you want to create timed events, you have to think in terms of numbers.

Processing gives us a command just for this purpose: ```millis()``` (check the reference)

This command returns a number that corresponds to the number of milliseconds since the program started running. A millisecond is one thousandth of a second, so 1000 milliseconds = 1 second. ```millis()``` is like a stopwatch that starts when your program starts, and keeps running as long as the program is running.

Even though this isn't a visual timeline, we can imagine a visual timeline in our thinking. millis() returns a number that represents a playhead or a marker, moving along a timeline. Thus, we can use this like a variable to ask questions about the status of our sketch, similar to mouseX and mouseY. We can also use it to "save" or remember a position of this playhead on the timeline.

This one basic command is enough to implement many different types of timed events, from simple things up to more complicated ones.

For example, think of this pseudocode:

```
  Do something for the first three seconds my sketch is running
We could implement that with:
    if millis() < 3000:
        # Do something
Similarly, think about this pseudocode:
  Wait three seconds, then do something for two seconds
Which we could implement with this:
    if millis() > 3000 and millis() < 5000:
        # Do something
```

What should Do something be in this case? Well let's say we want to draw a shape and only have it move according to the above timing. We could combine movement and timing like this:


```
circleX = 300
def setup():
    size(600,600)
    stroke(50,50,150)
    fill(200,200,255)

def draw():
    global circleX
    background(255)
    ellipse( circleX,300, 50,50)
    if millis() < 3000:
      circleX = circleX + 1

    if circleX > width:
      circleX = 0
```

Notice how now, the circle's position is being updated just like before, but only when that conditional about millis() is True. In other words, only during the interval described by the Boolean expression ```millis() < 3000```
We can get a bit more complicated by introducing variables to use for saving time values. For example:

```
circleX = 300
startTime = 3000
def setup():
    size(600,600)
    stroke(50,50,150)
    fill(200,200,255)

def draw():
    global circleX
    background(255)
    ellipse( circleX,300, 50,50)
    if millis() > startTime and millis() < startTime + 2000:
      circleX = circleX + 1

    if circleX > width:
      circleX = 0
```

When would this move the circle?
This doesn't seem that interesting since I'm setting the variable startTime to a hard-coded value. But because I am using a varibale as a placeholder for that value, that means that the value could change.

Building on this, we can combine it with event handling to let the user trigger the timing:

```
circleX = 300
startTime = 3000
def setup():
    size(600,600)
    stroke(50,50,150)
    fill(200,200,255)

def draw():
    global circleX
    background(255)
    ellipse( circleX,300, 50,50)
    if millis() > startTime and millis() < startTime + 2000:
      circleX = circleX + 1

    if circleX > width:
      circleX = 0

def keyPressed():
    global startTime
    startTime = millis()
```

Now when would this move the rectangle? Think about when the startTime variable gets set. Whenever any key is pressed, startTime gets set to the current value of millis() — or in other words, it marks where the imaginary playhead is at when the user presses a key. Then, each time ```draw()``` runs, it checks if the current value of millis() is greater than startTime, and less than startTime plus 2000, or two seconds. So, in pseudocode we could say:

```
  Every time the user presses any key,
    move a circle to the right for two seconds.
```

Notice that the circle still starts moving at 3 seconds and moves for 2 seconds. This is because of the initial value that we are using for startTime, still carried over from the previous code snippet. What could you set the initial value of startTime to so that it would not appear like this? Think about when that conditional is True and what value would make it not True. Highlight for answer: startTime = -2000

The following three examples show how to do different cases. Hopefully you can use these code snippets as patterns for how to implement these situations. Use them, combine them with other things we've worked on, and build on them.
Wait a while, then do something forever
In this example we wait two seconds, and then start moving the square and never stop

```
position = 0

def setup():
    size(600,600)
    smooth()
    stroke(50,50,150)
    fill(200,200,255)

def draw():
    global position
    background(255)

    ellipse(position,300,100,100)

    # wait two seconds, then move forever:
    if millis() > 2000:
        position = position + 1
```

Wait a while, then do something for a while, then stop
In this example we wait two seconds, then start moving the square, move the square for one second, and then stop.

```
position = 0

def setup():
    size(600,600)
    smooth()
    stroke(50,50,150)
    fill(200,200,255)

def draw():
    global position
    background(255)

    ellipse(position,300,100,100)

    # only increase the position if millis() is greater than two seconds but
    # less than three seconds
    if millis() > 2000 and millis() < 3000:
        position = position + 1
```

Do something for a little while, then stop
Wait a little while and repeat the above

This example is similar to example 2 above, but it has a variable which gets added to the timing values. Then another if statement periodically resets that variable. This causes the whole timing process to reset, doing this forever.

```
position = 0

startTime = 0

def setup():
    size(600,600)
    smooth()
    stroke(50,50,150)
    fill(200,200,255)

def draw():
    global position, startTime
    background(255)

    ellipse(position,300,100,100)

    # move for a little while, then stop
    if millis() > startTime and millis() < startTime + 2000:
        position = position + 1

    # wait a little while, then reset the startTime variable,
    # so the above timing starts over:
    if millis() > startTime + 4000:
      startTime = millis()
```

## BREAK

## CLOCKS???

## State: a new way to use variables

Do you remember this?

```
circleX = 300
circleDirection = 1
def setup():
    size(600,600)
    stroke(50,50,150)
    fill(200,200,255)

def draw():
    background(255)
    ellipse( circleX,300, 50,50)
    global circleX
    global circleDirection
    circleX = circleX + circleDirection
    if circleX > width:
        circleDirection = -1
    if circleX < 0:
      circleDirection = 1

def keyPressed():
    if key == 'j':
        circleDirection = -1

    if key == 'l':
        circleDirection = 1
```


So far we have been using variables either for numeric things (like shape sizes, positions, or colors) or for Boolean ```True```/```False``` values. All of these things are ways of keeping track of what the program is doing in a given moment.

Today we saw how we could use timing and ```millis()``` to affect how the program might change over time.

But what if we want the program to change over time in a way that is not explicitly tied to timing. For example, what if we wanted the user to be able to change what the program was doing? Or if we want the program to operate in different phases or modes, and move through those?

In computer science, the term for keeping track of the status of the program is state. We might ask, what state or phase is the program in? This could be used to implement the levels of a video game for example.

The way to do this is by using variables. This is not very different from anything that we have been doing so far. I just want to show a few examples that emphasize how you can use variables in some slightly different ways.

Let's implement a simple light switch. When the user presses the 'n' key (for "on") the light goes on, and when the user presses the 'f' key (for "off") the light goes off.
Let's start by simply drawing a window "with the light off" (black screen):

```
def setup():
    size(800,800)

def draw():
    background(0)
```

How should we implement the "on" key? Well we could use the Boolean keyPressed variable, like this:

```
def setup():
    size(800,800)

def draw():
    background(0)

    if keyPressed and key == 'n':
        background(255,255,200)
```

But that only works if the user is holding down the 'n' key. What if we want this to work not like a button that must be held down, and more like a switch that can be flipped?

Could we improve on things by using the def keyPressed() block? That would look like this: block,

```
def setup():
    size(800,800)

def draw():
    background(0)

def keyPressed():
    if key == 'n':
        background(255,255,200)
```

That doesn't really seem to help things. Now, whenever the user presses the 'n' key, the light flashes on for a split second. It still doesn't stay on.

We need a way to keep track of whether the light has been pressed or not. In other words, we need to keep track of the state of the light switch. We'll do this with a variable. Since this variable will only have two values (on, or off) we can use a Boolean variable for this purpose. Initially I will set the variable to False to signify that the light is off.

```
switchState = False
def setup():
    size(800,800)

def draw():
    if switchState:
        background(255,255,200)
    else:
        background(0)
```

Now, whenever the variable switchState is True, I will draw the light as on, and whenever the variable is False, I will draw the light off. But this is not doing anything yet. Why? Because I am not changing this variable anywhere! Let's try to change it.
When the user presses the 'n' key, let's make the variable True:

```
switchState = False
def setup():
    size(800,800)

def draw():
    if switchState:
        background(255,255,200)
    else:
        background(0)

def keyPressed():
    global switchState
    if key == 'n':
        switchState = True
```

OK! This is getting is somewhere. Now when the user presses the 'n' key, switchState is set to True, and so the light will be drawn on.
The last thing is to let the user turn it off. Have a look at this:

```
switchState = False
def setup():
    size(800,800)

def draw():
    if switchState:
        background(255,255,200)
    else:
        background(0)

def keyPressed():
    global switchState
    if key == 'n':
        switchState = True
    if key == 'f':
        switchState = False
```

Great! So now we have a variable (switchState) that keeps track of whether the user has pressed a certain key or not. In other words, it is keeping track of the state of the program. And we can use if statements to change the value of that variable.
Of course, we can create programs with even more states than just on / off. As a simple example, we could repeat the pattern from the above example to have several different on / off variables. Let's create a program that let's the user turn three shapes on or off:

```
rectOn = False
ellipseOn = False
triangleOn = False

def setup():
    size(800,800)
    rectMode(CENTER)

def draw():
    background(255)
    if rectOn:
        fill(255,155,155)
        rect(200,400,50,50)

    if ellipseOn:
        fill(155,255,155)
        ellipse(400,400,50,50)

    if triangleOn:
        fill(155,155,255)
        triangle(600,375, 625,425, 575,425)

def keyPressed():
    global rectOn, ellipseOn, triangleOn

    if key == 'q':
        rectOn = True
    if key == 'a':
        rectOn = False
        
    if key == 't':
        ellipseOn = True
    if key == 'g':
        ellipseOn = False
        
    if key == 'o':
        triangleOn = True
    if key == 'l':
        triangleOn = False  
```

Notice that I've named my variables using the pattern triangleOn. This creates a nice way of reading your code so that you're looking at the if statements, you can read it like If the triangle is on.
What if we didn't want to have different keys for on and off, but instead wanted the same key to turn each shape on and off? We call this a toggle. And it looks like this:

```
rectOn = False
ellipseOn = False
triangleOn = False

def setup():
    size(800,800)
    rectMode(CENTER)

def draw():
    background(255)
    if rectOn:
        fill(255,155,155)
        rect(200,400,50,50)

    if ellipseOn:
        fill(155,255,155)
        ellipse(400,400,50,50)

    if triangleOn:
        fill(155,155,255)
        triangle(600,375, 625,425, 575,425)

def keyPressed():
    global rectOn, ellipseOn, triangleOn

    if key == 'q':
        rectOn = not rectOn
        
    if key == 't':
        ellipseOn = not ellipseOn
        
    if key == 'o':
        triangleOn = not triangleOn
```

Now, in those if statements, I'm setting each variable to the opposite of whatever it currently is. This creates the toggle effect.
Lastly, we can keep track state that is more than on / off. Have a look at this code:

```
dayEveningNight = 1

def setup():
    size(800, 800)

def draw():
    if dayEveningNight == 1:
        background(155,155,255)
    elif dayEveningNight == 2:
        background(25,25,75)
    elif dayEveningNight == 3:
        background(0)

def keyPressed():
    global dayEveningNight

    if key == 'q':
        dayEveningNight = dayEveningNight + 1
        if dayEveningNight > 3:
            dayEveningNight = 1
```

Here, I am using a variable dayEveningNight that is holding the values 1, 2, or 3. I am using an if statement in the draw() block that checks what the value of this variable is and draws something accordingly. And then, in the keyPressed() block, I am incrementing that variable based on what the user has pressed. If the variable gets larger than 3, I am reseting back to its initial value of 1.

```
button_x = 0
button_y = 0
button_width = 100
button_height = 100
button_hover = False
button_clicked = False
button_clicked_time = 0
def setup():
    size(512, 512)
    
def draw():
    global button_clicked
    current_time = millis()
    background(0)
    if button_clicked:
        fill(0, 255, 255)
        if current_time - button_clicked_time > 750:
            button_clicked = False
    elif button_hover:
        fill(255, 0, 255)
    else:
        fill(255, 255, 0)
    
    rect(button_x, button_y, button_width, button_height)

def mousePressed():
    global button_clicked, button_clicked_time
    if mouseX > button_x and mouseX < button_x+button_width:
        if mouseY > button_y and mouseY < button_y+button_height:
            button_clicked = True
            button_clicked_time = millis()
        else:
            button_clicked = False
    else:
        button_clicked = False

def mouseMoved():
    global button_hover
    if mouseX > button_x and mouseX < button_x+button_width:
        if mouseY > button_y and mouseY < button_y+button_height:
            button_hover = True
        else:
            button_hover = False
    else:
        button_hover = False
```

```
circle_x = 300
circle_y = 300
last_frame = 0
start_time_x = 3000
start_time_y = 4000
dir_x = 1
dir_y = 1
def setup():
    size(512, 512)
    stroke(50, 50, 150)
    fill(200, 200, 255)
    textSize(32)
    frameRate(10)

def draw():
    background(255)
    global circle_x, start_time_x, start_time_y, circle_y, dir_x, dir_y
    current_time = millis()
    
    if current_time > start_time_x and current_time < start_time_x + 2000:
        circle_x += dir_x
    
    if circle_x > width or circle_x < 0:
        dir_x *= -1
        
    if current_time > start_time_x + 4000:
        start_time_x = current_time
        
    if current_time > start_time_y and current_time < start_time_y + 2000:
        circle_y += dir_y
    
    if circle_y > height or circle_y < 0:
        dir_y *= -1
        
    if current_time > start_time_y + 5000:
        start_time_y = current_time
        
    ellipse(circle_x, circle_y, 50, 50)
    
# def keyPressed():
#     global start_time
#     start_time = millis()
```

You can use these same principles to keep track of many kinds of state within your program. For example, if a user is entering a password, or the levels of a game.


## Homework Notes

```
def setup():
    size(1024, 1024)

def draw():
    background(0)
    
    for i in range(0, 12):
        pushMatrix()
        translate(width/2, height/2)
        theta = map(i, 0, 12, 0, TWO_PI) + PI
        r = width/3
        x = r * sin(theta)
        y = r * cos(theta)
        stroke(255, 255, 255)
        fill(255, 255, 255)
        r = 175
        tick_offset_x = r * sin(theta)
        tick_offset_y = r * cos(theta)
        line(tick_offset_x, tick_offset_y, x, y)
        popMatrix()
        
    for i in range(0, 60):
        pushMatrix()
        translate(width/2, height/2)
        theta = map(i, 0, 60, 0, TWO_PI) 
        r = width/3
        x = r * sin(theta)
        y = r * cos(theta)
        stroke(255, 255, 255)
        fill(255, 255, 255)
        r = width/3-25
        tick_offset_x = r * sin(theta)
        tick_offset_y = r * cos(theta)
        line(tick_offset_x, tick_offset_y, x, y)
        popMatrix()
        
    
    current_hour = hour() % 12
    theta = map(current_hour, 0, 12, TWO_PI, 0)+PI
    r = width/10
    x = r * sin(theta)
    y = r * cos(theta)
    pushMatrix()
    stroke(255, 255, 255)
    fill(255, 255, 255)
    translate(width/2, height/2)
    line(0, 0, x, y)
    popMatrix()
    
    
    current_min = minute()
    theta = map(current_min, 0, 60, TWO_PI, 0)+ PI
    r = width/5
    x = r * sin(theta)
    y = r * cos(theta)
    pushMatrix()
    stroke(255, 255, 255)
    fill(255, 255, 255)
    translate(width/2, height/2)
    line(0, 0, x, y)
    popMatrix()
```

## Home Work DUE WEEK 9

* Coding Assignment #5: One Button Game
* ["Data Visualization", from Matthew Fuller's Software Studies: A Lexicon](https://monoskop.org/images/a/a1/Fuller_Matthew_ed_Software_Studies_A_Lexicon.pdf)
Catherine D'Ignazio and Lauren Klein, ["Unicorns, Janitors, Ninjas, Wizards, and Rock Stars"]
