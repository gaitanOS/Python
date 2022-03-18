#starfield.py


from tkinter import *
import random

NUMBER_OF_STARS = 50

sw = 1000
sh = 800

def create_star():
    star = {}
    star["x"] = random.randint(300, sw - 300)
    star["y"] = random.randint(200, sh - 200)
    star["z"] = random.randint(500, 1000)
    star["init_z"] = star["z"]
    star["size"] = random.randint(1, 5)

    star["id"] = canvas.create_oval(star["x"], star["y"], star["x"] + star["size"], star["y"] + star["size"], fill="white", activefill="yellow")

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

root = Tk()
root.title("Star Field")
canvas = Canvas(root, width=sw, height=sh, background="black")
canvas.pack()



star_list = []
for i in range(NUMBER_OF_STARS):
    star_list.append(create_star())


move_stars()

root.mainloop()
