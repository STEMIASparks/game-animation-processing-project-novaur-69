x1 = 30
x2 = 30
ballx = 350
bally = 350
speedx = 1.9
speedy = 1.9

def setup():
    size (700,700)
    background(0)
    
def draw():
    global ballx,bally,x1,x2,speedx,speedy
    background (0)
    circle (ballx,bally,55)
    fill (246,120,78)
    rect(x1, 20, 100, 20)
    fill (80,257,69)
    rect(x2, 600, 100, 20)
    fill (100,224,240)
    #makes ball move
    ballx = ballx-speedx
    bally = bally+speedy
    if bally >= 600 and bally <= 800 and ballx >= x2 and ballx <= x2+100:
        speedx = -1*speedx
        speedx = speedx/random(0.5,1.5)
        speedy = -1*speedy
        speedy = speedy/random(0.5,1.5)
    if bally >= 700 or bally <= 0 or ballx >= 700 or ballx <= 0:
        fill(0, 408, 612)
        textSize (50)
        text("haha loser", 350, 350)        
   # if bally >= 20:
       # bally = bally+speedy
    #if ballx >= 20:
     #   ballx = ballx-speedx
    if ballx+55 >= x1 and ballx-55 <= x1+100 and bally-55<=20:
        speedx = -1*speedx
        speedx = speedx/random(0.5,1.5)
        speedy = -1*speedy
        speedy = speedy/random(0.5,1.5)
        print (speedy)
    
        
   
#movement
def keyPressed():
    background(0)
    global x1, x2
    if key == 'a':
        x1 = x1-70
    elif key == 'd':
        x1 = x1+70
    elif keyCode == LEFT:
        x2 = x2-70
    elif keyCode == RIGHT:
        x2 = x2+70
