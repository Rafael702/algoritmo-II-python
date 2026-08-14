import sys
from pathlib import Path
from tkinter import Label, PhotoImage, TOP, BOTTOM

sys.path.append(str(Path(__file__).resolve().parents[1]))

from comum.janela import executar_janela


def construir(root):
    photo = PhotoImage(file=str(Path(__file__).parent / 'gif.gif')).subsample(5)
    image = Label(master=root, image=photo)
    image.image = photo
    image.pack(side=TOP)
    text = Label(master=root, font=("Courier", 18), text='Ola alunos da UNIVESP')
    text.pack(side=BOTTOM)


executar_janela(construir)
