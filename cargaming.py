import tkinter as tk
import random

# Game window setup
window = tk.Tk()
window.title("Car Racing Game")
window.geometry("400x600")
window.resizable(False, False)

# Canvas for drawing
canvas = tk.Canvas(window, width=400, height=600, bg="gray")
canvas.pack()

# Road lines
for i in range(0, 600, 40):
    canvas.create_rectangle(190, i, 210, i + 20, fill="white", tags="line")

# Player car
player = canvas.create_rectangle(160, 500, 240, 570, fill="blue")

# Enemy car
enemy = canvas.create_rectangle(160, -100, 240, -30, fill="red")

# Movement values
player_speed = 20
enemy_speed = 10

# Controls
def move_left(event):
    x1, y1, x2, y2 = canvas.coords(player)
    if x1 > 20:
        canvas.move(player, -player_speed, 0)

def move_right(event):
    x1, y1, x2, y2 = canvas.coords(player)
    if x2 < 380:
        canvas.move(player, player_speed, 0)

window.bind("<Left>", move_left)
window.bind("<Right>", move_right)

# Reset enemy car
def reset_enemy():
    x_pos = random.randint(50, 300)
    canvas.coords(enemy, x_pos, -100, x_pos + 80, -30)

# Check collision
def check_collision():
    px1, py1, px2, py2 = canvas.coords(player)
    ex1, ey1, ex2, ey2 = canvas.coords(enemy)
    if px1 < ex2 and px2 > ex1 and py1 < ey2 and py2 > ey1:
        return True
    return False

# Game loop
def game_loop():
    canvas.move(enemy, 0, enemy_speed)
    ex1, ey1, ex2, ey2 = canvas.coords(enemy)

    if ey2 > 600:
        reset_enemy()

    # Road line animation
    for line in canvas.find_withtag("line"):
        canvas.move(line, 0, enemy_speed)
        if canvas.coords(line)[1] > 600:
            canvas.coords(line, 190, -20, 210, 0)

    if check_collision():
        canvas.create_text(200, 300, text="Game Over!", font=("Arial", 30), fill="white")
        return  # stop loop

    window.after(50, game_loop)

reset_enemy()
game_loop()
window.mainloop()
