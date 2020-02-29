import tkinter as tk

root = tk.Tk()
login_GUI = tk.Frame(root)
welcome = tk.Label(login_GUI, text="Hello Tk!", width="30", height="5")
welcome.pack()
# root.tk.call('wm', 'iconphoto', root.w, tk.PhotoImage(file='./asset/new.png'))
root.mainloop()
