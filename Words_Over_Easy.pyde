
def setup(): 
    global img
    size(800,800)
    

    instructions()
    # overEasy("credit")
    
    
def draw():
    pass
    
def keyPressed():
    if key == 's':
        overEasy("credit")
    print(key)
    
def instructions():
    fill(255,255,255)
    rect(100,100,600,600)
    f = createFont("ShadowsIntoLight-Regular.ttf",30)
    textFont(f)
    fill(0,0,0)
    text("""The name of this game is Words Over Easy. 
The object of the game is to see how many of the 
preset words you can make in 60 seconds. You
have to click the letters on the screen and 
then press ENTER on your keyboard to go to 
the next word. As time progresses, the words 
to guess will get harder.
Good luck!!""",110,140)
    
    bigF = createFont("ShadowsIntoLight-Regular.ttf",70)
    textFont(bigF)
    text("INSTRUCTIONS..",200,75)
    
    # hey cori
    #cori was here

    # dictionary()


# def dictionary():
#     setOfwords = {
#     "book", correct,
#     "cat", correct,
#     "crown", correct,
#     "ocean", correct,
#     "arrive", correct,
#     "credit", correct,
#     "junior", correct,
#     "bear", correct,
#     "dark", correct,
#     "hair", correct,
#     "apple", correct,
#     "build", correct,
#     "giant", correct,
#     "japan", correct,
#     "lucky", correct,
#     }
    
#     inputtedWord = #variable from cori("book").lower()
#     dictionary = setOfwords
#     if inputtedWord in setOfWords:
#         print(inputtedWord, "correct")
#     else:
#         print(inputtedWord, "incorrect")
           
    
def overEasy(word):
    img = loadImage("overeasy.jpg") #logo
    background(235,239,242)
    image(img,0,-100,800,800)
    
    f = createFont("ShadowsIntoLight-Regular.ttf",40)
    textFont(f)
    fill(0,0,0)
    text("Score:",20,40)
    text("Time:",640,40)
    
    fill(255,255,255)
    rect(40,680,100,100) #box 1
    rect(160,680,100,100) #box 2
    rect(280,680,100,100) #box 3
    rect(400,680,100,100) #box 4
    rect(520,680,100,100) #box 5
    rect(640,680,100,100) #box 6
    
    line(40,640,140,640) #line 1
    line(160,640,260,640) #line 2
    line(280,640,380,640) #line 3
    line(400,640,500,640) #line 4
    line(520,640,620,640) #line 5
    line(640,640,740,640) #line 6
    
    f = createFont("ShadowsIntoLight-Regular.ttf",40)
    textFont(f)
    fill(0,0,0)
    
    import random 
    l = list(word) #shuffles letters
    random.shuffle(l)
    result = "".join(l)
    print(word)
    print(l)
    print(result)
    
    for x in range(len(result)): #makes the letters appear in the boxes
        firstLetter = result[x]
        text(firstLetter,(x*120)+80,740)
