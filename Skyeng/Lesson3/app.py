import tkinter as tk

def button_click(button_number):
    print(f"Bogdan {button_number} clicked!")

root = tk.Tk()

button1 = tk.Button(root, text="Bogdan 1", command=lambda: button_click(1))
button2 = tk.Button(root, text="Bogdan 2", command=lambda: button_click(2))
button3 = tk.Button(root, text="Bogdan 3", command=lambda: button_click(3))

button1.pack()
button2.pack()
button3.pack()

root.mainloop()

