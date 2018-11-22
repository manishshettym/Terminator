import tkinter as tk
from PIL import ImageTk ,Image


root = tk.Tk()
root.title("Displaying an image")

root.geometry("300x300")
root.configure(background='grey')

path = "wall.jpg"
photo = ImageTk.PhotoImage(Image.open(path))

panel = tk.Label(root,image=photo)
panel.pack(side="bottom",fill = "both" , expand="yes")

root.mainloop()
