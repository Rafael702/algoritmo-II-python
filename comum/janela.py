"""Rotina comum de criacao de janelas Tkinter usadas nos exemplos de interface."""

from tkinter import Tk


def executar_janela(construir, titulo='UNIVESP'):
    """Cria a janela, delega o conteudo para `construir(root)` e inicia o loop."""
    root = Tk()
    root.title(titulo)
    construir(root)
    root.mainloop()
    return root
