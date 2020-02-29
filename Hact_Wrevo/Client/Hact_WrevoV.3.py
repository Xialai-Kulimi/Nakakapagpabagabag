import tkinter as tk

window = tk.Tk()  # Creating the root window.
window.title('Hact Wrevo')  # Set the title.
window['bg'] = 'black'
login_GUI = tk.Frame(window)  # Create the group of login GUI.
login_GUI.pack()

welcome = tk.Label(login_GUI, text="Hello Tk!", fg='white', bg='black', font='helvetica 24')
welcome.pack()

# root.tk.call('wm', 'iconphoto', root.w, tk.PhotoImage(file='./asset/new.png'))
window.mainloop()
