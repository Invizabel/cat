from tkinter import *

x = 128
y = 128

def crawl():
    global x
    if x < 640:
        x += 10
        root.geometry(f"50x50+{x}+200")
        root.after(1000, crawl)

# Must be a png
# Must be at most 50x50 pixels (will look at shrinking it further)
root = Tk()
root.overrideredirect(True)
root.geometry(f"50x50+{x}+200")
root.minsize(50, 50)
img = PhotoImage(file="cat.png")
label = Label(root, image=img)
label.pack()
root.after(1000, crawl)
root.mainloop()
