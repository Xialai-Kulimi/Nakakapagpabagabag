import tkinter as tk

root = tk.Tk()
main_windows = tk.Frame(root)
hello = tk.Label(root, text="Hello Tk!", width="30", height="5")
hello.pack()
# root.tk.call('wm', 'iconphoto', root.w, tk.PhotoImage(file='./asset/new.png'))
root.mainloop()
