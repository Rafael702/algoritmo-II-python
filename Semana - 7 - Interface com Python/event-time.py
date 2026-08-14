import sys
from pathlib import Path
from tkinter import Button
from tkinter.messagebox import showinfo
from time import strftime, localtime

sys.path.append(str(Path(__file__).resolve().parents[1]))

from comum.janela import executar_janela


def clicked():
    time = strftime('Day: %d %b %Y\nTime: %H:%M:%S%p\n', localtime())
    showinfo(message=time)


def construir(root):
    button = Button(root, text='Clique', command=clicked)
    button.pack()


executar_janela(construir)
