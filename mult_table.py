import tkinter as tk
from tkinter import messagebox

def generate_table():
    pass

scr = tk.Tk()
scr.title("Multiplication Table Generator")

# ask num label
label = tk.Label(scr, text="Enter a number:")
label.pack(pady=10)

#ask num
entry = tk.Entry(scr)
entry.pack(pady=10)

# button
button = tk.Button(scr, text="Generate Table", command=generate_table)
button.pack(pady=10)

#text
result_text = tk.Text(scr, height=10, width=30)
result_text.pack(pady=10)

scr.mainloop()
