import random

def setup():
    global img
    global guess
    global gameActive
    global startGame
    global scoreboard
    global letters6
    global letters7
    global letters8
    # global highscore

    setOfwords = ()
    letters6= [
    "dazzle",
    "jacket",
    "crowns",
    "oceans",
    "arrive",
    "credit",
    "junior",
    "artist",
    "coffee",
    "engine",
    "apples",
    "family",
    "memory",
    "summer",
    "target",]
    
    letters7=[
    "compete",
    "driving",
    "reading",
    "teacher",
    "working",
    "virtual",
    "sixteen",
    "quality",
    "publish",
    "pacific",
    "natural",
    "machine",
    "achieve"]
    
    letters8=[
    "absolute",
    "birthday",
    "children",
    "ultimate",
    "engineer",
    "festival",
    "graduate",
    "hospital",
    "keyboard",
    "learning",
    "workshop",
    "wireless",
    "triangle"]
    
    # highscore = {
    # "KP",160,
    # "Liv",220,
    # "Sky",280,
    # "Erica",200
    # }

    size(1000,800)

    guess=[]
    gameActive = False
    startGame = True
    scoreboard = 0
    # highscore = 0

    instructions()

def draw():
    global gameActive
    global gameclock
    global scoreboard
    # global highscore

    currentTime = millis()
    if gameActive:
        gameclock = (currentTime - startTimer)/1000
        fill(244,246,251)
        noStroke()
        rect(935,0,60,40)
        f = createFont("ShadowsIntoLight-Regular.ttf",40)
        textFont(f)
        fill(0,0,0)
        text(gameclock,935,40)
        
        if gameclock == 40 and scoreboard < 220: #if you dont make the level requirements
            gameActive = False
            bigFF = createFont("ShadowsIntoLight-Regular.ttf",130)
            textFont(bigFF)
            background(255,255,255)
            text("GAME OVER..",150,400)
            f = createFont("ShadowsIntoLight-Regular.ttf",30)
            textFont(f)
            text("press r to restart",400,450)
            
        if gameclock == 40 and scoreboard >= 100: #to go to level 2
            gameActive = False
            bigFF = createFont("ShadowsIntoLight-Regular.ttf",130)
            textFont(bigFF)
            background(255,255,255)
            text("NEXT LEVEl..",150,400)
            f = createFont("ShadowsIntoLight-Regular.ttf",30)
            textFont(f)
            text("press g",400,450)
        if key == 'g':
            fill(244,246,251)
            noStroke()
            rect(240,0,500,60)
            f = createFont("ShadowsIntoLight-Regular.ttf",40)
            textFont(f)
            fill(0,0,0)
            text("LEVEL 2 - 160 pts - 40 seconds",250,40)
        
        if gameclock == 40 and scoreboard >= 160: #to go to level 3
            gameActive = False
            bigFF = createFont("ShadowsIntoLight-Regular.ttf",130)
            textFont(bigFF)
            background(255,255,255)
            text("NEXT LEVEl..",150,400)
            f = createFont("ShadowsIntoLight-Regular.ttf",30)
            textFont(f)
            text("press h",400,450)
        if key == 'h':
            fill(244,246,251)
            noStroke()
            rect(240,0,500,60)
            f = createFont("ShadowsIntoLight-Regular.ttf",40)
            textFont(f)
            fill(0,0,0)
            text("LEVEL 3 - 220 pts - 40 seconds",250,40)
            
        if gameclock == 40 and scoreboard >= 220: #winner screen
            gameActive = False
            bigFFF = createFont("ShadowsIntoLight-Regular.ttf",120)
            textFont(bigFFF)
            background(255,255,255)
            fill(0,0,0)
            rect(200,150,600,600)
            fill(255,255,255)
            text("SCOREBOARD",215,300)
            # text(highscore,215,350)
                        
        stroke(0,0,0)

def keyPressed():
    global setOfwords
    global randomWord
    global startTimer
    global gameActive
    global guess
    global startGame
    global scoreboard
    global gameclock
    global letters6
    global letters7
    global letters8

    import random
    
    if key == 's' and startGame == True: #starts game
        gameActive = True
        startTimer = millis()
        setOfwords = letters6
        randomWord = random.choice(setOfwords)
        # randomWord = "dazzle"
        overEasy(randomWord)
        startGame = False

    if key == 'g' and gameclock >= 40:
        gameActive = True
        startTimer = millis()
        setOfwords = letters7
        randomWord = random.choice(setOfwords)
        overEasy(randomWord)
        startGame = True
        guess = []
        # fill(244,246,251)
        # noStroke()
        # rect(240,0,500,60)
        # f = createFont("ShadowsIntoLight-Regular.ttf",40)
        # textFont(f)
        # fill(0,0,0)
        # text("LEVEL 2 - 160 pts - 40 seconds",250,40)
        
    if key == 'h' and gameclock >= 30:
        gameActive = True
        startTimer = millis()
        setOfwords = letters8
        randomWord = random.choice(setOfwords)
        overEasy(randomWord)
        startGame = True
        guess = []
        # fill(244,246,251)
        # noStroke()
        # rect(240,0,500,60)
        # f = createFont("ShadowsIntoLight-Regular.ttf",40)
        # textFont(f)
        # fill(0,0,0)
        # text("LEVEL 3 - 220 pts - 40 seconds",250,40)
    
    if key == 'r':
        gameActive = True
        startTimer = millis()
        setOfwords = letters6
        randomWord = random.choice(setOfwords)
        scoreboard = 0
        overEasy(randomWord)
        startGame = True
        guess = []

    if keyCode == 10: #RETURN key #makes it go to next word

        together = "".join(guess) #makes list of letters become string
        if together in setOfwords: # to see if it was in a list
            scoreboard = scoreboard + 20
            
        setOfwords.remove(randomWord)
        guess = []
        randomWord = random.choice(setOfwords)
        overEasy(randomWord)
        
        
        # fill(244,246,251)
        # noStroke()
        # rect(240,0,500,60)
        # f = createFont("ShadowsIntoLight-Regular.ttf",40)
        # textFont(f)
        # fill(0,0,0)
        # text("LEVEL 2 - 160 pts - 40 seconds",250,40)
        
    if keyCode == 8 and len(guess) != 0: #deletes
        guess.pop()
        overEasy(randomWord)
        guessLetters()
        

def mousePressed():
    global result
    global randomWord
    global l
    global x
    global guess

    if gameActive == False or len(guess) == len(randomWord):
        return
    
    for e in range(len(randomWord)):
        if mousePressed and mouseY > 680 and mouseX > (e*120)+40 and mouseX < (e*120)+150:
            guess.append(result[e])
            
    guessLetters()

def guessLetters():

    f = createFont("ShadowsIntoLight-Regular.ttf",40)
    textFont(f)
    fill(0,0,0)

    for x in range(len(guess)): #makes the letters appear on the line
        firstLetter = guess[x]
        text(firstLetter,(x*120)+80,640)

def instructions():
    fill(255,255,255)
    rect(200,150,600,600)
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
Good luck!!""",210,200)

    bigF = createFont("ShadowsIntoLight-Regular.ttf",70)
    textFont(bigF)
    text("INSTRUCTIONS..",270,100)
               
def overEasy(word):
    global result
    global l
    global x
    global scoreboard

    numLetters = len(word)
    
    img = loadImage("FullSizeRender.jpeg") #logo
    background(244,246,251)
    image(img,0,-100,1000,800)

    f = createFont("ShadowsIntoLight-Regular.ttf",40)
    textFont(f)
    fill(0,0,0)
    text("Score:"+str(scoreboard),20,40)
    text("Time:",850,40)
    text("LEVEL 1 - 100 pts - 40 seconds",250,40)

    fill(255,255,255)    #draws boxes and spaces
    for j in range(numLetters):
        rect((j*120)+40,680,100,100)

    for r in range(numLetters):
        line((r*120)+40,660,(r*120)+140,660)

    f = createFont("ShadowsIntoLight-Regular.ttf",40)
    textFont(f)
    fill(0,0,0)

    l = list(word) #shuffles letters
    random.shuffle(l)
    result = "".join(l)

    for x in range(len(result)): #makes the letters appear in the boxes
        firstLetter = result[x]
        text(firstLetter,(x*120)+80,740)

    fill(255,255,255)
    rect(700,70,250,180)
    lilf = createFont("ShadowsIntoLight-Regular.ttf",20)
    textFont(lilf)
    fill(0,0,0)
    text("""
- ENTER to go to next word
- press DELETE if you clicked
the wrong letter""",710,80)
