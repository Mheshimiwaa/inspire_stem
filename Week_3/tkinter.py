#python user interface
import tkinter as tk

#Function to be executed
def button_click() :
    label.config(text="Button click me")

#create a tkinter window
Window =tk.Tk()
Window.title("Tkinter window ")

#label widget
label = tk.Label(Window, text="Welcome to python")
label.pack()

#create an entry
entry = tk.Entry(Window)
entry.pack()

#create a button
button = tk.Button(Window,text="Download video", command="button_click")
button.pack()

Window.mainloop()
