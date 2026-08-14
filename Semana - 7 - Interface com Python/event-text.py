import sys
from pathlib import Path
from tkinter import Button, Label, Entry
from tkinter.messagebox import showinfo
from time import strftime, strptime

sys.path.append(str(Path(__file__).resolve().parents[1]))

from comum.janela import executar_janela

entry = None


def clicked():
    date = entry.get()
    weekday = strftime('%A', strptime(date, '%b %d, %Y'))
    showinfo(message='{} was a {}'.format(date, weekday))


def construir(root):
    global entry
    label = Label(root, text="Digite uma data:")
    label.grid(row=0, column=0)
    entry = Entry(root)
    entry.grid(row=0, column=1)

    button = Button(root, text='Clique', command=clicked)
    button.grid(row=1, column=0, columnspan=2)


executar_janela(construir)
