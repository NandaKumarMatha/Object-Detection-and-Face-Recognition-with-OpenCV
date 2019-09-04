import subprocess
from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfilename
from subprocess import Popen
import os,sys

window = Tk()

window.title("Detection")
window.configure(bg='skyblue')
            
lbl = Label(window, text="Object",bg='pink',font=("Arial Bold", 20))
lbl.grid(column=5, row=0)

lbl = Label(window, text="Face",bg='pink', font=("Arial Bold", 20))
lbl.grid(column=9, row=0)

def wbc():
    Popen('python object_detection_yolo2.py')

#This is where we lauch the file manager bar.
def OpenFile():
    name = askopenfilename(filetypes =(("Image","*.jpg"),("Video", "*.mp4"),("All Files","*.*")),
                           title = "Choose a file."
                           )

    cmd1='python object_detection_yolo2.py --image='+name
    cmd2='python object_detection_yolo2.py --video='+name
    #Using try in case user types in unknown file or closes without choosing a file.
    if name.find(".mp4") == -1:
        Popen(cmd1)
    else:
        Popen(cmd2)

def data():
    Popen('python 1-face_datasets.py')

def train():
    Popen('python 2-training.py')

def dect():
    Popen('python 3-face_recognition.py', shell=True)

btn1 = Button(window, text="select",bg='orange', command=OpenFile, width=30, height=2)
btn1.grid(column=5, row=2, padx=15, pady=10)

btn4 = Button(window, text="Dataset",bg='orange', command=data, width=30, height=2)
btn4.grid(column=9, row=2, padx=50, pady=10)

btn2 = Button(window, text='Cam',bg='orange', command=wbc, width=30, height=2)
btn2.grid(column=5, row=5, padx=15, pady=10)

btn5 = Button(window, text="Trainer",bg='orange', command=train, width=30, height=2)
btn5.grid(column=9, row=5, padx=50, pady=10)

btn3 = Button(window, text='Exit',bg='orange', command=window.destroy, width=30, height=2)
btn3.grid(column=5, row=6, padx=15, pady=10)

btn6 = Button(window, text="Recognition",bg='orange', command=dect, width=30, height=2)
btn6.grid(column=9, row=6, padx=50, pady=10)

window.geometry('580x250')
window.mainloop()
