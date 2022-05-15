from tkinter import *
from tkinter import messagebox
from tkinter import ttk


def quit_app():
    root.quit()


def set_font(value):
    text_box.set(value)


def set_style(value):
    word_style.set(value)

def show_warning(event=None):
    messagebox.showwarning("Self Destruct", "Are you sure you want to self destruct?")


root = Tk()
root.title("Message Box")

main_menu = Menu(root)

# Pull-down menu
file_menu = Menu(main_menu)
file_menu.add_command(label="Open")
file_menu.add_command(label="Close", command=quit_app)
file_menu.add_command(label="New")
main_menu.add_cascade(label="File", menu=file_menu)

# Radio buttons
text_box = StringVar()
font_menu = Menu(main_menu)
font_menu.add_radiobutton(label="Times New Roman", command=lambda: set_font("Times New Roman"))
font_menu.add_radiobutton(label="Arial", command=lambda: set_font("Arial"))
font_menu.add_radiobutton(label="Comic Sans", command=lambda: set_font("Comic Sans"))
main_menu.add_cascade(label="Font", menu=font_menu)

# Checkbutton
word_style = StringVar()
format_menu = Menu(main_menu)
format_menu.add_checkbutton(label="Italicize", command=lambda: set_style("italicized"))
main_menu.add_cascade(label="Format", menu=format_menu)

# Pop-Up

help_menu = Menu(main_menu)
help_menu.add_command(label="Self destruct", accelerator="Control-a", command=show_warning)
main_menu.add_cascade(label="Help", menu=help_menu)

root.bind("<Control-A>", show_warning)
root.bind("<Control-a>", show_warning)
root.config(menu=main_menu)
root.mainloop()
