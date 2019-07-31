#notes for kevin:
    # when you press g to go to next level, the score does not reset and the time doesnt start again
    # when i draw my box in the corner, the numbers for the time get smaller
    # i could still click on the bottom of the screen and letters appear
    

def setup():
    global img
    global guess
    global gameActive
    global startGame
    global scoreboard

    size(800,800)

    guess=[]
    gameActive = False
    startGame = True
    scoreboard = 0

    instructions()

def draw():
    global gameActive
    currentTime = millis()
    if gameActive:
        gameclock = (currentTime - startTimer)/1000
        fill(235,239,242)
        noStroke()
        rect(740, 0,60,40)
        fill(0)
        text(gameclock ,740,40)
        
        if gameclock == 60:
            gameActive = False
            bigFF = createFont("ShadowsIntoLight-Regular.ttf",130)
            textFont(bigFF)
            background(255,255,255)
            text("NEXT LEVEl..",90,400)
            f = createFont("ShadowsIntoLight-Regular.ttf",30)
            textFont(f)
            text("press g",350,450)
              
        stroke(0,0,0)

def keyPressed():
    global setOfwords
    global randomWord
    global startTimer
    global gameActive
    global guess
    global startGame
    global scoreboard

    import random
    #print(setOfwords,"before")


    
    if key == 's' and startGame == True: #starts gamer
        gameActive = True
        startTimer = millis()
        dictionary()
        randomWord = random.choice(setOfwords)
        overEasy(randomWord)
        startGame = False
        scoreboard = 0
        
        
        
    if key == 'g': 
        gameActive = True
        startTimer = millis()
        dictionary()
        randomWord = random.choice(setOfwords)
        overEasy(randomWord)
        startGame = False 
        scoreboard = 0
      

    if keyCode == 10: #RETURN key #makes it go to next word
   
        randomWord = random.choice(setOfwords)
        together = "".join(guess) #makes list of letters become string
        if together in setOfwords: # to see if it was in a list
            scoreboard = scoreboard + 20
        setOfwords.remove(randomWord)
        guess = []
        overEasy(randomWord)

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

    #dictionary()

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
        
    guessLetters()

def guessLetters():
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
    
    # if "setOfwords" in globals():
        
    setOfwords = [
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


def overEasy(word):
    global result
    global l
    global x
    global scoreboard

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
        
#     fill(255,255,255)    
#     rect(530,70,250,180)
#     lilf = createFont("ShadowsIntoLight-Regular.ttf",20)
#     textFont(lilf)
#     fill(0,0,0)
#     text("""          Hints:
# - ENTER to go to next word
# - press DELETE if you clicked 
# the wrong letter""",540,90)
    
