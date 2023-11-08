def setupCharacter():
    global top_hat 
    top_hat = loadImage("Top_Hat_Transparent_Image.png")
    global mustache 
    mustache = loadImage("mustache-161330_1280.png")
    global elephant 
    elephant = loadImage("elephant_alpha.png")

def drawCharacter(x):
    pushMatrix()
    translate(x, 100)
    image(elephant, 0, 0, 300*1.4, 300)
    #image(mustache, 20, 100, 100*2, 100)
    image(top_hat, 150, -25, 75*1.25, 75)
    popMatrix()
    pass
    
