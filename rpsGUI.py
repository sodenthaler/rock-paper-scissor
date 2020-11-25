import random
from tkinter import *

schema = {
    "gur": {"gur": 1, "leter": 0, "gershere": 2},
    "leter": {"gur": 2, "leter": 1, "gershere": 0},
    "gershere": {"gur": 0, "leter": 2, "gershere": 1},
}


comp_score = 0
player_score = 0


def outcome_handler(user_choice):
    global player_score, comp_score
    outcomes = ["gur", "leter", "gershere"]
    random_number = random.randint(0, 2)
    print(outcomes[random_number])
    comp_choice = outcomes[random_number]

    result = schema[user_choice][comp_choice]

    player_choice_label.config(
        fg="red", text="Zgjedhja e lojtarit: " + str(user_choice)
    )
    computer_choice_label.config(
        fg="green", text="Zgjedhja e kompjuterit: " + str(comp_choice)
    )
    if result == 2:
        player_score = player_score + 2
        player_score_label.config(text="Lojtari: " + str(player_score))
        outcome_label.config(fg="blue", text="Ju fituat!")
    if result == 1:
        player_score = player_score + 1
        comp_score = comp_score + 1
        player_score_label.config(text="Lojtari: " + str(player_score))
        computer_score_label.config(text="Kompjuteri: " + str(comp_score))
        outcome_label.config(fg="blue", text="Kjo perballje mbaroi ne barazim!")

    if result == 0:
        comp_score = comp_score + 2
        computer_score_label.config(text="Kompjuteri: " + str(player_score))
        outcome_label.config(fg="blue", text="Kompjuteri fitoi!  :(")


master = Tk()
master.title("Gur, Leter, Gershere")


# Labels
Label(master, text="Gur, Leter, Gershere", font=("Calibri", 14)).grid(
    row=0, sticky=N, pady=10, padx=200
)
Label(master, text="Gur, Leter, Gershere", font=("Calibri", 14)).grid(
    row=0, sticky=N, pady=10, padx=200
)
Label(master, text="Ju lutem zgjidhni nje opsion").grid(row=1, sticky=N)
player_score_label = Label(master, text="Lojtari: 0")
player_score_label.grid(row=2, sticky=W)

computer_score_label = Label(master, text="Kompjuteri: 0")
computer_score_label.grid(row=2, sticky=E)

player_choice_label = Label(master)
player_choice_label.grid(row=3, sticky=W)

computer_choice_label = Label(master)
computer_choice_label.grid(row=3, sticky=E)

outcome_label = Label(master)
outcome_label.grid(row=3, sticky=N)
# Buttons
Button(master, text="Gur", width=15, command=lambda: outcome_handler("gur")).grid(
    row=4, sticky=W, padx=5, pady=5
)
Button(master, text="Leter", width=15, command=lambda: outcome_handler("leter")).grid(
    row=4, sticky=N, pady=5
)
Button(
    master, text="Gershere", width=15, command=lambda: outcome_handler("gershere")
).grid(row=4, sticky=E, padx=5, pady=5)

master.mainloop()
