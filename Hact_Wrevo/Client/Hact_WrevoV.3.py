import tkinter as tk

window = tk.Tk()
window.title('Hact Wrevo')
login_GUI = tk.Frame(window)
welcome = tk.Label(login_GUI, text="Hello Tk!", width="30", height="5")
welcome.pack()
# root.tk.call('wm', 'iconphoto', root.w, tk.PhotoImage(file='./asset/new.png'))
window.mainloop()
