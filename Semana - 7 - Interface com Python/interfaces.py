from tkinter import Tk, Label, PhotoImage, TOP, BOTTOM

root = Tk()
photo = PhotoImage(file="gif.gif").subsample(5)
#hello = Label(master=root, text="Ola mundo!", image=photo, width=300, height=300)
#hello.pack()
image = Label(master=root, image=photo)
image.pack(side=TOP)
text = Label(master=root, font=("Courier", 18), text='Ola alunos da UNIVESP')
text.pack(side=BOTTOM)
root.mainloop() #cria janela

