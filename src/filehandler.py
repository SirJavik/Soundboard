import os
from tkinter import filedialog

def onopen():

    print(filedialog.askopenfilename(initialdir=os.getcwd(), title="Load configuration",
                                     filetypes=(("Soundboard configurations", "*.sbc;*.sbconf"), ("All files", "*.*"))))


def onsave():
    print(filedialog.asksaveasfilename(initialdir=os.getcwd(), title="Save configuration",
                                       filetypes=(("Soundboard configurations", "*.sbc;*.sbconf"), ("All files", "*.*"))))