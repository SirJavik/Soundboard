import soundboardconstants
import logging
import threading

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from resource_path import *
from filehandler import *
from languageHandler import *

from pydub import AudioSegment
from pydub.playback import play

languages = Languages()
languages.load("languages/de_DE.sbl")

"""
    Soundboard root
"""
soundboardRoot = Tk()
soundboardRoot.geometry("800x400")
soundboardRoot.title("Soundboard")
soundboardRoot.iconbitmap(resource_path("musiknoten-symbol.ico"))

for i in range(3):
    soundboardRoot.columnconfigure(i, weight=1)
    soundboardRoot.rowconfigure(i, weight=1)

playAudio = False
runAudioThread = True

"""
    Soundboard Statusbar
"""
statusbartext = StringVar()
statusbartext.set(soundboardconstants.STATUSBARDEFAULT)
statusbar = Label(soundboardRoot, textvariable=statusbartext, bd=1, relief=SUNKEN, anchor=W)
statusbar.grid(row=3, column=0, sticky='ew', columnspan=3)


def playaudio():
    global playAudio

    playAudio = True


def playaudiothread(name):
    loggingPrefix = "Thread %s :"
    name = "Audio"

    global playAudio, statusbartext
    logging.info(f"{loggingPrefix} starting", name)

    while runAudioThread:
        sound = AudioSegment.from_file("sounds/sinalco.wav", format="wav")

        if playAudio:
            logging.info(f"{loggingPrefix} playing audio", name)
            statusbartext.set("Playing audio...")
            play(sound)
            logging.info(f"{loggingPrefix} sleeping", name)
            statusbartext.set(soundboardconstants.STATUSBARDEFAULT)

        playAudio = False

    logging.info(f"{loggingPrefix} finishing", name)


def doshutdown():
    global runAudioThread
    statusbartext.set("Exiting...")

    if messagebox.askokcancel(languages.getlanguagestr('filemenuExit'), languages.getlanguagestr('quitDialogQuestion')):
        runAudioThread = False
        soundboardRoot.destroy()

    statusbartext.set(soundboardconstants.STATUSBARDEFAULT)


"""
    Soundboard Menubar
"""
menubar = Menu(soundboardRoot)

filemenu = Menu(menubar)
filemenu.add_command(label=languages.getlanguagestr('filemenuLoadConfiguration'), command=onopen)
filemenu.add_command(label=languages.getlanguagestr('filemenuSaveConfiguration'), command=onsave)
filemenu.add_command(label=languages.getlanguagestr('filemenuExit'), command=doshutdown)

menubar.add_cascade(label="Application", menu=filemenu)
soundboardRoot.config(menu=menubar)

"""
    Soundboard inner frame
"""

rowCount = 0
btnNumber = 1
while rowCount != 3:
    for i in range(3):
        ttk.Button(soundboardRoot, text=f"Button {btnNumber}", command=playaudio).grid(column=i, row=rowCount,
                                                                                       sticky="nesw")
        btnNumber += 1
    rowCount += 1

if __name__ == '__main__':
    loggingPrefix = "Main         :"

    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")

    logging.info(f"{loggingPrefix} before creating thread")
    audioThread = threading.Thread(target=playaudiothread, args=(1,))
    logging.info(f"{loggingPrefix} before running thread")
    audioThread.start()
    logging.info(f"{loggingPrefix} wait for the thread to finish")

    soundboardRoot.protocol("WM_DELETE_WINDOW", doshutdown)



    soundboardRoot.mainloop()
    logging.info(f"{loggingPrefix} all done")


