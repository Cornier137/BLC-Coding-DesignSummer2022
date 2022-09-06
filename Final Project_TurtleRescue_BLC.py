from tkinter import *
import random

window=Tk()
window.title('Turtle Rescue')

canvas= Canvas(window, width=400, height=400, bg='blue')
canvas.pack()

#Title and printing out informative messages about the impact of ocean waste on turtles
title=canvas.create_text(200,200,text='Turtle Rescue',\
fill='white', font=('Helvetica',30))
directions=canvas.create_text(200,300,text='Collect Turtle 10 Eggs to win,\
but avoid the ocean waste. Seaweed will give you extra life point', fill='white',font=('Helvetica',20))
print('More than eight million tons of plastic end up in our ocean annually.')
print('over half of sea turtles have ingested plastic in their lives.')
print('A single piece of plastic has a twenty percent chance of killing a sea turtle.')
print('In order to save the turtles we can make a difference by reducing plastic usage.')

score=0
score_display=Label(window, text="Score: " + str(score))
score_display.pack()

level=1
level_display=Label(window, text="Level:" + str(level))
level_display.pack()

player_image=PhotoImage(file="turtle.gif")

mychar=canvas.create_image(200,360,image=player_image)

seaweed_image=PhotoImage(file="seaweed.gif")

waste_image=PhotoImage(file="waste.gif")
egg_image=PhotoImage(file="egg.gif")



seaweed_list=[]
waste_list=[]
egg_list=[]
waste_speed=1

#creating seaweed for life points at any location

def generate_seaweeds():
    global level
    xPosition= random.randint(1,400)
    yPosition=random.randint(1,400)
    seaweed=canvas.create_image(xPosition,yPosition,image=seaweed_image)
    seaweed_list.append(seaweed)
    window.after(15000, generate_seaweeds)

#creating waste & having it drop only from the x position
def generate_waste():
    global level
    xPosition= random.randint(1,400)
    waste=canvas.create_image(xPosition,0,image=waste_image)
    waste_list.append(waste)
    window.after(7000, generate_waste)
    
#creating eggs to be rescued & for score points at any location
def generate_eggs():
    global level 
    xPosition= random.randint(1,400)
    yPosition=random.randint(1,400)
    egg=canvas.create_image(xPosition,yPosition,image=egg_image)
    egg_list.append(egg)
    window.after(10000, generate_eggs)

#providing the conditions to update the score
def update_score_level():
    global score, level, waste_speed
    score=score+1
    score_display.config(text="Level :" + str(score))
    if score>3 and score <=9:
        waste_speed= waste_speed+1
        level=2
        level_display.config(text="Level :"+ strt(level))
    elif score>6:
        waste_speed=waste_speed+1
        level=3
        level_display.config(text="Level:"+str(level))
    
            


def end_game_over():
    window.destroy()
def end_title():
    canvas.delete(title)
    canvas.delete(directions)


def collision(item1, item2, distance):
    xdistance =abs(canvas.coords(item1)[0]-canvas.coords(item2)[0])
    ydistance = abs (canvas.coords(item1)[1]-canvas.coords(item2)[1])
    overlap = xdistance < distance and ydistance < distance
    return overlap 

#if turtle runs into waste than it's game over
def check_hits():
    for waste in waste_list:
        if collision(mychar,waste,30):
            game_over=canvas.create_text(30,30,text='/n/n                    Game Over!', fill='red', font=('Helvetica',30))
            print ('1,000 sea turtles die annually due to digesting plastic.')
            print('Please recycle or reduce your plastic usage. :)')
       
                   
            window.after(10000,end_game_over)
            return
#update score when an egg is captured and deleting it        
    for egg in egg_list:
        if collision(mychar,egg,30):
            canvas.delete(egg)
            egg_list.remove(egg)
            update_score_level()

            

    window.after(100, check_hits)

def move_waste():
    for waste in waste_list:
        canvas.move(waste,0,waste_speed)
        if canvas.coords(waste)[1]>400:
            xposition=random.randint(1,400)
    window.after(50,move_waste)
#Updating the score
def update_score_level():
    global score, level
    score=score+1
    score_display.config(text="score :"+ str(score))


#allowing the turtle to move all directions and creating the condition for each key press
move_direction =0

def check_input(event):
    global move_direction
    key=event.keysym
    if key=="Right":
        move_direction="Right"
    elif key=="Left":
        move_direction="Left"
    elif key=="Up":
        move_direction="Up"
    elif key=="Down":
        move_direction="Down"

def end_input(event):
    global move_direction
    
    move_direction="None"
    
def move_character():
    if move_direction == "Right" and canvas.coords(mychar)[0] <400:
        canvas.move(mychar,10,0)
    if move_direction=="Left" and canvas.coords(mychar)[0]>0:
        canvas.move(mychar,-10,0)
    if move_direction=="Up" and canvas.coords(mychar)[1]>0:
        canvas.move(mychar, 0,-10)
    if move_direction=="Down" and canvas.coords(mychar)[1]<400:
        canvas.move(mychar,0,10)
        
    window.after(16,move_character)


    
canvas.bind_all('<KeyPress>',check_input)
canvas.bind_all('<KeyRelease>',end_input)

window.after(1000,end_title)
window.after(1000,generate_seaweeds)
window.after(1000,generate_eggs)
window.after(1000,generate_waste)
window.after(1000,move_waste)
window.after(1000,check_hits)
window.after(1000,move_character)




window.mainloop()
