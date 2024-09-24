import tkinter as tk
import message_box

def showdata():
    options.config(text=str(color_var.get()))

    


scr = tk.Tk()
scr.title("RadioButton and CheckBox")

#Label for text
label = tk.Label(scr, text="Select color")
label.pack()

color_var = tk.StringVar(value="Blue")
#RadioButtons
#red
red = tk.Radiobutton(scr, text="red", value="Red", variable=color_var)
red.pack()
#blue
blue = tk.Radiobutton(scr, text="blue", value="Blue", variable=color_var)
blue.pack()
#green
green = tk.Radiobutton(scr, text="green", value="Green", variable=color_var)
green.pack()

options = tk.Label(scr, text=str(color_var.get()))
options.pack()

button = tk.Button(scr, text="update", command=showdata)
button.pack()




scr.mainloop()