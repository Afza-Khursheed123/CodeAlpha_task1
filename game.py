from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import random

game = Tk()
game.title("Game")
game.geometry("600x600")
game.maxsize(600, 600)
game.minsize(300, 300)
game.config(bg='#4B0082')
Label(game, text="  In a world where every letter counts, seize the moment and guess the word!               ",
      width=75, height=1, bg='#CD8500', fg='black',font=('roboto',10,'bold') ,anchor='e').place(x=0,y=0)

def resize_image(image_path, new_width=80, new_height=100):
    image = Image.open(image_path)
    resized_image = image.resize((new_width, new_height))
    return ImageTk.PhotoImage(resized_image)

Label(game, text="LET'S PLAY THE HANGMAN",fg ='black', font=('Hobo Std', 28, 'bold'), anchor='center', bg='#4B0082').place(x=40, y=30)
Label(game, text="Guess the word!",fg='#CD8500' ,font=('AlQalam Mujeeb', 28,'bold'), anchor='center', bg='#4B0082').place(x=130, y=120)
happy_face = "\U0001F604" 
img2 = resize_image("image2.png")
f1img2 = Label(game, image=img2,bg='#4B0082')
f1img2.place(x=420, y=85)

def word_choice():
    words = ["hangman", "python", "program", "computer", "keyboard", "mouse","hello","pin","frock","pizza",
             "juice","eat","tie","water","popcorn","potato","doctor","google","torch","pencil","eraser","keychain"]
    return random.choice(words)

def display_word(word, guessed_letters):
    display = ''
    for letter in word:
        if letter in guessed_letters:
            display += letter + ' '
        else:
            display += ' ___ '
    return display.strip()

word_display_label = Label(game, font=('roboto', 20, 'bold'), anchor='center', bg='#4B0082')
word_display_label.grid(padx=100, pady=200)

guessed_letters = []
wrong_ans = 0
max_wrong_ans = 6
word = word_choice()
def update_word_position():
    word_display = word_display_label.cget("text")
    word_width = word_display_label.winfo_reqwidth()
    x_position = (game.winfo_width() - word_width) / 2
    word_display_label.place(x=x_position, y=250)
def check_guess():
    global wrong_ans
    global max_wrong_ans
    global word
    global guessed_letters
    
    entered_text = guess.get().lower()
    if entered_text == "":
        return    
    if entered_text in guessed_letters:
        warn = Label(game, text='You already guessed that letter!', width=30,font=('roboto', 14, 'bold'), 
                     anchor='center', bg='#4B0082')
        warn.place(x=100, y=400)
    elif entered_text in word:
        guessed_letters.append(entered_text)
        warn = Label(game, text=f'Correct Guess {happy_face}', width=30, fg='#3CB371',font=('roboto', 14, 'bold'),
                      anchor='center', bg='#4B0082').place(x=110, y=400)
        word_display = display_word(word, guessed_letters)
        word_display_label.config(text=word_display)
        update_word_position()
    else:
        max_wrong_ans -= 1
        warn = Label(game, text='Incorrect Guess❌\n\n({} Guesses left☹️)'.format(max_wrong_ans),fg='#CD5555',
                      width=40,font=('roboto', 14, 'bold'), anchor='center', bg='#4B0082')
        warn.place(x=60, y=400)
    if wrong_ans>=max_wrong_ans:
        warn = Label(game, text=f'You ran out of guesses☹️\nthe word was\n"{word}"', 
                     width=26,fg='#FF6A6A' ,font=('AlQalam Mujeeb', 24,'bold'), anchor='center', bg='#4B0082')
        warn.place(x=30, y=320)
        game.after(3000, game.destroy)
    if all(letter in guessed_letters for letter in word):
        warn = Label(game, text=f'Congratulations!{happy_face}\nYou guessed the word \n"{word}"',fg='#CDC5BF',
                      width=22,font=('AlQalam Mujeeb', 28,'bold'), anchor='center', bg='#4B0082')
        warn.place(x=30, y=320)
        game.after(3000, game.destroy)
    guess.delete(0, END)
while wrong_ans <= max_wrong_ans:
    word_display = display_word(word, guessed_letters)
    word_display_label.config(text=word_display) 
    game.update()  

    word_width = word_display_label.winfo_reqwidth()
    x_position = (game.winfo_width() - word_width) / 2
    word_display_label.place(x=x_position, y=250)

    Label(game, text='Enter the letter you guessed', font=('roboto', 14, 'bold'), 
            anchor='center', bg='#4B0082').place(x=110, y=330)
    guess = Entry(game, text="guess", font=('poppins', 14, 'bold'), fg='black', bg='#4B0082', width=6)
    guess.place(x=390, y=322)
    dropdown_button = ttk.Button(game, text="↓", width=3, command=check_guess)
    dropdown_button.place(x=470, y=334)

    entered_text = guess.get()
    game.wait_variable(word_display_label)

game.mainloop()