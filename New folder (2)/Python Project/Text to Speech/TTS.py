from tkinter import *
import tkinter as tk
import pyttsx3

root = Tk()
root.title("Text to Speech")
root.geometry("400x200")
root.resizable(False, False)

#functin for speaknow
def speaknow():
    engine = pyttsx3.init()
    engine.say(textv.get())
    engine.runAndWait()
    engine.stop()

#Label Frame
LF = LabelFrame(root, text="Text to Speech", font=30, bd=4)
LF.pack(fill='both', expand='yes', padx=10, pady=10)

#label
lbl = Label(LF, text='Text', font = 60)
lbl.pack(side=tk.LEFT, padx=5)

#text entry
textv = StringVar()
text_entry = Entry(LF, width=25, font=30, bd=3, textvariable=textv)
text_entry.pack(side=tk.LEFT, padx=10)

#Button
btn = Button(LF, text='Speak', bg='black', fg='white', command=speaknow, font=20)
btn.pack(side=tk.LEFT, padx=10)

root.mainloop()