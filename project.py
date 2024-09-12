from tkinter import *
import random

root = Tk()

#===========IMAGES===========#
blank_img = PhotoImage(file="images/Blank.png").subsample(50, 50)

player_rock = PhotoImage(file="images/p_rock.png").subsample(3, 3)
player_paper = PhotoImage(file="images/p_paper.png").subsample(3, 3)
player_scissor = PhotoImage(file="images/p_scissor.png").subsample(3, 3)

com_rock = PhotoImage(file="images/c_rock.png").subsample(3, 3)
com_paper = PhotoImage(file="images/c_paper.png").subsample(3, 3)
com_scissor = PhotoImage(file="images/c_scissor.png").subsample(3, 3)

#==========SCORE VARIABLES==============#
player_score = 0
computer_score = 0

#==========METHODS==============#
def Rock():
    global player_choice
    player_choice = 1
    player_img.configure(image=player_rock)
    MatchProcess()

def Paper():
    global player_choice
    player_choice = 2
    player_img.configure(image=player_paper)
    MatchProcess()

def Scissor():
    global player_choice
    player_choice = 3
    player_img.configure(image=player_scissor)
    MatchProcess()

def MatchProcess():
    com_choice = random.randint(1, 3)
    if com_choice == 1:
        comp_img.configure(image=com_rock)
        ComputerRock()
    elif com_choice == 2:
        comp_img.configure(image=com_paper)
        ComputerPaper()
    elif com_choice == 3:
        comp_img.configure(image=com_scissor)
        ComputerScissor()
    UpdateScore()

def ComputerRock():
    global player_score, computer_score
    if player_choice == 1:
        lbl_status.config(text="Game Tie")
    elif player_choice == 2:
        lbl_status.config(text="Player Win")
        player_score += 1
    elif player_choice == 3:
        lbl_status.config(text="Computer Win")
        computer_score += 1

def ComputerPaper():
    global player_score, computer_score
    if player_choice == 1:
        lbl_status.config(text="Computer Win")
        computer_score += 1
    elif player_choice == 2:
        lbl_status.config(text="Game Tie")
    elif player_choice == 3:
        lbl_status.config(text="Player Win")
        player_score += 1

def ComputerScissor():
    global player_score, computer_score
    if player_choice == 1:
        lbl_status.config(text="Player Win")
        player_score += 1
    elif player_choice == 2:
        lbl_status.config(text="Computer Win")
        computer_score += 1
    elif player_choice == 3:
        lbl_status.config(text="Game Tie")

def UpdateScore():
    lbl_player_score.config(text=f"Player Score: {player_score}")
    lbl_computer_score.config(text=f"Computer Score: {computer_score}")

def ExitApp():
    root.destroy()
    exit()

#==========LABEL WIDGET ==============#
player_img = Label(root, image=blank_img)
comp_img = Label(root, image=blank_img)

lbl_player = Label(root, text="PLAYER")
lbl_player.grid(row=1, column=1)
lbl_player.config(bg="#99ff99")

lbl_computer = Label(root, text="COMPUTER")
lbl_computer.grid(row=1, column=3)
lbl_computer.config(bg="#99ff99")

lbl_status = Label(root, text="", font=('arial', 12))
lbl_status.config(bg="#99ff99")

lbl_player_score = Label(root, text="Player Score: 0", font=('arial', 12))
lbl_player_score.config(bg="#99ff99")

lbl_computer_score = Label(root, text="Computer Score: 0", font=('arial', 12))
lbl_computer_score.config(bg="#99ff99")

player_img.grid(row=2, column=1, padx=30, pady=20)
comp_img.grid(row=2, column=3, pady=20)
lbl_status.grid(row=3, column=2)
lbl_player_score.grid(row=4, column=1)
lbl_computer_score.grid(row=4, column=3)

#============BUTTON WIDGET ============#
rock = Button(root, image=player_rock, command=Rock)
paper = Button(root, image=player_paper, command=Paper)
scissor = Button(root, image=player_scissor, command=Scissor)
btn_quit = Button(root, text="Quit", command=ExitApp)

rock.grid(row=5, column=1, pady=30)
paper.grid(row=5, column=2, pady=30)
scissor.grid(row=5, column=3, pady=30)
btn_quit.grid(row=6, column=2)

#==========INITIALIZATION===========#
if __name__ == "__main__":
    root.mainloop()

#==========END OF CODE===========#