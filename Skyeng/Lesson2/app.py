from tkinter import *

def center(win):
    win.update_idletasks()
    width = win.winfo_width()
    height = win.winfo_height()
    x = (win.winfo_screenwidth() // 2) - (width // 2)
    y = (win.winfo_screenheight() // 2) - (height // 2)
    win.geometry('{}x{}+{}+{}'.format(width, height, x, y))

window = Tk()
window.title('Bogdan lol')
window.geometry('650x500')
center(window)
window.resizable(False, False)

window.configure(bg="orange")
window.mainloop()

