import tkinter as tk
from gtts import gTTS
from playsound import playsound

win = tk.TK()
win.title("Text TO Speech")
win.geometry("200*70")

def text_to_speech():
    text = entry.get()
    speech = gTTS(text=text,lang="en")
    speech.save(r'C:\Users\doros\Desktop\rr.mp3')
    playsound((r'C:\Users\doros\Desktop\rr.mp3')


label = tk.Label(win, text="Enter Here :")
label.grid(row=0,column=0)

entry = tk.Entry(win)
entry.grid(row=1,column=0)

button = tk.Button(win,text="Go",command=text_to_speech)
button.grid(row=1,column=1)

win.mainloop()
