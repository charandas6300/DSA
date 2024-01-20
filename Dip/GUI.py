import tkinter as tk

def button_click():
    entry1 = entry.get()
    label.config(text=entry1)

root = tk.Tk()
root.title("My GUI App")

label = tk.Label(root, text="Hello, GUI!")
button = tk.Button(root, text="Click Me", command=button_click)
entry = tk.Entry(root, width=30)


label.pack()
button.pack()
entry.pack()

root.mainloop()
