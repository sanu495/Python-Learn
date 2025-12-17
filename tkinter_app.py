# Tkinter for developing a Deskttop application

import tkinter as tks

# Step 1: create the main window

root =tks.Tk()
root.title("My First GUI")
root.geometry("400x300") # set width and height

# Step 2: Add a label

label=tks.Label(root, text="Hello, Tkinter",font="Arial")
label.pack(pady=20) # Add vertical padding

# Step 3: Add a button

def on_click():
    label.config(text="You Clicked the button")

button=tks.Button(root, text="click me", command=on_click)