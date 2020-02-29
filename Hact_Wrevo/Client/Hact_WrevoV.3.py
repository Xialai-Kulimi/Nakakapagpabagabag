import tkinter as tk

window = tk.Tk()  # Creating the root window.
window.title('Hact Wrevo')  # Set the title.
window['bg'] = 'black'
login_GUI = tk.Frame(window)  # Create the group of login GUI.
login_GUI.pack()

welcome = tk.Label(login_GUI, text="Login Hact Wrevo", fg='white', bg='black', font='helvetica 24')
welcome.pack()

try:
    window.tk.call('wm', 'iconphoto', window.w, tk.PhotoImage(file='./asset/new.png'))
except:
    pass

window.mainloop()
