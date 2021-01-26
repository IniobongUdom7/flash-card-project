from tkinter import *
import pandas
import random
import time

BACKGROUND_COLOR = "#383838"
current_card = {}
for_learning = {}

#EXTRACTING FROM THE CSV FILE
try:
    data = pandas.read_csv("data/words_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    for_learning = data.to_dict(orient="records")
else:
    for_learning = data.to_dict(orient="records")



def next_card():
    global current_card, flip_timer
    screen.after_cancel(flip_timer)
    current_card = random.choice(for_learning)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_background, image=card_front_img)
    flip_timer = screen.after(3000, func=switch_card)


#SWITCH THE CARD FROM BACK AND FRONT
def switch_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=card_back_img)

def is_known():
    for_learning.remove(current_card)
    print(len(for_learning))
    data = pandas.DataFrame(for_learning)
    data.to_csv("data/words_learn.csv", index=False)
    next_card()



#SCREEN SETUP
screen =Tk()
screen.title("Flash Card")
screen.config(padx=50, pady=50, bg=BACKGROUND_COLOR)


flip_timer = screen.after(3000, func=switch_card)

canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 158, text="", font=("courier", 45, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("courier", 45, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0,column=0, columnspan=2)


cross_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=cross_image, highlightthickness=0, command=next_card)
wrong_button.grid(row=1, column=0)

check_image = PhotoImage(file="images/right.png")
right_button = Button(image=check_image, highlightthickness=0, command=is_known)
right_button.grid(row=1, column=1)

next_card()













screen.mainloop()