from tkinter import *
from tkinter import ttk
from multiprocessing import Process
import tkinter as tk
import random
import time
import wordle_bot

class GUI:
    def __init__(self):
        f = open("cuvinte_wordle.txt", 'r')
        words = list(i.strip() for i in f)

        self.row = 1
        self.word = ""
        self.wordToGuess = random.choice(words)

        self.init_auto()

    def init_auto(self):
        global root

        root = tk.Tk()
        root.config(background="#f8f8f8")  
        root.title("Wordle")
        width = 340
        height = 720

        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()

        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)

        root.geometry("%dx%d+%d+%d" % (width, height, x, y))

        for x in range(7):
            l = tk.Label(
                root,
                text=" ",
                font=("Calibri", 30),
                background="#f8f8f8",  
            )
            l.grid(row=0, column=x, sticky=N + S + E + W, padx=10, pady=10)

        label1 = tk.Label(
            root,
            text=self.wordToGuess,
            font=("Calibri", 30),
            justify="center",
            anchor=CENTER,
            background="#f8f8f8",  
            foreground="#151515",
        )
        label1.grid(row=0, columnspan=7, sticky=N + S + E + W, padx=30, pady=10)

        self.addWord()

        if self.word == "🟩🟩🟩🟩🟩":
            again = tk.Label(
                root,
                text="AGAIN",
                font=("", 15),
                foreground="#f1f1f1",
                background="#363636",  
                width=10,
                anchor="center",
            )
            again.bind(
                "<Button-1>",
                lambda self: [
                    root.destroy(),
                    Process(target=wordle_bot.auto).start(),
                    Process(target=GUI).start(),
                ],
            )
            again.grid(row=self.row + 1, columnspan=7, padx=10, pady=15)
            root.update()

        root.mainloop()

    def addWord(self):
        f = open("output.txt", 'r+')
        f.seek(0)
        self.word = f.read()
        pattern = ""

        for i in range(5):
            label = tk.Label(root, text=self.word[i].upper())

            if self.word[i] == self.wordToGuess[i]:
                label.config(background="#4CAF50")  
                pattern += "🟩"
            elif self.word[i] in self.wordToGuess:
                label.config(background="#FFC107")  
                pattern += "🟨"
            else:
                label.config(background="#757575")  
                pattern += "⬜"

            label.config(
                foreground="#d7dadc",
                font=("Arial", 30),
                width=2,
                justify="center",
                anchor="center",
            )
            label.grid(row=self.row, column=i+1, padx=3, pady=5)

            time.sleep(0.1)
            root.update()

        f = open("output.txt", "w", encoding="utf-8")
        f.write(pattern)

        self.row += 1

        f = open("output.txt", "r+", encoding="utf-8")
        self.word = f.read()

        f = open("output.txt", "r+", encoding="utf-8")
        while self.word == f.read():
            f = open("output.txt", "r+", encoding="utf-8")
            f.seek(0)

        if self.word == "🟩🟩🟩🟩🟩":
            return

        time.sleep(0.1)
        self.addWord()

if __name__ == "__main__":
    gui_process = Process(target=GUI)
    bot_process = Process(target=wordle_bot.auto)

    gui_process.start()
    bot_process.start()

    bot_process.join()
    gui_process.join()
