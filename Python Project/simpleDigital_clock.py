from tkinter import * 
import time

class App(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.label = Label(root, font = ("digital-7", 40, "bold"),
                background = "black",
                foreground = "red")

        self.label.pack(anchor = "center", fill="both", expand=True)
        self.time()
        self.flash()

    def flash(self):
        bg = self.label.cget("background")
        fg = self.label.cget("foreground")
        self.label.configure(background=fg, foreground=bg)
        self.after(250, self.flash)
    
    def time(self):
        string = time.strftime("%H:%M:%S %p")
        self.label.config(text=string)
        self.label.after(1000, time)

root = Tk()
root.geometry("600x400")
app = App(root)
root.title("Digital Clock")
root.after(1000, app.time)
root.mainloop()