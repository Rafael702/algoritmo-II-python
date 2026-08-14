import sys
from pathlib import Path
from tkinter import Text, BOTH

sys.path.append(str(Path(__file__).resolve().parents[1]))

from comum.janela import executar_janela


def key_pressed(event):
    print('char: {}'.format(event.keysym))

def mouse_clicked_left(event):
    print('mouse left clicked')

def mouse_clicked_right(event):
    print('mouse right clicked')


def construir(root):
    text = Text(root, width=20, height=5)
    text.bind('<KeyPress>', key_pressed)
    text.bind('<Button-1>', mouse_clicked_left)
    text.bind('<Button-2>', mouse_clicked_right)
    text.pack(expand=True, fill=BOTH)


executar_janela(construir)
