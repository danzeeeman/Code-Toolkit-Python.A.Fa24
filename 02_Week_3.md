# Code Toolkit: Python, Fall 2023
## Week 3 — Class notes

# Part 1 :: Your Books

## BREAK

# Part 2
## Review of what we've done so far

Python and Processing programs are comprised of commands, also known as statements, also known as instructions. Each exists on its own line. Statements are generally comprised of expressions and operators. Expressions are things that have a value, like the number 250, and operators are things that have effects, they do something, combining values in various ways.

## The grid system:

![Grid](/images/grid.png)

Processing is a programming platform designed for coding education around creative applications. Given that, it is very visual by default. Most (but not all) of our work this semester will have a visual output. In Processing that is primarily arranged around a draw window. The draw window is a grid of pixels. Each one like a little lightbulb that you can turn on or off and control the color of.

The draw grid starts at the top-left corner of the window at 0,0. The numbers that specify an individual pixel are called coordinates. We almost always refer to coordinates with x first, then y. x increases to right and y increases down.

On Mac you can use the screencapture utility to measure pixel values. On my computer the shortcut is ⌘-SHIFT-4, then click and drag, then press ESCAPE or else you'll end up with a bunch of funny screenshot fragments!

You can do this on Windows with Snippet Tool, but no global keyboard shortcut unless you make one.

### Color
Color is specified by default with three numbers which signify components red, green, and blue, or, RGB. Color specifications can also include a fourth number for transparency (alpha). Color can also be specified as HSB (hue, saturation, and brightness). 

Processing offers a color selector tool to help you with this. From the menu, specify Tools > Color Selector. You can find the color you want, and then copy/paste its value into your sketch. You can use either the three RGB numbers, or just copy/paste the hex value.

### Some syntax rules:
All text is case sensitive
Whitespace means spaces, line breaks, tabs, etc., and Processing mostly ignores this. So these are all equivalent:
```
rect(10,10,50,50)
rect( 10,10, 50,50 )
rect   (        10, 10,    50, 50 )
```
And you can use this to help make your code more readable. Personally, I find the first line above to be the easiest to read.
The exception to this rule is that spaces at the beginning of the line (called indentation) are very important and we'll talk more about this next week.

Commands use parentheses to specify parameters, also referred to as arguments. For example, in your homework you used commands like: ```rect(10,10,50,50)```. The parameters here are the four numbers.

Make sure your parentheses always come in pairs, open ( and close ).

Comments are bits of text that you can put in your code as notes to yourself, to me, or to anyone who might be looking at your code. They are like documentation. They are very useful and you should use them often.

Comments are specified two ways:

```
# With a hashtag symbol, which go to the end of the line
rect(10,10,50,50) # Single line comments can also start at the end of a line
```
or
```
"""
    Or with three quotation marks like this. This marks off a block of
    text and is useful for entering longer explanations, like
    describing what the program does for example.  At the top of all
    of your homeworks, please add a comment like this and include your
    name, date, assignment number, and any other comments. I would
    also like you to submit your reading notes this way
"""
```
### Class note style

In class notes I will indicate Processing code by highlighting :
  
  ```rect(250,250,100,50)```

Whenever text is formatted in this way, it is valid Python / Processing syntax.

Use the Processing PDE "Auto Format" command frequently, and always use the command before sharing your code when asking for help. In the menu: Edit > Auto Format (or ⌘T on Mac). This helps keep your code nicely lined up. For now this doesn't matter that much, but soon, as we learn new types of syntax, this will actually help you debug your code and help you see the structure of your programs.

Have you memorized the URL for the Python Processing reference yet Processing reference yet?!? Highlight the brackets to reveal: http://py.processing.org/reference

### Drawing Shapes

```rect(x, y, width, height)```
```
fill(255, 0, 255)
rect(250,250,100,50)
```

```ellipse(x, y, width, height)```
```
fill(255, 0, 255)
ellipse(0, 0, 512, 512)
```

```triangle(x1, y1, x2, y2, x3, y3)```
```
fill(255, 0, 255)
triangle(0, 0, 256, 512, 512, 0)
```

### Draw Order is important

```
size(300,300)
stroke(0,0,255)
fill(150,150,255,255) # 255 as alpha is equivalent to totally opaque
rect(50,50,200,200)
ellipse(250,250,50,50)
triangle(250,250,250,300,300,250)
```

### Raster images

```
img = loadImage("YOUR-IMAGE-FILENAME.jpg")
image(img, 0, 0)
```

## Variables
What is a variable?

#### _Who remembers algebra?_
  ```
  y = m * x + b aka the formula for a line
  ```

```Y``` is equal to the variable ```M``` times the variable ```X``` plus the variable ```B``` this gives us the forumla of a line where ```M``` defines the slope of the line and ```B``` define the point that the line crosses the ```Y``` axis, when ```x = 0```.

  ```
  a**2 + b**2 = c**2 aka Pythagorean Theorem
  ```
#### _Did anyone take Physics?_
  ```
  force = mass * acceleration 
  ```
####  _Did anyone take Calculus?_

![Cover](images/changing-stuff.jpeg)

A way to introduce variation on a theme, generalization within a formal structure, or the abstraction of some parts of a process.

The word comes from vary (dictionary.com) like variety and variance, and means a thing that is able to change.

![Bernd and Hilla Becher](/images/becher-khan.jpg)

The image on the left above is by the artist photographer couple Bernd and Hilla Becher. Examples of the Bechers' work like this one identify a kind of concept, and then stretch that concept by showing us all acceptable variations within that structure. A round gas water tank may have between 6 and 16 support beams, it may be on flat tiles or an elevated platform, it may have a diagonal staircase, it may be covered in a variable number of vertical streaks or it may be blotchy. This is not some objective, Platonic ideal, but rather it somehow portrays a truer representation of that concept because it shows us simultaneously all possible differences, all the ways that the structure can exist in the world.

The image on the right is by the artist Idris Khan. Khan takes collections of the Becher images (and other images), adds transparency, and layers them. In this way, it's like he is creating one image that shows us a fuzzy portrait that depicts the range of all possible items in a collection. One image of a gas tank that somehow portrays all possible gas tanks. We'll start with the Becher approach today and in your homework you will end with Khan's.

![Idris Khan](/images/idris%20khan%202%20-%20spherical%20gas.jpg)

(More examples of both bodies of work are available here.)

A variable is a placeholder. A placeholder for a value. Instead of using a specific value (like a number), you create a name, and then use that name in your code. When looking at your code, you don't know exactly what the value of that variable is. You can set it to a specific value, or change that value later. This means that one bit of code is now able to do different things.

This creates a kind of abstraction. Think of other examples of abstraction that you're aware of. Like maybe Cubism, for example. There is an aspect to this of being "not specific", somehow general in some sense. Thinking back to the recipe metaphor from week 1, think of a recipe that might say something like "now add your sweetener" or "now add your protein". Often recipes can also be halved, doubled, or tripled. The person following the recipe may modify the amount of something or swap out an equivalent item. But still the recipe would just say "now add the spices" — the recipe specifies the amount and kind of spices, but that amount may have changed, but still, the recipe can proceed without knowning the exact amount. This is what a variable allows.
Variables allow algorithms to have generality. So the google search algorithm works approximately the same whether the user is searching for "apples", "bananas", or "carrots". When you write code that uses variables, you don't know exactly what your code will do in advance.

A little more specifically:
- First you create a variable and give it a value
- Then you can use and re-use that variable in one or more places
- You can also change that value, and future uses will use this new value.
 
### How this works in Python Processing:
```  
  treeHeight = 50
  rect( 100, 100, 20, treeHeight )
```

Let's break that down and introduce some new vocabulary:

The first line creates the variable. In some programming languages, you have to _declare_ variables before you can use them. In Python, you don't have to do that. You simply create a variable by _using_ it: by using the placeholder name in your code.

![Matrix](/images/matrix_var_names.jpg)

![Graph](/images/var_meme.jpg)

_My advice is_ 

```
camelCase
makeItEasyToRead = 1

snake_case
make_it_easy_to_read = 1

camelCase
makeItMeanSomethingUnique = 1

snake_case
make_it_mean_something_unique = 1
```

An important rule is that you have to give the variable a _value_ before you can use it. Usually you do this as I did above, with an equal sign (=). This is called variable assignment, and the equal sign is sometimes called the _assignment operator_.


Read that equal sign almost like an arrow pointing from right to left. Variable assignment is a declaration. You are telling Python: "This placeholder that I'm calling ```treeHeight``` now contains the value ```50```." (Later we will use equal signs to ask Python what the value of a variable is, but for now, we are telling.)

```treeHeight``` is a name I made up. Your variables can be any name as long as they are not already special Python Processing words, like size() or rect(). (Some additional rules about variable names are below.) But you should use things that will be useful to you and others later when reading your code.
Please use good, informative variable names that describe what the variable will be used for.


The next line above is using the variable. After assigning it a value, you can use it over and over. You can also use it with arithmetic, and you can modify the value.
So if the above ```rect()``` draws a tree trunk, and I wanted to draw another tree with the same height to the right of it, I could say:

```
  # draw a second tree
  rect( 150, 100, 20, treeHeight)
```
And now I could change the value of the variable once and both tree heights would change.
Valid variable names:
* must start with a letter or the underscore character
* cannot start with a number
* can only contain alpha-numeric characters and underscores (A-Z, a-z, 0-9, and _)
* are case-sensitive (treeheight, TREEHEIGHT, TreeHeight, and treeHeight are all different variables)

Variables can be used for all sorts of values. This week we will primarily be working with variables that store numerical values. For example:
```
armLength = 100
curveAngle = PI/2
legToArmRatio = 1.5
```

Later in the semester we will be working with other values. For example:

```True``` / ```False``` values called booleans: ```isOn = False``` (This funny word is acutally a very common term in computer science that comes from George Boole, a 19th century mathematician who invented a formal system of logic, like an entire arithmetic that operates only on the values true and false instead of numbers. Booleans use keywords True and False to specify values.)
strings: ```name = "Dan Moore"```
characters: ```stopKey = 's'```
You can also use variables to store colors. So you could specify a color like this:
```
r = 255
g = 150
b = 150
fill(r,g,b)
```

Or, you could also specify a color with the color() command, which creates a color variable, like this:

```
c = color(255,150,150)
fill(c)
```

You can even use variables to store images, like this:
```
img = loadImage("clouds.jpg")
```

These different kinds of values are called types and we will be talking more throughout the semester about this idea of different kinds of placeholders.

Later in the semester you will even be able to create your own custom variable types.

Going back to the recipe metaphor, you can kind of imagine your variables as the ingredients list. Most recipes list all ingredients at the beginning so you know what to expect, and specify all the values, but later on only reference the item and not the quantity.
Processing comes with special some built-in variables. 

For example:

* ```width``` — the width of the draw window
* ```height``` — the height of the draw window

And some others we'll talk about next week:

* ```mouseX``` — the horizontal part of the mouse position
* ```mouseY``` — the vertical part of the mouse position
* ```pmouseX```
* ```pmouseY```

and others

## Arithmetic

![basic_math](images/1zp2du.jpg)

Arithmetic is done with the following operators:

### basic math and some __funky__ _shit_
* add (+)
  * a = 1 + 1
  * a += 2 or a = a + 2
* subtract (-)
  * a = 1 - 1 = 0
  * a -= 1 or a = a - 1
* multiply (*)
  * a = 2 * 2 = 4
  * a = 4 * 4 = 16
  * a *= 4 or a = a * 4
* divide (/)
  * a = 2 / 2  = 1
  * a = 1 / 2  = 0.5
  * a /= 2 or a = a / 2
* pow (**)
  * a = 2**2 = 4 
  * a = 4**2 = 16
  * a**=2 or a = a ** 2
* modulus (%) 
  ![wft](images/1y62g6.jpg) 
  *  a = 1 % 4 = 1
  *  a = 2 % 4 = 2
  *  a = 3 % 4 = 3
  *  a = 4 % 4 = 0
  *  a = 5 % 4 = 1
  *  a = 6 % 4 = 2
  * a %= 4 or a = a % 4

#### PURE PYTHON
```
# take two variable, assign values with assignment operators
a=3
b=4

print("a: "+str(a))
print("b: "+str(b))

# it is equivalent to a=a+b
a+=b

print("a: "+str(a))
print("b: "+str(b))

# it is equivalent to a=a*b
a*=b
print("a: "+str(a))
print("b: "+str(b))

# it is equivalent to a=a/b
a/=b
print("a: "+str(a))
print("b: "+str(b))

# it is equivalent to a=a%b
a%=b
print("a: "+str(a))
print("b: "+str(b))

# it is equivalent to a=a**b ( exponent operator)
a**=b
print("a: "+str(a))
print("b: "+str(b))

# it is equivalent to a=a//b ( floor division)
a//=b
print("a: "+str(a))
print("b: "+str(b))
```

```
#create two variables
a=100
b=200

# addition (+) operator
print(a+b) 

# subtraction (-) operator
print(a-b) 

# multiplication (*) operator
print(a*b)

# division (/) operator
print(b/a)

# modulus (%) operator
print(a%b) # prints the remainder of a/b

# exponent (**) operator
print(a**b) #prints a^b
```

Question: So how would you draw a shape in the center of the window, and make sure it was in the center no matter what the window size was? (Highlight below to see the answer.)
```
  ellipse( width/2, height/2, 50,50 )
```

### Example
Let's work through an example. Start with this code:

```
  size(600,600)
  background(255)
  stroke(100,100,100)

  fill(255,100,100,100)
  rect(250,100,100,100)

  fill(255,255,100,100)
  rect(250,200,100,100)

  fill(100,100,255,100)
  rect(250,300,100,100)
```

What if we want to make the first square wider? What should we change? Check the Processing reference:


So we need to change the third parameter of the rect() command. And since we want the square to be wider, we'll make that number bigger.

```
  size(600,600)
  background(255)
  stroke(100,100,100)

  fill(255,100,100,100)
  rect(250,100,200,100)

  fill(255,255,100,100)
  rect(250,200,100,100)

  fill(100,100,255,100)
  rect(250,300,100,100)
```

OK great. And if we want the other two squares to also be the same width, we could change them too:

```
  size(600,600)
  background(255)
  stroke(100,100,100)

  fill(255,100,100,100)
  rect(250,100,200,100)

  fill(255,255,100,100)
  rect(250,200,200,100)

  fill(100,100,255,100)
  rect(250,300,200,100)
```

But now what if we wanted to play with this width a bit, make some adjustments. We'd have to keep changing all three rect() commands each time. Since we want them all to have the same width, we can use a variable as a placeholder for this value. Here's how:

``` 
  squareWidth = 200 # variable assignment (creates the variable)

  size(600,600)
  background(255)
  stroke(100,100,100)

  fill(255,100,100,100)
  rect(250,100,squareWidth,100)

  fill(255,255,100,100)
  rect(250,200,squareWidth,100)

  fill(100,100,255,100)
  rect(250,300,squareWidth,100)
```

Now to make tweaks, I can simply change the value (200) in the variable assignment, and all my squares will be drawn using this value. (Note: my variable name, squareWidth is arbitrary and can be anything I want. I could have called it spaghetti and I just chose a name that would be informative to the purpose for which I was using it.)

Let's keep going. What if we wanted to make the first square taller? Let's change it's height and see what happens.

```
  squareWidth = 200 # variable assignment (creates the variable)

  size(600, 600)
  background(255)
  stroke(100, 100, 100)

  fill(255, 100, 100, 100)
  rect(250, 100, squareWidth, 120)

  fill(255, 255, 100, 100)
  rect(250, 200, squareWidth, 100)

  fill(100, 100, 255, 100)
  rect(250, 300, squareWidth, 100)
```

If you run that, you'll see that the first square is taller, but now there is an overlap between the first and second square. What if we want the other two squares to automatically adjust their position?

Let's add a variable for the first square's height, and use that to position the second square. Like this:

```
  squareWidth = 200 # variable assignment (creates the variable)
  firstSquareHeight = 120

  size(600, 600)
  background(255)
  stroke(100, 100, 100)

  fill(255, 100, 100, 100)
  rect(250, 100, squareWidth, firstSquareHeight)

  fill(255, 255, 100, 100)
  rect(250, 100 + firstSquareHeight, squareWidth, 100)

  fill(100, 100, 255, 100)
  rect(250, 300, squareWidth, 100)
```

OK, looks good. So now we can adjust just the value of the variable firstSquareHeight and it's height will change, and the second square will move accordingly.

But now we have the same problem with the third square! So we have to repeat the pattern. The vertical postiion (y) of the third square should be the top point of the first square, plus the height of the first square, plus the height of the second square. So we can write that out, like an equation.

```
  squareWidth = 200 # variable assignment (creates the variable)
  firstSquareHeight = 300

  size(600, 600)
  background(255)
  stroke(100, 100, 100)

  fill(255, 100, 100, 100)
  rect(250, 100, squareWidth, firstSquareHeight)

  fill(255, 255, 100, 100)
  rect(250, 100 + firstSquareHeight, squareWidth, 100)

  fill(100, 100, 255, 100)
  rect(250, 100 + firstSquareHeight + 100, squareWidth, 100)
```

Note that if firstSquareHeight is 100 (it's original value above), then this equation works out to 300, which was its original value above as well.
Great. So now we can change only the variables squareWidth and firstSquareHeight and the composition will adjust accordingly.

To keep going, can you add a variable for the x position of the squares, and have that adjust the position of all three squares? What if you add two more squares to make a small cross ("+" sign) and want the composition to adjust accordingly?

So, how much "variance" can you achieve with 1 variable? with 2?

How many variables would you need to draw a shape that varied its height, and also its horizontal and vertical position?
Let's say you were trying to implement Pong for your midterm project. (A totally feasible project by the way!) How may variables would you need? What is moving or changing in this game?


## Randomness
One thing that works really nicely with variables is creating randomized variation of those variable values. You will need this for your homework this week.
In Processing, this is done with the command random(). For a detailed explanation, check the Processing reference for random().
```random()``` returns a floating point (a number with a decimal point).
Like this:
```
	  firstSquareHeight = random(10,300)
```
The parameters to random() are minimum and maximum values. They define a range from which random() chooses a number. Like asking a person to "pick a number between 10 and 300".
Putting that altogether, here is how we could use random values to draw the above composition:
```
  squareWidth = random(10,300) # variable assignment (creates the variable)
  firstSquareHeight = random(10,300)

  size(600, 600)
  background(255)
  stroke(100, 100, 100)

  fill(255, 100, 100, 100)
  rect(250, 100, squareWidth, firstSquareHeight)

  fill(255, 255, 100, 100)
  rect(250, 100 + firstSquareHeight, squareWidth, 100)

  fill(100, 100, 255, 100)
  rect(250, 100 + firstSquareHeight + 100, squareWidth, 100)
```

Stop and run that a few times to see what kinds of variation we've just created.


# Homework
### Explore the Examples
![Homework](images/lewitt-trapezoid.jpeg)
