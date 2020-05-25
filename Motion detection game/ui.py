from tkinter import *
import cv2
from tkinter import messagebox 
import PIL.Image, PIL.ImageTk
window = Tk()
window.title("Welcome")
window.geometry('1500x1500')
########CODING FOR QUIT BUTTON MESSAGEBOX#########
def close_window(): 
    MsgBox=messagebox.askquestion('Quit the game','Are you sure you want to quit the game?',icon='warning')
    if MsgBox =='yes':
        window.destroy()
    else:
        messagebox.showinfo('Return','You will now return to the game screen')
def close():
    if txt1 == '':
        messagebox.showinfo('Return','You will now return to the game screen')
    else:
        file=open("text1.txt","w")
        a=txt1.get()
        file.write(a)
        file.close()
    if txt2 == '':
        messagebox.showinfo('Return','You will now return to the game screen')
    else:
        file=open("text2.txt","w")
        b=txt2.get()
        file.write(b)
        file.close()
    window.destroy()
#################CREATE A WINDOW##################
cv_img=cv2.imread("images.jpeg")
canvas=Canvas(window,width=1500,height=1500)
canvas.pack()
photo=PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(cv_img))
canvas.create_image(0,0,image=photo,anchor=NW)
##########LABEL AND TEXTBOX FOR PLAYER 1##########
photo2=PhotoImage(file="player1.gif")
lbl1 = Label(window, compound=TOP, width=284, height=58, image=photo2)
lbl1.place(x=200,y=180)
txt1 = Entry(window,font=("Bold",20),bd=5,bg='light green')
txt1.place(x=600,y=185)
##########LABEL AND TEXTBOX FOR PLAYER 2##########
photo3=PhotoImage(file="player2.gif")
lbl2 = Label(window, compound=TOP, width=292, height=60, image=photo3)
lbl2.place(x=200,y=280)
txt2 = Entry(window,font=("Bold",20),bd=5,bg='light green')
txt2.place(x=600,y=285)
##############READY AND QUIT BUTTONS##############
btn2=Button(window,text="Ready",font=("Bold",20),height=2,width=20,fg='green',bg='black',bd=10,command=close)
btn2.place(x=400,y=500)
btn3=Button(window,text="Quit",font=("Bold",15),height=1,width=8,fg='black',bg='gray',bd=5,command=close_window)
btn3.place(x=1225,y=50)
###################MAIN LOOP######################
window.mainloop()


