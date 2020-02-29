import tkinter as tk

window = tk.Tk()  # Creating the root window.
window.title('Hact Wrevo')  # Set the title.
login_GUI = tk.Frame(window)  # Create the group of login GUI.
login_GUI.pack(side=tk.TOP)

welcome = tk.Label(login_GUI, text="Hello Tk!")
welcome.pack()

try:
    window.tk.call('wm', 'iconphoto', window.w, tk.PhotoImage(file='./asset/new.png'))
except:
    pass

window.mainloop()
