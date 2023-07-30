from tkinter import *
import random
import img

win = Tk()
#===========IMAGES===========#
blank_img = PhotoImage(file="images/Blank.png")

player_rock = PhotoImage(file="images/p_rock.png")
sm_player_rock = player_rock.subsample(3,3)

player_paper = PhotoImage(file="images/p_paper.png")
sm_player_paper = player_paper.subsample(3,3)

player_scissor = PhotoImage(file="images/p_scissor.png")
sm_player_paper = player_paper.subsample(3,3)

com_rock = PhotoImage(file="images/c_rock.png")
com_paper = PhotoImage(file="images/c_paper.png")
com_scissor = PhotoImage(file="images/c_scissor.png")


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
   com_choice = random.randint(1,3)
   if com_choice == 1:
       com_img.configure(image=com_rock)
       ComputerRock()
   elif com_choice == 2:
        com_img.configure(image=com_paper)
        ComputerPaper()
   elif com_choice == 3:
        comp_img.configure(image=com_scissor)
        ComputerScissor()

def ComputerRock():
    if player_choice == 1:
        lbl_status.config(text="Game Tie")
    elif player_choice == 2:
        lbl_status.config(text="Player Win")
    elif player_choice == 3:
        lbl_status.config(text="Computer Win")

def ComputerPaper():
     if player_choice == 1:
        lbl_status.config(text="Computer Win")
     elif player_choice == 2:
        lbl_status.config(text="Game Tie")
     elif player_choice == 3:
        lbl_status.config(text="Player Win")

def ComputerScissor():
     if player_choice == 1:
        lbl_status.config(text="Player Win")
     elif player_choice == 2:
        lbl_status.config(text="Computer Win")
     elif player_choice == 3:
        lbl_status.config(text="Game Tie")

def ExitApp():
    root.destroy()
    exit()


#==========LABEL WIDGET ==============#
player_img = Label(root,image=blank_img)
comp_img = Label(root,image=blank_img)

lbl_player = Label(root,text="PLAYER")
lbl_player.grid(row=1,column=1)
lbl_player.config(bg="#99ff99")

lbl_computer = Label(root,text="COMPUTER")
lbl_computer.grid(row=1,column=3)
lbl_player.config(bg="#99ff99")

lbl_status = Label(root,text="", font=('arial',8))
lbl_status.config(bg="#99ff99")

player_img.grid(row=2,column=1,padx=30,pady=20)
comp_img.grid(row=2,column=3,pady=20)
lbl_status.grid(row=3,column=2)

#============BUTTON WIDGET ============#
rock=Button(root, image= sm_player_rock, command=rock)
paper=Button(root, image= sm_player_paper, command=paper)
scissor=Button(root, image= sm_player_scissor, command=scissor)
btn_quit=Button(root, text="Quit", command=ExitApp)

rock.grid(row=4, column=1, pady=30)
paper.grid(row=4, column=1, pady=30)
scissor.grid(row=4, column=1, pady=30)
btn_quit.grid(row=5, column=2)

#==========INITIALIZATION===========#
if __name__=="__main__":
   root.mainloop()

        

   
