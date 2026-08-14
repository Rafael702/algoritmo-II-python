import sys
from pathlib import Path
from tkinter import Label, RAISED

sys.path.append(str(Path(__file__).resolve().parents[1]))

from comum.janela import executar_janela

labels = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9'], ['*', '0', '#']]


def construir(root):
    for row in range(4):
        for column in range(3):
            label = Label(root, relief=RAISED, padx=10, text=labels[row][column])
            label.grid(row=row, column=column)


executar_janela(construir)
