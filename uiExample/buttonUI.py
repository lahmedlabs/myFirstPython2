import tkinter as tk

def on_button_click_ok():
    label.config(text="Hello, Tkinter!")

def on_button_click_cc():
    label.config(text="Canceled!")

root = tk.Tk()
root.title("Tkinter Example")

label = tk.Label(root, text="Click the button")
label.pack()

button1 = tk.Button(root, text="OK", command=on_button_click_ok)
button1.pack()

button2 = tk.Button(root, text="Cancel", command=on_button_click_cc)
button2.pack()


root.mainloop()
