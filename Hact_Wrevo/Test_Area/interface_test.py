import tkinter as tk
import os

root = tk.Tk()
root.title('Hact_Wrevo')
root.geometry('800x600')
# top_frame = tk.Frame(root)
# top_frame.pack()
# root.overrideredirect(True)
# root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

print(screen_height, screen_width)

root.mainloop()

while True:
    pass
