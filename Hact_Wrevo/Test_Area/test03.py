import tkinter as tk

root = tk.Tk()
root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
root.resizable(False, False)
root.update_idletasks()
root.overrideredirect(True)
root.mainloop()
