def setup():
    global img
    size(800,800)
    img = loadImage("Screen Shot 2019-07-29 at 11.00.25 AM.png")
    background(235,239,242)
    image(img,0,-100,800,800)
    
    f = createFont("ShadowsIntoLight-Regular.ttf",40)
    textFont(f)
    fill(0,0,0)
    text("Score:",20,40)
    text("Time:",640,40)
    
    overEasy("book")
    
def overEasy(word):
    fill(255,255,255)
    rect(40,680,100,100)
    rect(160,680,100,100)
    rect(280,680,100,100)
    rect(400,680,100,100)
    rect(520,680,100,100)
    rect(640,680,100,100)
    
    line(40,640,140,640)
    line(160,640,260,640)
    line(280,640,380,640)
    line(400,640,500,640)
    line(520,640,620,640)
    line(640,640,740,640)
    
    f = createFont("ShadowsIntoLight-Regular.ttf",40)
    textFont(f)
    fill(0,0,0)
    
    import random
    l = list(word)
    random.shuffle(l)
    result = "".join(l)
    print(word)
    print(l)
    print(result)
    
    for x in range(len(result)):
        firstLetter = result[x]
        text(firstLetter,(x*120)+80,740)
        
# def mouseClicked():
    
#     # for j in range(len(word)):
#     #     if mouseX > 40 and mouseX < 140 and mouseY > 680 and mouseY < 780:
#     #         print(firstLetter)
#     #         word = 
import time
def timer():
   now = time.localtime(time.time())
   return now[5]
