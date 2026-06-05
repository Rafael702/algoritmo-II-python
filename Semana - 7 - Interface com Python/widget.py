from tkinter import Tk, Label, RAISED

root = Tk()
labels = [['1','2','3'], ['4','5','6'],['7','8', '9'],['*','0','#']]

for row in range(4):
    for column in range(3):
        label = Label(root, relief=RAISED, padx=10, text=labels[row][column])
        label.grid(row=row, column=column)

root.mainloop()