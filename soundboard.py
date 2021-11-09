import os
import soundboardconstants

from tkinter import *
from tkinter import ttk
from playsound import playsound
from resource_path import *
from filehandler import *

from pydub import AudioSegment
from pydub.playback import play

"""
    Soundboard root
"""
soundboardRoot = Tk()
soundboardRoot.geometry("800x400")
soundboardRoot.title("Soundboard")
soundboardRoot.iconbitmap(resource_path("./musiknoten-symbol.ico"))

for i in range(3):
    soundboardRoot.columnconfigure(i, weight=1)
    soundboardRoot.rowconfigure(i, weight=1)

def playaudio():
    play(AudioSegment.from_wav("sounds/sinalco.wav"))



"""
    Soundboard Menubar
"""
menubar = Menu(soundboardRoot)
filemenu = Menu(menubar)
filemenu.add_command(label="Load configuration",    command=onopen)
filemenu.add_command(label="Save configuration",    command=onsave)
filemenu.add_command(label="Exit",                  command=soundboardRoot.destroy)
menubar.add_cascade(label="Application", menu=filemenu)
soundboardRoot.config(menu=menubar)

"""
    Soundboard inner frame
"""

rowCount = 0
btnNumber = 1
while rowCount != 3:
    for i in range(3):
        ttk.Button(soundboardRoot, text=f"Button {btnNumber}", command=playaudio).grid(column=i, row=rowCount, sticky="nesw")
        btnNumber += 1
    rowCount += 1



"""
    Soundboard Statusbar
"""
statusbar = Label(soundboardRoot, text="To Boldly Go Where No Man Has Gone Before.", bd=1, relief=SUNKEN, anchor=W)
statusbar.grid(row=3, column=0, sticky='ew', columnspan=3)

if __name__ == '__main__':
    soundboardRoot.mainloop()
