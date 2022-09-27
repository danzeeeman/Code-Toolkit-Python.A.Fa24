# Code Toolkit: Python, Fall 2022
## Week 5 — Wednesday, September 28 — Class notes

## Review of last week

Last week we learned about conditionals and the syntax of if and elsestatements, along with elif, and we used this to respnd to user-triggered events. Broadly, this could be divided into three topics:

We looked at the syntax for three kinds of blocks:

```
if conditional:
  # instructions here
```

```
if conditional:
  # instructions here
else:
  # instructions here
```

```
if conditional:
  # instructions here
elif conditional:
  # instructions here
else:
  # instructions here
```

The conditional is comprised of an expression that evaluaates to a Boolean value. These allow us to ask questions about the status of our program. Things like: "Is the mouse being pressed?" "Is the mouse on the right side of the screen??" "Is the size of this shape greater than 200 pixels?"

Inside the code blocks (the indented lines after a colon) go any arbitrary Python / Processing statements and commands, which get executed if the conditions are met (if they evaluate to True).

Boolean expressions are variables that evaluate to True and False (like mousePressed or keyPressed) together with boolean operators that allow us to combine these True and False values to make more detailed conditions.

In Python, the boolean operators are:

* and meaning both parts must be True
* or meaning at least one part must be True
* not meaning the thing that follows must be False

In addition to these boolean operators, we can also ask questions about numbers, using comparison operators:

* less than (<) meaning the value on the left must be less than the value on the right
* greater than (>) meaning the value on the left must be greater than the value on the right
* equal to (==) meaning both values must be equal. Remember: this is different from the assignment operator, which only uses one equal sign (=). 
* less than or equal to (<=). This is a shortcut. It is very useful, but can always be written another way. For example: x <= 10 could also be written as x < 10 or x == 10, or if you're working with whole numbers, as x < 11.
* greater than or equal to (>=). Same as above.

We also looked at several new special Processing variables:

```mousePressed```: a Boolean variable that is True whenever the mouse is being pressed

```keyPressed```: a Boolean variable similar to the above that is True whenever any key is being pressed.

```key```: a variable that contains a string (text in single or double quotes, 'a' or "s") of whichever character the user has most recently pressed. You can check this value by specifying a string literal with quotes and using the comparison operator for equality:

```
if key == 'a':
```

And lastly, we looked at two new kinds of blocks for event handling:

```
def mousePressed():
    # code instructions
```

and

```
def keyPressed():
    # code instructions
```

Unlike the special variables ```mousePressed``` and ```keyPressed```, these blocks respond to every mouse or key press. That means that each user action will trigger the code in these blocks exactly once, and it is not depending on the current frameRate of your program.
If any of that remains confusing, please review the class notes from last week or reach out for help.

## Adding repetition
Today we will learn how to create repetition with our code. This is one of the most powerful concepts within software. So far this semester we have learned:

* how to create and use variables, to create a media object that can dynamically change,
* how to create interactive programs, that use dynamic variables to chnage in response to user input
* how to use conditionals to check for different situations within our code and render or respond to them differently.

And all of these things are essential components of software.
But repetition is another key concept that is at the core of what software does.

The kind of repetition that we are going to learn today allows you to write a program that does something hundreds, thousands, millions, or billions of times. Whenever you hear people talking about the power of software to proces "big data", or to search through billions of web pages, they are referencing the ability of software to implement some kind of repetition. It lets you write a piece code, and then repeat that an inhuman number of times.

Creative inspiration
But first, let's consider some examples of related creative work that explores these kinds of forms, which we can draw on for inspiration this week.

Sol Lewitt

![Sol Lewitt](images/sol-lewitt-colorful.jpeg)

Conceptual Art was a movement that rose to prominence in the 1960s, made popular by artists such as Sol Lewitt and Yoko Ono. This body of work put more emphasis on the idea or the concept of the artwork, more than the technical or material implementation or rendering. In Conceptual Art, the artwork was considered to be the idea itself, with various instantiations relegated to a lower priority, or ignored altogether.

As Sol Lewitt wrote in his essay "Paragraphs on Conceptual Art" (June 1967, Artforum) "When an artist uses a conceptual form of art, it means that all of the planning and decisions are made beforehand and the execution is a perfunctory affair. The idea becomes a machine that makes the art."

Yoko Ono

![Yoko](images/yoko-ono-kitchen.jpeg)

![Yoko](images/yoko-ono-sandwich.jpeg)

If this idea sounds a lot like computer programming to you, you wouldn't be alone. Several digital artists have drawn inspiration from Conceptual Art to draw parallels in the ways that with software and other digital media, we often create machine configurations that themselves produce cultural objects.

In fact, one of the creators of Processing, Casey Reas, produced a 2004 Processing project related to Lewitt's work: {Software} Structures project at the Whitney, curated by Christiane Paul.

Beyond this general connection to software, this week we'll look at Sol Lewitt's work as an example of creative experimentation with formal pattern and repetition. This video documents a 2008 installion of his work at MoMA:

Behind the Scenes: Wall Drawing #260

In addition to the way that Lewitt uses language to create something like a computer program to generate a drawing, let's also pay attention to the way that he uses logic, combinatorics, and repetition, rendered here in the form of a grid of geometric shapes.

There are several installations of Sol Lewitt's work throughout New York City. One of his line drawings was recently installed in the library at Pratt University in Brooklyn, which you could make arrangements to go see. Another huge colorful piece is at the 59th Street / Columbus Circle subway station. And another is in the lobby of 55 West 13th St (at Sixth Ave), on the campus of The New School.

## Loops
To add repitition in a computer program, we use loops.
You have already seen one kind of repetition in your sketches. Remember from week 3 that all the code inside the draw() block gets repeated many times, once per frame, depending on the frame rate of your sketch:

```
def draw():
    # This block of code runs many times
```

This is definitely a kind of repetition. Remember the movie metaphor: without ```setup()``` and ```draw()``` your code creates a static image like a photograph. But with these, your code is like a film: a sequence of frames played quickly, giving the illusion of motion. Every time ```draw()``` runs, it outputs one frame.

But the repetition that we are talking about today is for drawing multiples within one frame. So it is a way to go from images like the left, to images like the right:

 
So how does it work? First some pseudocode:

```
while some question is True:
    Run some commands over and over.
```

The question is a Boolean expression, which, as we talked about last week, is one or more Boolean variables combined with boolean operatorsor comparison operators asking questions about the values of variables. And the commands in the block are any arbitrary commands.
What this does is execute all the commands, in order, over and over again, as long as the conditional is True — i.e. "while" it is true, hence the name.

The actual syntax for this new structure is the following:

```
while conditional:
    # run some commands
```	    

That's still a little abstract, so let's work through a specific example.
Let's start with the following code:
```
size(600,600)
background(255)
fill(100, 100, 250)
rect(200,200, 200,20)
```
Now say we want to add two more rectangles. We could copy/paste and change some values like this:
```
size(600,600)
background(255)
fill(100, 100, 250)
rect(200,100, 200,20)
rect(200,200, 200,20)
rect(200,300, 200,20)
```
That's fine in this case, but what if we now wanted to add 10 or 100 or 1000 more. And what if we then wanted to change the width for each one. This could get tedious really quickly. So let's see how we could do it with a while loop.

```
size(600,600)
background(255)
fill(100, 100, 250)
i = 100
while i <= 300:
  rect(200,i, 200,20)
  i = i + 100
```

Mentally step through that code and make note of each value of i. Notice that the above loop is functionally equivalent to the three separate rect() statements above.

This introduces some new vocabulary.

The variable assignment: i = 100. This defines what we will call the looping variable. This is the variable that will be used to control the number of repetitions of the loop.
The boolean operator: i <= 300. This works just like an if statement, so we can call this the conditional or the check, as in "the check to continue".
The last line (i = i + 1) modifies the looping variable, and usually increases the value, so we can call this or increment. (Or decrement, if it were being decreased.)

Another term from computer science for looping is iteration, a fancy but commonly used term in computer programming that simply means repeating in this way. Looping is also referred to as iterating, and one might describe repetition like this as an iterative style of programming. (There are other styles, such as recursive, but we won't talk about those.)

Some notes on this new syntax:

Unlike with other variables, I highly recommend that you always create your looping variables right before your while loop, even if you are inside another block, such as draw() or an if statement. This will give the variable local scope and will make things a little easier to keep track of.
I recommend always putting your increment as the last line in the while loop block. This will also help you keep track of things and make it easy to check that you are properly incrementing your looping variable.

In the past I have said to always use informative variable names. And you can do that here, but it is common practice to simply use short, one-letter names for looping variables. Common choices are i, j, or n. So feel free to do that. Of course, if you have many loops and you want to help keep track of them, using more informative names for looping variables might help, like personNumber.
Common errors

```println()``` can be very useful here. Try putting a ```println()``` inside a loop to see how the value of the looping variable changes. This works well in static mode, because the loop will run once, but can be very hard to read in interactive mode, beacuse the loop will run every frame, many times per second.

Don't forget to increment your looping variable!!!!! This happens so frequently. So I'm telling you now: do not forget!!

What happens if you forget the increment? Try removing it (or commenting it out) in the above example, running your code, and seeing what happens. Probably nothing will show up on the screen, and you might even have trouble exiting the program. If you do, go to the PDE and click Stop instead of simply trying to click on the "x" to close the window. This is because your while loop never exits! It never completes, so your program hangs, running in this loop forever. This is called an infinite loop and should always be avoided (for now). Make sure that you are incrementing your looping variable, and that eventually the conditional check will be met.

For example, the following code example would never terminate:

```
i = 100
while i <= 300:
    i = i - 50
    rect(200,i, 200,20)
    i = i + 50
```

Do you see why? Step through the loop a few times in your mind to think about what happens to the values of i.
We could call this the "two steps forward, two steps back" loop. That might seem like a silly thing to do, and that infinte loop could be easily caught and fixed. But sometimes you may encounter cases that are harder to catch.

Getting back to our original example. Now we have a flexible way of adding more repetitions. If we want to add more rectangles, there are several ways.

```
# This makes more rectangles because
# they are spaced more closely together
size(600,600)
background(255)
fill(100, 100, 250)
i = 100
while i <= 300:
    rect(200,i, 200,20)
    i = i + 50
```

```
# This makes more rectangles because 
# they extend further down in the window
size(600,600)
background(255)
fill(100, 100, 250)
i = 100
while i <= 600:
    rect(200,i, 200,20)
    i = i + 100
```

Experiment with this and see what you get.

So, that saves us some typing. But there are even more interesting things about loops. For example, what if you wanted to modify what you were doing inside the loop each time you did it. Let's move fill() from outside the loop block to inside, and modify its value with the looping variable:

```
size(600,600)
background(255)
i = 100
while i <= 250:
    fill(i,100,200)
    rect(200,i, 200,20)
    i = i + 50
```

Mentally stepping through this loop, we see that the parameter to fill() change each time the loop runs. The values will be:
```
100,100,200 blue
150,100,200 more red
200,100,200 even more red
250,100,200 purplish
```
giving us a nice gradient.

We can also use the looping variable to modify other things about the shapes we're drawing. For example, the width of rect():

```
size(600,600)
background(255)
i = 100
while i <= 250:
    fill(i,100,200)
    rect(200,i, i,20)
    i = i + 50
```

So we can use loops so that the commands we are running repeatedly can change a little each time.

But we can even do more. Using loops, we can do things a dynamic number of times. For example, let's put our sketch in active mode and use a dynamic variable in the while loop conditional:

```
def setup():
    size(600,600)

def draw():
    background(255)
    i = 100
    while i <= mouseY:
      fill(i,100,250,100)
      rect(200,i, 200,20)
      i = i + 50
```

Try mentally stepping through this loop. When this code runs, the number of repetitions is determined dynamically, when the sketch runs, based on user input. This is exciting because so far the number of things that you've been drawing has always been fixed in advance.
Even when you had lots of dynamism in your compositions, the number of things that you were drawing were always in a sense hard-coded. Now, the number of things themselves can vary.

Well, it is true that you have already been able to allow the user to draw many shapes by dragging the mouse around the screen, but this only worked by removing background(). Now you can draw a dynamic number of things while changing the background. For example:

```
def setup():
    size(600,600)

def draw():
    background( random(200,255) )
    i = 100
    while i <= mouseY:
      fill(i,100,250,100)
      rect(200,i, 200,20)
      i = i + 50
```

This would not be possible without loops.
Another new possibility here is to combine loops in interesting ways.

Let's say that instead of simply drawing a rectangle in a loop, you wanted to draw many things. Let's go back to static mode and start with this example:
```
size(600,600)
background(255)
i = 100
while i <= 250:
    fill(i,100,200)

    rect(200,i, 25,25)
    rect(300,i, 25,25)
    rect(400,i, 25,25)

    i = i + 50
```
Now inside the loop we're drawing three squraes with each iteration. Note the highlighted values. They are changing, increasing in an incremental pattern.
When you see values incrementing like that, think back to the original example today and think how you could write that instead.

We can replace those three rect() statements with a loop — even though we are already inside a loop.
```
size(600,600)
background(255)
i = 100
while i <= 250:
    fill(i,100,200)

    j = 200
    while j <= 400:
        rect(j,i, 25,25)
        j = j + 100

    i = i + 50
```
Mentally step through one iteration of the i loop, and see how it is equivalent to one iteration of the previous code snippet.

Now, just like with the example that started off this lesson, now we can ask: what if we now wanted to add 10 or 100 or 1000 more squares? And what if we then wanted to change the width for each one?

What we have here is called a nested loop and is a very powerful idea. In pseudocode, you could think of it like:

  Repeat many times,
    Each time through, repeat many times
      Run some commands each time
In this example, we've adding an entirely new inner loop here, with a new looping variable j, but it is inside the original loop.

The outer "i loop" repeats four times (for i equal to 100, 150, 200, and 250). And each time it repeats, the inner "j loop" repeats three times (for j equal to 200, 300, and 400). So how many rectangles will there be total? 4 x 3 = 12.

Nested iteration multiplies the number of repetitions. Think of this kind of repetition as working in two dimensions. Instead of repeating in a linear fashion, it can be used to create a grid.

Note that each row of squares is the same color. Why? Where is the fill() statement? It is inside the "i loop" but outside of the inner "j loop". In other words, for each iteration of the outer loop, the color is changed, then the inner loop repeats three times without changing the color. (Then the outer loop repeats again.)

Better loop organization

Writing loops in the above way is fine, but there is a slightly different way of working out the math of loops that is in many ways more powerful and easier to keep track of. Compare the following two examples:

```
size(600,600)
background(255)
i = 100
while i <= 400:
    fill(i,100,200)
    rect(200,i, 25,25)
    i = i + 100
```

```
size(600,600)
background(255)
i = 1
while i <= 4:
    fill( i*100, 100,200)
    rect(200, i*100, 25,25)
    i = i + 1
```
Stepping through both examples, it should be clear that both are functionally equivalent. Both result in the following fill() commands:
```
fill(100,100,200)
fill(200,100,200)
fill(300,100,200)
fill(400,100,200)
```
And corresponding rect() commands for each.
But there are several advantages to the version on the right side.

If I were to ask you how many times each loop repeats, you could step through the left side and do the math, but you could also quickly glance at the right side and probably figure it out much more quickly. Of course, the math inside the loop is a little more complicated, but it is more obvious and apparent how many iterations are taking place.

You should feel free for now to work with whichever is more clear to you. But next week when we start to look at arrays, it will be essential to use the right side style. So it is good to start thinking about it now. And there are certain kinds of functionality that are much easier to implement with the right side style, as we'll see next.

I've mentioned that you are able to put any arbitrary commands inside the while block. Let's see an example of doing something inside a loop that is a little more complicated than merely drawing squares. Let's start with some pseudocode:

```
  Repeat 10 times
    Each time through,
    Alternate the fill color between red and blue
    Draw a square
Wait, "alternate"?? Let's try to get more specific:
  Repeat 10 times
    Each time through,
    If we're on an even numbered repetition, set the fill to red
    If we're on an odd numbered repetition, set the fill to blue
    Draw a square
```
OK, we're getting into something that we can work with in Processing syntax.
We can use our looping variable somehow. But how do you determine if a number is even or odd?

Rember the ```%``` mod operator?  


```
size(600,600)
background(255)
i = 1
while i <= 4:
    if i % 2 == 0:
      fill( 255,0,0 )

    if i % 2 == 1:
      fill( 0,0,255 )

    rect(200
    , i*100, 25,25)
    i = i + 1
```
This would be a great occasion to use else, so let's re-write it that way:

```
size(600,600)
background(255)
i = 1
while i <= 4:
    if i % 2 == 0:
      fill( 255,0,0 )
    else:
      fill( 0,0,255 )

    rect(200, i*100, 25,25)
    i = i + 1
```

Read this as: "If i is even, then set the fill color to red, otherwise set it to blue."
What if we want to alternate colors in a grid? Thinking of a grid — i.e. repetition in two dimensions, horizontal and vertical — should immediately trigger thinking in terms of a nested loop: repeating, and for each iteration, repeating again.

For this, we can put together everything from this lesson into the following example:

```
size(600,600)
background(255)
i = 1
while i <= 4:
    j = 1
    while <= 4:
        if (i + j) % 2 == 0:
            fill( 255,0,0 )
        else:
            fill( 0,0,255 )

      rect( j*100, i*100, 25,25)
      j = j + 1

    i = i + 1
```

## for loops 

All the above discussion is about while loops. There is another kind of syntax for creating loops that looks a little different but achieves the same behavior: for loops. These two different constructs are veyr similar but not precisely equivalent.

In generla, programmers tend to use for loops more commonly than while loops, but I find that the syntax of while more clearly illustrates the principles of looping in a way that is more easily readable by new programmers. Feel free to use whichever loop style you like and whichever is more clear to you.

The following two examples show how to translate between one and the other:

```
i = 0
while i < 10:
    println("i = " + str(i))
    rect(i,i,5,5)
    i = i + 1
```

and

```
for i in range(10):
    println("i = " + str(i))
    rect(i,i,5,5)
```

Both examples contain: a variable declaration and a boolean expression. But the variable increment works differently in each case. In the while loops that we have been working on in this lesson, the increment is clearly discernible on its own line. In the for loop case, the increment happens kind of implicitly, because the Python range() command generates a list of numbers, and the variable i is automatically set to each number in an iterative way.

What is a list, you may ask? We'll talk about this next week.

I will say that one advantage of the for loop is that it's nearly impossible to forget to include your variable increment, making it less likely to accidentally produce an infinite loop.

## Home Work
* Coding Assignment #4.a: Create a Endless animation using primitives: Circle, Square, Rectangle, Triangles
* Coding Assignment #4.b: Create a Endless animation using found objects   
    * MEMEs will be judged by their Dankness