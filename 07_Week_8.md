# Code Toolkit: Python, Fall 2024
## Week 8 — Class notes
## Review
Last week we covered two topics:

Timing. Unlike other digital design and production tools, Processing does not give us a visual representation of the timline to work with for scheduling events. Instead, as is the common pattern with computer programming (and hence with Processing, the goal of which is to teach coding fundamentals) we get a numeric representation of time which we can use to schedule events. We access this in the form of the millis() command (documentation).

Using ```millis()``` and if statements, we're able to ask all kinds of complicated questions related to timing and the scheduling of events. For example, refresh your memory (or refer back to last week's class notes) about what this conditional would do:

```
if millis() > eventTime and millis() < eventTime + 1000:
    ellipse(400,400,50,50)

if millis() > eventTime + 5000:
    eventTime = millis()
```

State. We also talked about a new way to use variables. So far we've used variables to keep track of numbers, Boolean values, and text. Numbers can be used for anything related to drawing: the position, size, or color of shapres, for example. Boolean values can be used to keep track of yes / no questions, especially as applied to conditionals in if statements or while loops.

But with state, we can use variables to keep track of what our programs are doing. For example, maybe you are drawing two scenes, day and night, and you want the user to switch between them with a key press. Your code might look something like this:

# global variable:

```
isNight = False

def draw():
    if isNight:
        # include commands to draw the night scene
    else:
        # include commands to draw the day scene

def keyPressed():
    isNight = not isNight
```

That else could also say if not isNight if you wanted to be explicit.
Make sure you understand the last line. That is toggling the Boolean value of the variable. If the variable was True, after a key press it will be False (i.e., not True). Invsersely, if the variable was False, after a key press it will be set to not False, or in other words, it will be True. So by pressing any key the user is flip-flopping the Boolean variable back-and-forth, which will affect what the if statement does inside the draw() block.

Working with may things
Today we will learn about working with many things. So far if you wanted to move many things, you would hard code new variables for each one. In week 5 we learned how to draw many items using loops, but you couldn't move each item around individually. Today we will learn how to do that using a thing called lists.

In Python, a list is like a collection of variables.

In a certain way, this topic is like a mashup of variables and loops:

With loops, instead of drawing many things line-by-line, you can create a loop which draws many things at once, even a dynamic number of things.

With lists, instead of declaring each variable line-by-line, you can create one list that declares many variables at once, and can even allow you to work with a dynamic number of variables.

This introduces us to one of the most interesting aspects of computer science: data structures. The term data structure refers to a way of organizing many variables together for efficient and convenient use. The type of variable organization that you'll need to use in a given situation (i.e., the type of data structure) depends on the problem that you are trying to solve. In addition to lists, Python provides many other data structures, such as: sets, tuples, and dictionaries, among others. And beyond these data structures that come with Python, in computer science there are many other more complex kinds of data structures that go by names like: stacks, queues, linked lists, and trees. But in one sense, lists are the most fundamental data structure, and in a certain way it makes sense to think of them as underlying all these others.

Data structures allow you to start to think about modeling: how to organize your variables and other code in a way that matches the thing that you're trying to do. A good data structure could make your program much easier to implement and to read, while an inappropriately chosen data structure could make the thing that you're trying to do very hard and potentially less efficient in terms of computing resources.

# Background

![Gene Kogan](images/flocking.jpg)

Since lists are used to manage many things, they are often used to implement things like swarms, or herds of objects that behave as if they are acting independently or on their own.

Daniel Shiffman, a professor at NYU in the Interactive Telecommunications Program (ITP) graduate program, uses lists and other data structures to implement swarms that are used to simulate natural phenomenon like animals, plants, clouds, flowing liquids, and others.

For example, here is a [video](https://www.youtube.com/watch?v=tOv8JGA2-mM) that demonstrates a simulation of "flocking", like birds or fish moving together. (It's a very cute video.) Shiffman's book [Nature of Code](https://natureofcode.com/) offers detailed lessons in how to achieve affects like this.

Another, more aesthetically developed, example is this [flocking demo](https://vimeo.com/39517129) by Gene Kogan.

And another great example is the project [We Feel Fine](http://www.wefeelfine.org/) by Jonathan Harris and Sep Kamvar. This project was made in 2006 using Processing and unfortuntely can be a bit difficult to run that now. (You will probably need to install Java for your browswer and OS version.) But there is documentation online, like this [video](https://www.youtube.com/watch?v=NSGpOSgnfz8) that demonstrates how the project functioned.

# Lists
When we first looked at variables, we saw how you could use them to add "variance" or "change" into your composition. You replace a hard-coded number with a placeholder like x, and then you could change the value of that placeholder, modifying your sketch. And each variable stores one value.


```
circle_x = 0
circle_y = 0
circle_dir_x = 1
circle_dir_y = 1

def setup():
    size(600, 600)
    frameRate(60)

def draw():
    global circle_x, circle_y, circle_dir_x, circle_dir_y
    background(255)
    ellipse(circle_x, circle_y, 100, 100)
    circle_x = circle_x + circle_dir_x
    circle_y = circle_y + circle_dir_y
     
    if circle_x > width-50:
        circle_dir_x = -1
    if circle_x < 50:
        circle_dir_x = 1
        
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
    global circle_dir
    circle_dir = circle_dir * -1
    pass
```

Have a look at this example if you'd like, but don't be intimidated. There's a lot going in there, and we'll work through it today bit-by-bit.

Let's start with a simple example that just draws 4 squares:

```
def setup():
    size(500, 500)
    fill(150, 150, 250)
    rectMode(CENTER)

def draw():
   background(255)
   rect(100, 250, 100, 100)
   rect(200, 250, 100, 100)
   rect(300, 250, 100, 100)
   rect(400, 250, 100, 100)
```

Now what if we want each one of these squares to move up and down randomly? Well to start, let's just add a variable for each one:

```
a = 200
b = 200
c = 200
d = 200

def setup():
    size(500, 500)
    stroke(50, 50, 250)
    fill(150, 150, 250)
    rectMode(CENTER)

def draw():
    background(255)

    rect(100, a, 100, 100)
    rect(200, b, 100, 100)
    rect(300, c, 100, 100)
    rect(400, d, 100, 100)
```

Nothing new yet, I've just swapped out a hard-coded number for a variable placeholder. Note that I don't need to add global inside the draw() block yet because while I am using these global variables, I am not assigning or modifying them.
Now to make each square move, we could change the value of each variable in draw(). Let's change it by a random amount, so they just kind of shake there.

```
a = 200
b = 200
c = 200
d = 200

def setup():
    size(500, 500)
    stroke(50, 50, 250)
    fill(150, 150, 250)
    rectMode(CENTER)

def draw():
    global a, b, c, d
    background(255)

    rect(100, a, 100, 100)
    rect(200, b, 100, 100)
    rect(300, c, 100, 100)
    rect(400, d, 100, 100)
    
    a = a + random(-5,5)
    b = b + random(-5,5)
    c = c + random(-5,5)
    d = d + random(-5,5)
```

Note that now I am modifying the variables inside the draw() block, so now I do have to add global because otherwise Python would think that my assignment statements were creating new local variables. Hopefully this global is getting clearer for you, but I agree that it can be confusing.

Looking at that code, notice that I'm doing the same thing several times: drawing a rect(). And the paramters to each one follow a simple and direct pattern. Hopefully that makes you want to replace those four lines with something else. What is it? Think back to week 5 ... What if we wanted to have 8 or 100 or 1000 squares?

So hopefully you realized that we could replace those four rect() commands with one while loop that draws all four:

```
a = 200
b = 200
c = 200
d = 200

def setup():
    size(500, 500)
    stroke(50, 50, 250)
    fill(150, 150, 250)
    rectMode(CENTER)

def draw():
    global a, b, c, d
    background(255)

    i = 100
    while i <= 400:
        rect( i, a, 100, 100)
        i = i + 100

    a = a + random(-5, 5)
    b = b + random(-5, 5)
    c = c + random(-5, 5)
    d = d + random(-5, 5)
```

If you step through that loop, you'll see that it is replicating the four rect() statements from the previous snippet.
BUT WAIT — what about the variables b, c, and d?! As you can see from running that, the vertical position of each square is now being controlled by a. Changing the value of a changes the position of each square in the same way. But we can't use a, b, c, and d independently because we are in a loop.

This is precisely why we need lists. To keep track of many things in a situation like a loop.

And we might even have a dynamic number of things. Think for example what would happen if I used mouseX in my while conditional.

So what we're about to do is: replace those four variables with one variable, a list, and that one list variable will hold all four values within it and will let us reference them inside a loop.

New syntax:
```x = []``` These square brackets create a new kind of variable, which is a list. It does not have any values yet, but we've just told Python that this one variable can hold many values. I suggest reading this code like: "Create a variable called x and set it to an empty list".
Now to actually add values to this new list variable, we use a command called append(). Like this:

```
x.append(5)
x.append("Hello")
x.append(True)
```

As you see, a list can contain any of the other values that we've been working with so far: numbers, text strings, and Boolean values. You can view the contents of a list with print():

```
print(x)
# This would print to the console:
# [5, 'Hello', True]
```
But the really new, weird, and exciting thing is how we actually reference, or in other words, how we use those values.

Lists are ordered. The values they hold are stored in order. And you reference those values by number, using a new syntax, square brackets:
```
print( x[0] )
# This would print to the console
# 5
```
This is called the list index. The word index (like the index in a book or your index finger) has etymology related to pointing. So you can think of the 0 here as pointing to a specific value, the first value. (In other parts of computer science, this is actually called a pointer, but pointers are a slightly different and more complicated topic common in C and C++ programming.)
You can use an indexed list anywhere that you would use a regular variable, so any of the following would be valid:

```
rect( x[0], 5, 100, 100)
fill( 155, 155, x[0] )
if x[5] < 10:
    # do something
```

(Obviously this snippet wouldn't make any sense altogether.)
You also use the assignment operator = to set values in a list like this:

```
x[0] = 5
```

But you cannot use the assignment operator to add new values to the list, or in other words to make the list longer. For example, this will get an error:

```
y = [] # Make a new empty list
y[0] = 5 # Try to set a value into the list

# Displays an error in the console saying:
# IndexError: list assignment index out of range

# But this would work:
y.append(5)
# And then you could change the value later like this:
y[0] = 6
```

The exciting thing is that now we have a list of values, and they are referenced or indexed using a number. That allows us to do things like reference those values in a loop or have a dynamic number of values.

Important note. You may have noticed something a little weird: lists are always indexed starting with 0. So the first item of this list would be x[0], and if a list had ten items, the last would be indexed as x[9].

You can ask Python for the length of a list like this: len(x). This is a very important and extremely common thing to do.

So we can say that the index of a list called x ranges from 0 to len(x)-1
Let's put this to use in our example, but start by first by going back to the version without a while loop:

```
y = []
y.append(200)
y.append(200)
y.append(200)
y.append(200)

def setup():
    size(500, 500)
    stroke(50, 50, 250)
    fill(150, 150, 250)
    rectMode(CENTER)

def draw():
    background(255)

    rect(100, y[0], 100, 100)
    rect(200, y[1], 100, 100)
    rect(300, y[2], 100, 100)
    rect(400, y[3], 100, 100)
    
    y[0] = y[0] + random(-5,5)
    y[1] = y[1] + random(-5,5)
    y[2] = y[2] + random(-5,5)
    y[3] = y[3] + random(-5,5)
```

We're using a list! Notice that instead of creating four independent variables, a, b, c, and d, I am now creating one list called y, and appending the value 200 to it four times. And then I reference those values using the square bracket index notation, as items 0, 1, 2, and 3. So instead of saying a, I'm saying y[0].
This doesn't have any apparent advantage yet, but let's keep going ...

Remember that my goal was to use a loop to draw and move my squares, so that I could have a dynamic number. Here's where it gets exciting and a little tricky.

Since we use numbers to index lists, we can also use a variable for the list index. In other words, we can use a variable to specify which item in the list we are referring to. For example:

```
n = []
n.append(350)
i = 0
print( n[i] )
# Prints to the console:
# 350
Pause and make sure you can wrap your head around that. What is the value of i?
Step through this example:

clouds = []
clouds[0] = 700
clouds[1] = 800
clouds[2] = 900
i = 0
print( clouds[i] ) # What would this print? 700 (Highlight to see.)
i = i + 1
print( clouds[i] ) # What would this print? 800
```

Now that we can use variables to index our list, we're almost there. Let's go back to our loop, but we have to change one thing first.

Remember how last week we talked about different ways of specifying our looping varible in a while loop? Compare the below two examples to see how they are equivalent:

```
i = 100
while i <= 400:
    rect(i, a, 100, 100)
    i = i + 100
i = 0
while i <= 3:
    rect(100 + i*100, a, 100, 100)
    i = i + 1
```

We can finally put everything together:

```
y = []
y.append(200)
y.append(200)
y.append(200)
y.append(200)

def setup():
    size(500, 500)
    stroke(50, 50, 250)
    fill(150, 150, 250)
    rectMode(CENTER)

def draw():
    background(255)

    i = 0
    while i <= 3:
        rect(100 + i*100, y[i], 100, 100)
        i = i + 1
    
    y[0] = y[0] + random(-5,5)
    y[1] = y[1] + random(-5,5)
    y[2] = y[2] + random(-5,5)
    y[3] = y[3] + random(-5,5)
```

We can also move the code that changes the y values into the same loop:

```
y = []
y.append(200)
y.append(200)
y.append(200)
y.append(200)

def setup():
    size(500, 500)
    stroke(50, 50, 250)
    fill(150, 150, 250)
    rectMode(CENTER)

def draw():
    background(255)

    i = 0
    while i <= 3:
        rect(100 + i*100, y[i], 100, 100)
        y[i] = y[i] + random(-5,5)
        i = i + 1
```
And we can also make a loop that initializes the list values. Note that I've moved this into the setup() block:

```
def setup():
    size(500, 500)
    stroke(50, 50, 250)
    fill(150, 150, 250)
    rectMode(CENTER)

    global y
    y = []
    i = 0
    while i <= 3:
        y.append(200)
        i = i + 1

def draw():
    background(255)

    i = 0
    while i <= 3:
        rect(100 + i*100, y[i], 100, 100)
        y[i] = y[i] + random(-5,5)
        i = i + 1
```

Note that since I am creating y inside the setup() block (by saying y = # something) I need to declare it global so that it can be accessed inside the draw() block.
Now we have a loop that uses repetition to create many things and and one list that holds many values, one for each of those things.

This means that now we could relatively easily modify this so that instead of 4 squares, we had 8, 100, or 1000. Change the 3 to 4 to see how easy it is to add one more:

```
def setup():
    size(500, 500)
    stroke(50, 50, 250)
    fill(150, 150, 250)
    rectMode(CENTER)

    global y
    y = []
    i = 0
    while i <= 4:
        y.append(200)
        i = i + 1

def draw():
    background(255)

    i = 0
    while i <= 4:
        rect(100 + i*100, y[i], 100, 100)
        y[i] = y[i] + random(-5,5)
        i = i + 1
```

Or change it to 10 (for this, I'll make each one less wide):

```
def setup():
    size(500, 500)
    stroke(50, 50, 250)
    fill(150, 150, 250)
    rectMode(CENTER)

    global y
    y = []
    i = 0
    while i <= 10:
        y.append(200)
        i = i + 1

def draw():
    background(255)

    i = 0
    while i <= 10:
        rect(100 + i*25, y[i], 25, 100)
        y[i] = y[i] + random(-5,5)
        i = i + 1
```

What if we only wanted to move the even-numbered rectangles? We could add an if statement inside that last loop:

```
i = 0
while i <= 3:
    rect(100+i*100, y[i], 100, 100)
    if i == 0 or i == 2:
        y[i] = y[i] + random(-5,5)
    i = i + 1
```

But then if we wanted to change our list size, we'd have to keep adding additional checks into that if statement. So to do this more concisely, we could use a thing called the modulo which is like division, but only returns the remainder.
Here are some examples that help demonstrate how modulo works:

```
# Regular division:
print( 10 / 2 ) # Prints 5

# The remainder when dividing 10 by 2:
print( 10 % 2 ) # Prints 0

# Python ignores the decimal when you're using whole numbers:
print( 10 / 3 ) # Prints 3 

# Using the decimal tells Python not to ignore it:
print( 10.0 / 3 ) # Prints 3.3333

# The remainder when dividing 10 by 3:
print( 10 % 3 ) # Prints 1

# 10 goes in to 11 once, with remainder 1:
print( 11 % 10 ) # Prints 1

# So this expression would print True whenever x was an even number:
print( x % 2 == 0 )
```

And here's how you could use that in the above loop:

```
i = 0
while i <= 3:
    rect(100+i*100, y[i], 100, 100)
    if i % 2 == 0: # if dividing by 2 gives remainder 0, it's even
        y[i] = y[i] + random(-5,5)
    i = i + 1
```

That conditional inside the while loop can also be interactive based on mouse input:

```
i = 0
while i <= 3:
    rect(100+i*100, y[i], 100, 100)
    if mouseX > i*100-50 and mouseX < i*100+50:
        y[i] = y[i] + random(-5,5)
    i = i + 1
```

(If you're working through the math on that remember that I'm using ```rectMode(CENTER)``` in these examples.)
To conclude, what should we do if we want these squares to move around in space, like in the flocking examples? In other words, to move horizontally as well as vertically?

We would need an x value for each square. So? Add a new list!

```
x = [] # in setup
```

And go from there: set initial values, use them with the ```rect()``` command, and change the values in some way.

## Live Code Setting Position and Color based upon a List

```
y = []
x = []
speed = []
rect_color = []
def setup():
    global y, x
    size(1920, 1080)
    stroke(50, 50, 250)
    fill(150, 150, 250)
    rectMode(CENTER)
    i = 0
    while i < 10:
        x.append(random(0, width))
        y.append(random(0, height))
        speed.append(random(1, 5))
        rect_color.append([random(0, 255), random(0, 255), random(0, 255)])
        i += 1

def draw():
    global y, x
    background(255)
    i = 0
    while i < len(y):
        fill(rect_color[i][0], rect_color[i][1], rect_color[i][2])
        rect(x[i], y[i], 100, 100)
        dir_x = (mouseX - float(x[i]))/width
        dir_y = (mouseY - float(y[i]))/height
        # print('x:{} y:{} i:{}'.format(dir_x, dir_y, i))
        x[i] += dir_x * speed[i]
        y[i] += dir_y * speed[i]
        if x[i] < 0:
            x[i] = width
        if x[i] > width:
            x[i] = 0
        if y[i] < 0:
            y[i] = height
        if y[i] > height:
            y[i] = 0
        i += 1
 ```

If you wanted them to move in a way that was more sophisticated than just random, what would you do? Well each square would need its own x and y direction. More lists!

## Break

# Functions: project planning, reusability and modularity

Functions are a way to organize your code.

Now that you've started thinking about the midterm project, you will be working on a computer program that is a little bit longer and a little bit more complicated. You need a way to keep this organized and manageable. Functions give you a technique for how to do that.

(Another strategy for code organization involves a technique called object-oriented programming, which uses things called classes and objects. We might talk about this later in the semester if there is time and interest.)

## Functions
A function takes any sequence of commands, groups them together into a block, and gives that block a name. Then, just by using that name, you can automatically run all those commands.

New syntax. Let's say I have this sketch I'm working on:
```
def setup():
    size(600,600)

def draw():
    # Pretend that in here
    # I have many many commands
    # to draw a landscape.
```

To use a function, I must first define it. I pick any name that I'd like (as long as it's not a special Processing reserved word) and then I create a new block like this:

```
def drawLandscape():
    # Pretend that in here
    # I have many many commands
    # to draw a landscape.
```

The term ```drawLandscape()``` is arbitrary. I could have called it ```spaghetti()```, but like with variables, I recommend that you use informative function names that describe what the function does and that will help you remember and understand later what the function is doing.
This syntax is called the function definition or implementation, and this bit of code is described as defining or implementing a function.

Now you would use this new function simply by specifying its name like this:
```
drawLandscape()
```

This is referred to as calling or invoking the function. Now, just specifying this function name is equivalent to invoking all the commands contained within the function definition.
If calling a function looks familiar to you, that is because nearly everything that you've been doing all semester has been calling functions. We just weren't refering to it that way. I've been referring to them as commands. All the commands that you have been using thus far are actually functions that Processing has already defined for you in advance.

```rect()```, ```background()```, ```map()```: these are all functions that Processing has defined for you, that you are able to use simply by calling. The ```len()``` command is a function that Python defines for you. The ```setup()``` and ```draw()``` blocks are also functions, but they are special functions that Processing requires you to define. When you run a sketch, the Processing system starts by first calling your ```setup()``` function, then calling your ```draw()``` function many times, as we talked about in week 3.

Putting all these pieces together, my initial sketch would now look like this:

```
def setup():
    size(600,600)

def draw():
    drawLandscape()

def drawLandscape():
    # Pretend that in here
    # I have many many commands
    # to draw a landscape.
```

Here you can see the definition and the invocation of this new function called drawLandscape().
Some notes on this new syntax:

You may be curious about why I am calling the function before (or above) where I am defining it. The order does not matter. When you run your sketch, Processing (and Python) looks through your entire program for all function definitions and stores them in memory, ready and waiting to be invoked. Only after all functions are defined does it then automatically invoke the setup() function for you, starting your sketch running. In other words, functions can be defined in any order.

But, make sure that all your functions are defined in global space. Functions cannot be defined inside other functions. (They actually can, but that is a more advanced topic that we will not touch on this semester. Javascript programmers might be familiar with this technique, as it is more common in that language.)

If you really want to keep your code organized and manageable, consider putting some functions in different tabs. You can make tabs with helpful and informative names, and then put different function definitions in them. Perhaps you have a tab called "User input" and a tab called "Draw code". Experiment with whatever works for you.

IMPORTANT UPDATE: Initially, I neglected to mention that if you want to use multiple tabs, and include other code in your tabs like function definitions, you need to use the import command in your main tab to be able to access those functions. Examples of how to use this is below.

This usage of functions is what is called modularity: breaking down a big task into smaller modules, that are themselves each more manageable. Remember that we read about modularity in the Lev Manovich chapter. You could imagine that I might continue expanding the above example with additional functions, and my draw() block might look like this:

```
def draw():
    drawLandscape()
    drawClouds()
    drawCar()
    moveClouds()
    moveCar()
```

Looking at this code, we don't know what each of those functions does, but we can start to get an abstract, high level understanding of what is going on in this sketch.

Functions can work really well with the topic of state variables from last week. For example, if you were doing the game option for the midterm, you could implement your different levels like this: NOTE: Please pay attention to how I'm using the import command in the main tab to import the function definitions from the other two tabs.

```
# First, main tab
from level_1 import *
from level_2 import *

level = 1

def setup():
    size(800,800)

def draw():

    # ... other code here ...

    if level == 1:
        drawLevel1()
    elif level == 2:
        drawLevel2()

    # ... more code down here ...
```

```	  
# Tab: level_1.py
def drawLevel1():
    # draw code goes here ...
```

```
# Tab: level_2.py
def drawLevel2():
    # draw code goes here ...
```

Keep this in mind as you work on the midterm!

## Drag and Drop Coding Exercise
lets debug this problem what's wrong with it?

```
x = []
y = []
rect_width = []
rect_height = []
mouse_pressed = False
def setup():
    size(1024, 1024)
    rectMode(CENTER)
    for i in range(0, 10):
        x.append(width/10 + width/10*i)
        y.append(height/10 + height/10*i)
        rect_width.append(150)
        rect_height.append(150)
    
def draw():
    global x, y
    background(255)
    for i in range(0, len(x)):
        rect(x[i], y[i], rect_width[i], rect_height[i])
        x[i], y[i] = checkBounds(x[i], y[i], rect_width[i], rect_height[i])
    
def checkBounds(x, y, rect_w, rect_h):
    if mouse_pressed:
        if mouseX > x - rect_w/2 and mouseX < x + rect_w/2:
            if mouseY > y - rect_h/2 and mouseY < y + rect_h/2:
                x += mouseX - pmouseX
                y += mouseY - pmouseY
    return x, y
            
def mousePressed():
    global mouse_pressed
    mouse_pressed = True
    
def mouseReleased():
    global mouse_pressed
    mouse_pressed = False
```
```
x = []
y = []
rect_width = []
rect_height = []
mouse_pressed = False
def setup():
    size(1024, 1024)
    rectMode(CENTER)
    for i in range(0, 10):
        x.append(width/10 + width/10*i)
        y.append(height/10 + height/10*i)
        rect_width.append(150)
        rect_height.append(150)
    
def draw():
    global x, y
    background(255)
    for i in range(0, len(x)):
        rect(x[i], y[i], rect_width[i], rect_height[i])
        x[i], y[i] = checkBounds(x[i], y[i], rect_width[i], rect_height[i])
    
def checkBounds(x, y, rect_w, rect_h):
    if mouse_pressed:
        if mouseX > x - rect_w/2 and mouseX < x + rect_w/2:
            if mouseY > y - rect_h/2 and mouseY < y + rect_h/2:
                x = mouseX
                y = mouseY 
    return x, y
            
def mousePressed():
    global mouse_pressed
    mouse_pressed = True
    
def mouseReleased():
    global mouse_pressed
    mouse_pressed = False
```
