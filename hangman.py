from tkinter import *
import random
from tkinter import ttk
from PIL import Image, ImageTk
import subprocess

w = Tk()
w.title("Hangman Game")
w.geometry('600x600')
w.maxsize(600,600)
w.minsize(600, 600)
w.config(bg='#4B0082')
def open_game():
    w.destroy()
    subprocess.run(['python', 'game.py'],shell=True)
def resize_image(image_path, new_width=300, new_height=250):
    image = Image.open(image_path)
    resized_image = image.resize((new_width, new_height))
    return ImageTk.PhotoImage(resized_image)
Label(w, text="  In a world where every letter counts, seize the moment and guess the word!               ",
      width=75, height=1, bg='#CD8500', fg='black',font=('roboto',10,'bold') ,anchor='e').place(x=0,y=0)

img = resize_image("image1.png", new_width=400, new_height=500)
fimg = Label(w, image=img,bg='#4B0082')
fimg.place(x=240,y=40)
text = "HANGMAN\nGAME"
Label(w , text=text,
      width=10, height=3, bg='#4B0082', fg='black',font=('Hobo Std',36,'bold') ,anchor='e').place(x=30,y=170)
t="       Can you guess the word before it's too late?  \nPlay Hangman and test your word-guessing skills!"
Label(w, text=t,width=43, height=2 ,bg='#4B0082', fg='white',font=('forte',14) ,anchor='e').place(x=20,y=535)
play_button = ttk.Button(w, text="Play", style='Custom.TButton',width=5,command= open_game)
play_button.place(x=80,y=380)
play_button.config(width=10)
def on_enter(event):
    style.configure('Custom.TButton', background='black') 

def on_leave(event):
    style.configure('Custom.TButton', background='blue')

style = ttk.Style()
style.configure('Custom.TButton',font = ('forte',16,'bold'),width=10, background='blue',  foreground="black",
                borderwidth=3,height =0, relief=SOLID,
                cursor="hand2", padding=10)  
style.map('Custom.TButton', background=[('pressed', 'pink'), ('active', 'blue'), ('disabled', 'black')])
play_button.configure(style='Custom.TButton')
w.mainloop()
