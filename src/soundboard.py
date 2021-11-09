import soundboardconstants
import logging
import threading
import sounddevice

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
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
    name = "Audio"

    global playAudio, statusbartext
    logging.info("Thread %s: starting", name)

    while runAudioThread:
        sound = AudioSegment.from_file("sounds/sinalco.wav", format="wav")

        if playAudio:
            logging.info("Thread %s: playing audio", name)
            statusbartext.set("Playing audio...")
            play(sound)
            logging.info("Thread %s: sleeping", name)
            statusbartext.set(soundboardconstants.STATUSBARDEFAULT)

        playAudio = False

    logging.info("Thread %s: finishing", name)


def doshutdown():
    global runAudioThread
    statusbartext.set("Exiting...")

    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        runAudioThread = False
        soundboardRoot.destroy()

    statusbartext.set(soundboardconstants.STATUSBARDEFAULT)


"""
    Soundboard Menubar
"""
menubar = Menu(soundboardRoot)

filemenu = Menu(menubar)
filemenu.add_command(label="Load configuration", command=onopen)
filemenu.add_command(label="Save configuration", command=onsave)
filemenu.add_command(label="Exit", command=soundboardRoot.destroy)

devicemenu = Menu(menubar)
for element in sounddevice.query_devices():
    if element["max_input_channels"] == 0 & element["hostapi"] == 0:
        devicemenu.add_radiobutton(label=element["name"])

menubar.add_cascade(label="Application", menu=filemenu)
menubar.add_cascade(label="Device", menu=devicemenu)
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
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")

    logging.info("Main    : before creating thread")
    audioThread = threading.Thread(target=playaudiothread, args=(1,))
    logging.info("Main    : before running thread")
    audioThread.start()
    logging.info("Main    : wait for the thread to finish")

    print("Found audio devices:")
    print(sounddevice.query_devices())

    soundboardRoot.protocol("WM_DELETE_WINDOW", doshutdown)
    soundboardRoot.mainloop()
    logging.info("Main    : all done")


