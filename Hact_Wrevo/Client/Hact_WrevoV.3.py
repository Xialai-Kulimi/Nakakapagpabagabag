import tkinter as tk

root = tk.Tk()
main_windows = tk.Frame(root)
hello = tk.Label(root, text="Hello Tk!", width="30", height="5")
hello.pack()
root.iconbitmap('./asset/Hact.ico')
root.mainloop()
