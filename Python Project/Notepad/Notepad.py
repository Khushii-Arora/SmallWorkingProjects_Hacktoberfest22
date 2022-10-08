from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os


def new():
    global file
    root.title("Simple Notepad")
    file = None
    Textarea.delete(1.0, END)


def open_file():
    global file
    file = askopenfilename(defaultextension=".txt", filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])
    if file == "":
        file = None
    else:
        root.title(os.path.basename(file) + "Notepad")
        Textarea.delete(1.0, END)
        f = open(file, "r")
        Textarea.insert(1.0, f.read())
        f.close()


def save():
    global file
    if file == None:
        file = asksaveasfilename(initialfile = 'Untitled.txt', defaultextension=".txt", filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])
        if file == "":
            file = None

        else:
            f = open(file, "w")
            f.write(Textarea.get(1.0, END))
            f.close()

            root.title(os.path.basename(file) + " - Notepad")
            print("File Saved")
    else:
        f = open(file, "w")
        f.write(Textarea.get(1.0, END))
        f.close()


def quit_app():
    root.destroy()


def cut():
    Textarea.event_generate(("<<Cut>>"))


def copy():
    Textarea.event_generate(("<<Copy>>"))


def paste():
    Textarea.event_generate(("<<Paste>>"))


def about():
    showinfo("Help", "Notepad made my Mihir Aman Raj")


if __name__ == '__main__':
    root = Tk()
    root.geometry("600x700")
    root.title("Simple Notepad")
    root.wm_iconbitmap("1.ico")

    Textarea = Text(root, font="lucida 19")
    file = None
    Textarea.pack(expand=True, fill=BOTH)

    MenuBar = Menu(root)
    FileMenu = Menu(MenuBar, tearoff=0)
    FileMenu.add_command(label="New", command=new)
    FileMenu.add_command(label="Save", command=save)
    FileMenu.add_command(label="Open", command=open_file)
    FileMenu.add_separator()
    FileMenu.add_command(label="Exit", command=quit_app)
    MenuBar.add_cascade(label="File", menu=FileMenu)

    EditMenu = Menu(MenuBar, tearoff=0)
    EditMenu.add_command(label="Cut", command=cut)
    EditMenu.add_command(label="Copy", command=copy)
    EditMenu.add_command(label="Paste", command=paste)
    MenuBar.add_cascade(label="Edit", menu=EditMenu)

    HelpMenu = Menu(MenuBar, tearoff=0)
    HelpMenu.add_command(label="Help", command=about)
    MenuBar.add_cascade(label="Help", menu=HelpMenu)

    root.config(menu=MenuBar)
    Scroll = Scrollbar(Textarea)
    Scroll.pack(side=RIGHT, fill=Y)
    Scroll.config(command=Textarea.yview)
    Textarea.config(yscrollcommand=Scroll.set)

    root.mainloop()