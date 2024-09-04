# Code Toolkit: Python, Fall 2023
## Week 2 — Class notes
# Reading Discussion
### This is a change
_So what did everyone think of the reading?_
_Did you do the reading?_

Marshall McLuhan made some interesting statements huh?

_With any piece of art or design, there is an explanation behind the medium through which we choose to share our work. Whether it relates to the context, adds to the message, or is the easiest way to gather a wider audience._


Marshall McLuhan wrote:

_The title "The Medium Is the Massage" is a teaser—a way of getting attention. There's a wonderful sign hanging in a Toronto junkyard which reads, 'Help Beautify Junkyards. Throw Something Lovely Away Today.' This is a very effective way of getting people to notice a lot of things. And so the title is intended to draw attention to the fact that a medium is not something neutral—it does something to people. It takes hold of them. It rubs them off, it massages them and bumps them around, chiropractically, as it were, and the general roughing up that any new society gets from a medium, especially_


More importantly I want you to take away this:

The communication channel used to communicate any message shapes the message itself.  So if you see a instagram ad that ad was manufactured to get _you_ to click it.  That promoted 288 Character xheet was crafted to get you to pay attention to it.  That TikTok, was engineered to be captivating for the first 7 seconds. Remember that the way a message is communicated influences the design and execution of the message itself.

### Discussion Question: 
[miro](https://miro.com/app/board/uXjVKmKDkns=/)
- _what are some of the theme is the reading?_
- _how does writing code to communicate shape your message?_
- _what do you want to talk about? and how are you using code to tell that story?_
- _what can you do when the communication channel is interactive and response?_

Continuing Education in Media Studies read [Manufacturing Consent by Edward S. Herman and Noam Chomsky](/pdfs/Manufacturing%20Consent%20%5BThe%20Political%20Economy%20Of%20The%20Mass%20Media%5D.pdf) and write a short (2-6 pages double-spaced ~800-1500 or 5000 words) essay on the _Propaganda Model_ (this will replace 2 missed coding homeworks if you are struggling)


# _A crash course to git_
## _how to get the classnotes_
- Create a [Github](https://github.com) profile
- Install Git
  - On Windows 
    - Install [git](https://git-scm.com)
    - open git-cmd [see screen shot] ![terminal](images/terminal.PNG)
    - go to cloning
  - on Mac 
    - install [brew](https://brew.sh)
    - open terminal ![terminal](images/CloneMac.png)
    - install git
      - type ```brew install git``` into your terminal
    - go to cloning
  - Clone the repo: 
    - type ```git clone https://github.com/danzeeeman/Code-Toolkit-Python.A.Fa23``` into the terminal

```
git clone your_repo_url
```
![terminal](images/CloneMac.png)
Cloning a repository of code is basically making a copy but with 
- Copy the _template_ folder and rename it to your chosen name
```
git add path_your_new_file_folder_name/*
git commit -a -m "adding my homework folder where I will store all of my homework"
git push origin main
```

## Install the PDE:
Download the version of Processing that fits your computer:

- [Processing Windows](https://github.com/processing/processing4/releases/download/processing-1293-4.3/processing-4.3-windows-x64.zip)
- [Processing Intel Mac](https://github.com/processing/processing4/releases/download/processing-1293-4.3/processing-4.3-macos-x64.zip)
- [Processing Apple Silicon](https://github.com/processing/processing4/releases/download/processing-1293-4.3/processing-4.3-macos-aarch64.zip)

### Install Python



# Part 2 :: Introductory Beep Boops 

Let's write a simple "program"

```
print('Hello World')
```

This is the most written program in the world. It is an example in every language.  It comes form _The C Programming Language_ sometimes referred to as _K&R_ for the Authors', Brian Kernighan and Dennis Ritchie, initials. 

```
main( ) {
        printf("hello, world");
}
```

But the first instance of it being used is from K's 1972 _A Tutorial Introduction to the Language B_ (B came before C)

```
main( ) {
    extern a, b, c;
    putchar(a); putchar(b); putchar(c); putchar('!*n');
}
 
a 'hell';
b 'o, w';
c 'orld';
```

If you want to get really low-level you can learn C by looking how to write [arduino](https://www.arduino.cc/) programs. 

## How to make a drawing

There were some things that many of your drawing instructions did that we will see again later:
placeholders: things like "the first square", "the bottom line". 

*In computer programs these are called variables*

repetition: "do this 4 times", "do this until you connect back to the first line". 

*In computer programs these are called loops*

questions or conditions: "if the shape is not closed, keep drawing". 

*In computer programs these are called conditionals* 

groups of commands: "draw another shape like you did in steps 1-4". 

*In computer programs these are called functions and they are a way to make a group of instructions with a name for re-use*

So how does all this translate to Processing?

## Introducing the Processing Development Environment

Let's get started by opening up the Processing Development Environment, or PDE, and look around:
* play button
* stop button
* File > Open
* File > Examples
* Modes: Java & Python

In Processing, a program is called a "sketch".

Let's make a very simple example:
```
size(300,300)
stroke(0,0,255)
fill(0,255,0)
rect(50,50,200,200)
```
```Click File > New > Save``` 
This creates a new folder for this sketch. Note the location. It is probably in a folder called Processing in your Document folder Give the sketch a name and click "Save".

## 2D drawing basics (a.k.a 2D primitives)

*The basic commands to draw shapes are called 2D primitives*

In Processing, we mainly draw using coordinates. Keep in mind a grid where the top-left corner is 0,0. The horizontal dimension is always specified first and is referred to as ```x```, and the vertical dimension is always specified second and is referred to as ```y```.

![GRID](images/grid.png)

```x``` increases as you move to the right, and ```y``` increases as you move down.

So in the following example, what are the coordinates of this pixel?

Highlight this text for an answer: ```x=2```, ```y=3```. Remember, we start counting from 0.
What about in this example: what are the coordinates of this pixel?

Please don't actually count all those pixels! Let's just approximate. Maybe, ```x=30``` and ```y=15```? That seems about right.
Computers require us to be precise. But we can comply with that precision while also being loose and approximate in achieving the goals that we're working toward. We can leave space to play, experiment, estimate, and work by trial-and-error.


Let's look at one command in the [reference](https://py.processing.org/reference/): ```rect()```


```rect(x, y, width, height)```
```
fill(255, 0, 255)
rect(0, 0, 512, 512)
```

The numbers in parenthesis are called ```parameters``` and their order is very important. The [reference](https://py.processing.org/reference/) will tell you what the various ```parameters``` do. In this case, the [reference](https://py.processing.org/reference/) explains that the first parameter is the "```x```-coordinate of the rectangle", the second parameter specifies the ```y``` coordinate, the third is the ```width``` of the shape, and the fourth is the ```height```


*Some comments on lecture note format & style*

Throughout all my lecture notes this semester, I will indicate Processing code by highlighting like so:

```rect(250,250,100,50)```

or

```
rect(250,250,100,50)
```

Whenever text is formatted in this way, it is valid Python Processing syntax. You should be able to copy/paste it into your PDE. I will try my best to also use this formatting when specifying code in my emails, but I can't promise total consistency there as that can get quite tedious.


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

Let's look at this ```fill``` function that we keep calling.  Fill sets the fill color for our shapes.

Color is specified using red, green and blue components, called ```RGB``` color. ```Tools > Color Selector``` gives you a helpful tool for selecting colors.  You can also use hue, saturation and brightness, called ```HSB``` color, if you specify that with the ```colorMode()``` command. Let's modify the above example:

```
size(300,300)
stroke(0,0,255)
fill(150,150,255)
rect(50,50,200,200)
```

```fill(r, g, b)```

```
fill(255, 0, 255)
```

```stroke(r, g, b)```
```
stroke(255, 255, 0)
```

You can always add a fourth argument to any color commands to specify alpha which is a common digital media term that means transparency: how see-through a digital image is.

```
size(300,300)
stroke(0,0,255)
fill(150,150,255,50)
rect(50,50,200,200)```
That might not seem very different but if we add a new shape it should be more apparent:
```
```
size(300,300)
stroke(0,0,255)
fill(150,150,255,50)
rect(50,50,200,200)
ellipse(250,250,50,50)
```
Notice that the overlap is slightly darker.

## Draw Order

Drawing order is also important. Intructions are followed from top down, first things first. Lower commands are run later. This means that later drawn shapes will be drawn as if layerd on top of earlier ones. So it's like making a collage: the things that you place down later will be on top.
Let's add a third shape and remove the transparency to see what I mean:

```
size(300,300)
stroke(0,0,255)
fill(150,150,255,255) # 255 as alpha is equivalent to totally opaque
rect(50,50,200,200)
ellipse(250,250,50,50)
triangle(250,250,250,300,300,250)
```

### Some syntax rules
Parenthesis must always come in pairs, open and closed: ```( )```

Processing will try to help you with text highlighting and helpful error messages. If you are confused, check the [reference](https://py.processing.org/reference/) for relevant examples.
Comments are also an important part of coding. They are how you communicate with others (and with yourself in the future!) about what your code does. There are two ways to add comments in Python:

```
# Using a hashtag symbol creates a single line comment, like this
```
Single-line comments can also start midway through a line

```
rect(10,10,10,10)  # like this
```

```
"""
  Using three quotation marks, you can create a comment for a block of
  text, like this. Use this at the top of your files to include your
  name, date, and what this code is for (such as homework week number
  or project)
"""
```
  
# Gut Check 
How are those books coming?

# One on Ones


# Home Work
## Explore the Processing Python Examples
## Lewitt Trapezoid
![Homework](images/lewitt-trapezoid.jpeg)
