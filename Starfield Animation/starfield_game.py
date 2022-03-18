from tkinter import *
import random

sw = 1000
sh = 800

NUMBER_OF_STARS = 50

#score.txt file is used to keep track of high scoring when game program is ended
f = open("score.txt", "r+")
high_score = f.read()
if len(high_score) == 0:
    high_score = 0
else:
    high_score = int(high_score)
f.close()



def create_star():
    star = {}
    star["x"] = random.randint(300, sw - 300)
    star["y"] = random.randint(200, sh - 200)
    star["z"] = random.randint(500, 1000)
    star["init_z"] = star["z"]
    star["size"] = random.randint(1, 5)

    star["id"] = canvas.create_oval(star["x"], star["y"], star["x"] + star["size"], star["y"] + star["size"], fill="white", activefill="yellow")
    canvas.tag_bind(star['id'], '<Enter>', got_star) #tag -> cursor
    return star

def move_stars():

    for i in range(NUMBER_OF_STARS):
        star = star_list[i]

        factor = star["init_z"] / star["z"]

        x = (star["x"] - sw / 2 ) * factor + sw / 2
        y = (star["y"] - sh / 2 ) * factor + sh / 2
        size = star["size"] * factor

        canvas.coords(star["id"], x, y, x + size, y + size)
        star["z"] = star["z"] - 4

        if x < 0 or x > sw or y > sh or y < 0 or star["z"] <= 0:
            canvas.delete(star["id"])
            star_list[i] = create_star()

    canvas.after(10, move_stars)


def got_star(event):
    global score, high_score
    
    if not game_over:
        '''
        you get a point if you hover over a star.
        assume at this point you hovered over a star.
        change the correct variables and update the correct text.
        
        '''
        
        score = score + 1
        if score > high_score:
            high_score = score
            
        canvas.itemconfig(score_id, text="Score: " + str(score))
        canvas.itemconfig(highscore_id, text="High score: " + str(high_score))
            


def do_timer():
    
    global timer, game_over

    timer = timer - 1
    canvas.itemconfig(timer_id, text="Time: " + str(timer))

    '''
    check if the game is over
    if the game is over, stop the game, show the game over text, restart text
    '''
    if timer == 0:
        game_over = True
        canvas.itemconfig(game_over_id, state=NORMAL)
        canvas.itemconfig(restart_id, state=NORMAL)
        f = open("score.txt", "w")
        f.write(str(high_score))
        f.close()
        
    else:
        canvas.after(1000, do_timer)
        

def restart_game(event):
    global timer, score, game_over

    if game_over:
        game_over = False
        timer = 25
        score = 0
        canvas.itemconfig(game_over_id, state=HIDDEN)
        canvas.itemconfig(restart_id, state=HIDDEN)
        canvas.itemconfig(score_id, text="Score: " + str(score))
        canvas.itemconfig(highscore_id, text="High Score: " + str(high_score))
        canvas.itemconfig(timer_id, text="Time: " + str(timer))
        canvas.after(1000, do_timer)
    

root = Tk()
root.title("Star Field")
canvas = Canvas(root, width=sw, height=sh, background="black")
canvas.pack()

score_id = canvas.create_text(10, 10, font=("Arial", 20), fill="purple", anchor=NW)
highscore_id = canvas.create_text(140, 10, font=("Arial", 20), fill="purple", anchor=NW)
timer_id = canvas.create_text(sw - 150, 10, font=("Arial", 20), fill="purple", anchor=NW)
game_over_id = canvas.create_text(sw / 2, sh / 2, font=("Arial", 20), fill="purple", anchor=NW, text="Game Over!", state=HIDDEN)
restart_id = canvas.create_text(sw / 2, sh / 2 + 40, font=("Arial", 20), fill="purple", anchor=NW, text="Press Spacebar to Restart", state=HIDDEN)



star_list = []
for i in range(NUMBER_OF_STARS):
    star_list.append(create_star())
    
#game properties
game_over = True
canvas.bind_all("<space>", restart_game)
restart_game(None)
move_stars()

root.mainloop()
