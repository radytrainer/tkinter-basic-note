import tkinter as tk

# create window object
window = tk.Tk()

# create title on window
window.title("My Game tile")

# Window size
window.geometry("300x400")

# create text label in window
label = tk.Label(window, text="Text in window")

# To display text label
label.pack()

# your code more here

# Build the window object
window.mainloop()

