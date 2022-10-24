x1 = 30
x2 = 30
ballx = 350
bally = 350
speed = 1.5

def setup():
    size (700,700)
    background(0)
    
def draw():
    global ballx,bally
    global x1,x2
    global speed
    fill (246,120,78)
    rect(x1, 20, 100, 20)
    fill (80,257,69)
    rect(x2, 600, 100, 20)
    fill (100,224,240)
    circle (ballx,bally,55)
    if bally >= 600 and bally <= 800 and ballx >= x2 and ballx <= x2+100:
        ballx = -1*ballx*speed
        bally = -1*bally*speed
    if bally >= 20:
        bally = bally+speed
    if ballx >= 20:
        ballx = ballx-speed
        
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
