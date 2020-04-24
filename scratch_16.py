from tkinter import *
import tkinter as tk

window=tk.Tk()
window.geometry("500x500")
bgImage=PhotoImage(file="C:\Users\acer\.PyCharmCE2019.1\config\scratches\guddu.jpg")
Label(window,image=bgImage).place(relwidth=1,relheight=1).pack()
while running:
    Screen.blit(background,(0,0))

button=Button(window,text="SUBMIT",command="store_member",bg="#E6E914",fg="black").pack()

window.mainloop()

