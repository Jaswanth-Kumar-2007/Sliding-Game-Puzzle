'''
#Sliding Game Python
#Name : Jaswanth Kumar Kamireddi
#ID No. : B25DS015
#Branch : DSAI
'''

'''
Requirements
# pip install Pythonturtle random2 os-sys pypi-json
'''

import turtle

import random

import os

import json

'''
Screen Starts here . Building Basic of the Screen
'''
#Screen Output Start
s = turtle.Turtle()
s.screen.bgcolor("LightSkyBlue")
s.screen.title("15 Sliding Game")
s.pencolor("Black")
s.fillcolor("Yellow")
s.hideturtle()
s.penup()
s.width(4)
s.goto(-50,-50)
s.pendown()
s.begin_fill()
for i in range(6):
    s.forward(100)
    s.left(60)
s.width(0)
s.end_fill()
s.penup()
s.goto(-80, 0)
s.write("Welcome", font=("Arial", 36, "bold"))

'''
Turtle Delays some Time from Start Screen to Name Input
'''
#Wait Until Some Time
turtle.delay(3000)
turtle.clearscreen()

'''
Defining New Turtle for Screen and Square
'''
#Define Turtle and Start Square
j = turtle.Turtle()
j.screen.bgcolor("Black")
j.pencolor("#00ff00")

'''
Take the Name Input for the person to store the date in name and to display about person in leaderboard 
'''
#Enter Name
name = []
name = turtle.textinput("Welcome to Sliding Game:", "Enter your Name")

'''
Function : save_name
Makes the Names to store in name_data.json file to check that name in checkpoint to load
'''
#Saves All the Name of Players
def save_name():
    global names
    names.append(name)
    n = {"name" : names}
    with open("name_data.json","w") as t:
        json.dump(n,t)
 
'''
Function : load_name
Makes the Names to load out from file
'''
#Loads the Player Names
def load_name():
    global names
    names = [] 
    with open("name_data.json","r") as t:
        n = json.load(t)
    names =  n["name"]

'''
Checks the name_data.json is there , if not there create that file
'''
# Check the First Time or Not (File Created or Not)
file = "name_data.json"
if os.path.exists(file):
    load_name()
    save_name()
    namep = list(set(names))
else:
    names = []
    save_name()
    namep = list(set(names))

'''
Input of Difficulty and Difficulty Patterns Predefined (Got from Real Game Environment) , 
they are working checked already
'''
#Selection of Easy , Medium , Hard Sets from these 4 Sets
difficulty = turtle.textinput("Welcome to Sliding Game:","Enter Difficulty E/M/H")
# EASY
easy1 = ['A','B','C','D','E','G','O','H','I','J','F','K','M','N','L','Z']
easy2 = ['A','B','C','D','E','F','G','H','M','J','K','L','N','I','O','Z']
easy3 = ['A','B','C','D','E','F','G','H','M','J','K','L','N','I','O','Z']
easy4 = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','Z']

# MEDIUM
medium1 = ['A','B','H','C','E','F','D','L','J','N','M','K','I','O','G','Z']
medium2 = ['A','B','C','D','E','I','F','L','J','N','M','K','G','H','O','Z']
medium3 = ['A','B','C','D','E','F','L','H','J','N','M','K','I','G','O','Z']
medium4 = ['A','B','G','N','I','E','C','H','M','K','O','F','J','L','D','Z']

# HARD
hard1   = ['F','E','B','D','A','C','L','G','N','M','H','K','J','I','O','Z']
hard2   = ['E','D','C','H','A','K','G','L','F','N','B','I','M','J','O','Z']
hard3   = ['B','A','D','E','K','C','L','M','J','F','O','N','I','H','G','Z']
hard4   = ['C','E','B','D','A','G','L','H','N','M','F','K','J','O','I','Z']
'''
Selects the Difficulty Arrangement Randomly
'''
#Finds Easy , Medium , Hard from the 4 sets
easy = random.choice([easy1,easy2,easy3,easy4])
medium = random.choice([medium1,medium2,medium3,medium4])
hard = random.choice([hard1,hard2,hard3,hard4])

'''
turtle conditions defined
'''
#Initiation of Turtle
turtle.delay(0)
j.width(4)
j.speed(0)
j.penup()
j.goto(-200,-200)
j.pendown()

'''
Function : draw_grid
#Draws the Sqaure defined only for 4x4
'''
#Square Outline Draw
def draw_grid():
    for i in range(4):
       j.forward(400)
       j.left(90)

    
    for i in range(4):
       j.setheading(0)
       j.forward(100)
       if(i%2 == 0):
           j.left(90)
       else:
           j.right(90)
       j.forward(400)
    
       
    j.setheading(90)
    

    for i in range(4):
       j.forward(100)
       if(i%2 == 0):
           j.left(90)
       else:
           j.right(90)
       j.forward(400)
       j.setheading(90)
       
#Draws the Square
draw_grid()
j.width(None)

'''
Assigning Numbers to Only this Respective Positions
'''
#Assigning Points
points = [(-150,150),(-50,150),(50,150),(150,150),(-150,50),(-50,50),(50,50),(150,50),(-150,-50),(-50,-50),(50,-50),(150,-50),(-150,-150),(-50,-150),(50,-150),(150,-150)]


'''
Defines the CheckPoint Variables,timecounter,movecounter
'''
board = {}
empty_pos = "Z"
timecounter = 0
movecounter = 0  
global movevalues
movevalues = []


'''
Function : Leaderboard
Prints the LeaderBoard By Keeping the Played members in Respective Difficulty and Time Order
'''
#Leaderboard Function
def leaderboard():
    global p,difficulty,timecounter,movecounter
    p = 1
    turtle.clearscreen()
    y = turtle.Turtle()
    y.hideturtle()
    y.screen.bgcolor("White")
    y.pencolor("Black")
    y.penup()
    y.goto(-150, 180)
    y.write("LEADERBOARD ", font=("Arial", 36, "bold"))

    leaderboarddata = []
    
    for i in namep:
         file = f"{i}.json"
         if os.path.exists(file):
              with open(file, "r") as t:
                  d = json.load(t)
              board_data = {eval(pos): val for pos, val in d["board"].items()}
              timecounter = d.get("timecounter1", 0)
              difficulty = d.get("q", "Easy")
              leaderboarddata.append({
                "name": i,
                "time": timecounter,
                "difficulty": difficulty
              })
    
    difficulty_order = {"Easy": 1, "Medium": 2, "Hard": 3}
    leaderboarddata.sort(key=lambda x: (difficulty_order.get(x["difficulty"], 0), x["time"]))
    # Display leaderboard
    h = 140
    SNo = 1
    for entry in leaderboarddata[:3]:
        y.goto(-250, h)
        # Format time as MM:SS
        min = entry['time'] // 60
        sec = entry['time'] % 60
        formatted_time = f"{min:02}:{sec:02}"

        y.write(f"{SNo}., Name: {entry['name']}, Time: {formatted_time}, Mode: {entry['difficulty']}",
                font=("Arial", 20, "bold"))
        h -= 40
        SNo += 1

'''
Function : checkpoint_load
#It Opens the Checkpoint of the player details of timecounter , movecounter , movevalues
'''
def checkpoint_load():
    global board,timecounter,movecounter,q
    file = f"{name}.json"
    if os.path.exists(file):
        with open(file, "r") as t:
            d = json.load(t)
        board = {eval(pos): val for pos, val in d["board"].items()}
        timecounter = d.get("timecounter1",0)
        movecounter = d.get("movecounter1",0)
        movevalues = d.get("movevalues",0)
        q = d.get("difficulty",0)
    else:
        pass   
               
#Selection of Diificulty and Assigning of Difficulty
global q

if os.path.exists(f"{name}.json"):
    global q
    choice = turtle.textinput("Checkpoint Found", "Do you want to continue? (Y/N)")
    if  choice in  ('Y','y'):
        checkpoint_load()
    else:
        if difficulty in ('E', 'e'):
            q = "Easy"
            alphabets = easy
        elif difficulty in ('M', 'm'):
            q = "Medium"
            alphabets = medium
        elif difficulty in ('H', 'h'):
            q = "Hard"
            alphabets = hard
        else:
            turtle.bye()
        board = dict(zip(points, alphabets))
else:
    if difficulty in ('E', 'e'):
        q = "Easy"
        alphabets = easy
    elif difficulty in ('M', 'm'):
        q = "Medium"
        alphabets = medium
    elif difficulty in ('H', 'h'):
        q = "Hard"
        alphabets = hard
    else:
        turtle.bye()
    board = dict(zip(points, alphabets))

'''
Starts Assigns the Alphabets For Every Position there will
Be Defined New Turtle
'''
#Assign Alphabets(or Numbers) to a Position
writers = {}
for (x,y),num in board.items():
    k = turtle.Turtle()
    k.pencolor("#00ff00")
    k.hideturtle()
    k.speed(0)
    k.penup()
    k.goto(x,y)
    k.pendown()
    #num != 16
    if num != "Z" :
        k.write(num,font =("Arial",18,"bold"))
    else:
        empty_pos = (x,y)
    writers[(x,y)] = k

'''
Function: checkpoint_save
It defines that Save the All Position By Name
'''
def checkpoint_save():
    global q
    d = {
        "board": {str(pos): val for pos, val in board.items()},
        "timecounter1": timecounter,
        "movecounter1": movecounter,
        "difficulty": q,
        "movevalues":movevalues
    }
    with open(f"{name}.json", "w") as t:
        json.dump(d, t)


'''
Displays the Time , Difficult and Counter
'''
#Time , Difficulty and Move Counter Intiation
global p
p = 0

    
count = turtle.Turtle()
count.pencolor("#00ff00")
count.hideturtle()
count.penup()
count.goto(-200,250)
count.pendown()

time = turtle.Turtle()
time.pencolor("#00ff00")
time.hideturtle()
time.penup()
time.goto(200,250)
time.pendown()

difficult = turtle.Turtle()
difficult.pencolor("#00ff00")
difficult.hideturtle()
difficult.penup()
difficult.goto(-50,250)
difficult.pendown()

'''
Function : update_move
Updates all the Count
'''
def update_move():
    global movecounter
    count.clear()
    count.write(f"Moves:{movecounter}",font =("Arial",14,"bold"))

'''
Function : difficulty_show
Displays the Diificulty on Screen
'''
def difficulty_show():
    global q
    difficult.write(f"Mode:{q}",font =("Arial",14,"bold"))

def update_time():
    global timecounter, p
    if p == 0:
        timecounter += 1
    time.clear()
    minutes = timecounter // 60
    seconds = timecounter % 60
    time.write(f"Time: {minutes:02}:{seconds:02}", align="center", font=("Arial",14,"bold"))
    update_move()
    difficulty_show()
    turtle.ontimer(update_time, 1000)

def closewindow():
    turtle.bye()
    
'''
Function : checkwin()
#Checks that the Board is Satisfied Win
'''
# Win Checking Condition
def checkwin():
    global p,storage,movevalues
    ordered = [(-150,150),(-50,150),(50,150),(150,150),(-150,50),(-50,50),(50,50),(150,50),(-150,-50),(-50,-50),(50,-50),(150,-50),(-150,-150),(-50,-150),(50,-150),(150,-150)]
    nums = [board[pos] for pos in ordered]
    if nums == ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','Z']:
        turtle.clearscreen()
        w = turtle.Turtle()
        w.hideturtle()
        p = 1
        w.write(" YOU WIN! ", align="center", font=("Arial", 36, "bold"))
        w.penup()
        w.goto(-250,-200)
        w.write(f"Congratulations , {name}\n You Won the Game ",font=("Arial", 36, "bold"))
        turtle.clearscreen()
        leaderboard()
        print(movevalues)
        turtle.listen()
        turtle.onkey(closewindow,"c")
        turtle.onkey(closewindow,"C")
        
        
#Time Intiation
update_time()
save_name()

'''
Function : writers
#Works like Swap Function Clears the Screen and Rewrite Numbers
'''
def writes(pos):
    writers[pos].clear()
    val = board[pos]
    # val != 16
    if val != "Z":
        writers[pos].write(val, font=("Arial",18,"bold"))

'''
Function : up(),down(),left(),right()
#Works per the Movement of the Tiles By Swapping Numbers
'''
#Up Function
def up():
    global empty_pos,movecounter,storage,movevalues
    x,y = empty_pos
    if (x,y-100) in board:
        board[(x,y)], board[(x,y-100)] = board[(x,y-100)], board[(x,y)]
        writes((x,y))
        writes((x,y-100))
        empty_pos = (x,y-100)
        movecounter += 1
        update_move()
        checkwin()
        checkpoint_save()
        movevalues.append("Up")

# Down Function
def down():
    global empty_pos,movecounter,storage,movevalues
    x,y = empty_pos
    if (x,y+100) in board:
        board[(x,y)], board[(x,y+100)] = board[(x,y+100)], board[(x,y)]
        writes((x,y))
        writes((x,y+100))
        empty_pos = (x,y+100)
        movecounter += 1
        movevalues.append("Down")
        update_move()
        checkwin()
        checkpoint_save()


#Left Function
def left():
    global empty_pos,movecounter,storage,movevalues
    x,y = empty_pos
    if (x+100,y) in board:
        board[(x,y)], board[(x+100,y)] = board[(x+100,y)], board[(x,y)]
        writes((x,y))
        writes((x+100,y))
        empty_pos = (x+100,y)
        movecounter += 1
        movevalues.append("Left")
        update_move()
        checkwin()
        checkpoint_save()

# Right Function
def right():
    global empty_pos,movecounter,storage,movevalues
    x,y = empty_pos
    if (x-100,y) in board:
        board[(x,y)], board[(x-100,y)] = board[(x-100,y)], board[(x,y)]
        writes((x,y))
        writes((x-100,y))
        empty_pos = (x-100,y)
        movecounter += 1
        movevalues.append("Right")
        update_move()
        checkwin()
        checkpoint_save()
        


'''
This Below Code Make the Record Input and Runs until win
'''
turtle.listen()
turtle.onkey(up ,"Up")
turtle.onkey(down ,"Down")
turtle.onkey(left ,"Left")
turtle.onkey(right,"Right")
turtle.onkey(leaderboard,"l")
turtle.onkey(leaderboard,"L")


turtle.mainloop()

