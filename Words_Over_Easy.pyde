def setup(): 
    global img
    global guess
    global showTimer
    global startGame
    global scoreboard
    global boxX
    global Rect
    global boxes
    global spaces
    global space1
    global space2
    
    size(800,800)
    
    guess=[]
    showTimer = False 
    startGame = True
    scoreboard = 0
    
    instructions()
    
def draw():
    global showTimer 
    currentTime = millis()
    if showTimer:
        displayTime = (currentTime - startTimer)/1000
        fill(235,239,242)
        noStroke()
        rect(740, 0,60,40)
        fill(0)
        text(displayTime ,740,40)
        stroke(0,0,0)
    
def keyPressed():
    global setOfwords
    global randomWord
    global startTimer
    global showTimer
    global guess
    global startGame
    global scoreboard
    
    import random
    dictionary()
    randomWord = random.choice(setOfwords)
    if key == 's' and startGame == True:
        showTimer = True 
        startTimer = millis()
        overEasy(randomWord)
        startGame = False
        
    if keyCode == 10: #RETURN key #makes it go to next word
        together = "".join(guess) #makes list of letters become string
        if together in setOfwords: # to see if it was in a list
            scoreboard = scoreboard + 20
        guess = []
        overEasy(randomWord)
        
    if keyCode == 8:
        guess = []
    print(keyCode)
        
    
def mousePressed():
    global result
    global randomWord
    global l
    global x
    global guess
    
    dictionary()
                        
    if mousePressed and mouseY > 680 and mouseX > 40 and mouseX < 150:
        guess.append(result[0])
    elif mousePressed and mouseY > 680 and mouseX > 160 and mouseX < 270:
        guess.append(result[1])
    elif mousePressed and mouseY > 680 and mouseX > 280 and mouseX < 390:
        guess.append(result[2])
    elif mousePressed and mouseY > 680 and mouseX > 400 and mouseX < 510:
        guess.append(result[3])
    elif mousePressed and mouseY > 680 and mouseX > 520 and mouseX < 630:
        guess.append(result[4])
    elif mousePressed and mouseY > 680 and mouseX > 640 and mouseX < 730:
        guess.append(result[5])
        
    for x in range(len(guess)): #makes the letters appear on the line
        firstLetter = guess[x]
        text(firstLetter,(x*120)+100,640) 
        
def instructions():
    fill(255,255,255)
    rect(100,150,600,600)
    f = createFont("ShadowsIntoLight-Regular.ttf",30)
    textFont(f)
    fill(0,0,0)
    text("""The name of this game is Words Over Easy. 
The object of the game is to see how many of the 
preset words you can make in 60 seconds. To start, 
press 's'. You have to click the letters on the 
screen and then press ENTER on your keyboard to 
go to the next word. As time progresses, the words 
to guess will get harder.
Good luck!!""",110,200)
    
    bigF = createFont("ShadowsIntoLight-Regular.ttf",70)
    textFont(bigF)
    text("INSTRUCTIONS..",200,100)
    
def dictionary():
    global setOfwords
    setOfwords = [
    "book",
    "cat",
    "crown",
    "ocean",
    "arrive",
    "credit",
    "junior",
    "bear",
    "dark",
    "hair",
    "apple",
    "build",
    "giant",
    "japan",
    "lucky",
    ]
    
def overEasy(word):
    global result
    global l
    global x
    global scoreboard
    global boxX
    global Rect
    global spaces
    global space1
    global space2

    img = loadImage("overeasy.jpg") #logo
    background(235,239,242)
    image(img,0,-100,800,800)
    
    f = createFont("ShadowsIntoLight-Regular.ttf",40)
    textFont(f)
    fill(0,0,0)
    text("Score:"+str(scoreboard),20,40)
    text("Time:",640,40)
    
    fill(255,255,255)
    for j in range(6):
        rect((j*120)+40,680,100,100)
        
    for r in range(6):
        line((r*120)+40,660,(r*120)+140,660)

    f = createFont("ShadowsIntoLight-Regular.ttf",40)
    textFont(f)
    fill(0,0,0)

    import random 
    l = list(word) #shuffles letters
    random.shuffle(l)
    result = "".join(l)
    
    for x in range(len(result)): #makes the letters appear in the boxes
        firstLetter = result[x]
        text(firstLetter,(x*120)+80,740)
