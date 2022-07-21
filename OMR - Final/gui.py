import tkinter as tk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo

# create the root window
root = tk.Tk()
root.title('Browse File')
root.resizable(False, False)
root.geometry('400x250')
root.configure(bg="black")


def select_file():
    global imgPath
    filetypes = (
        ('All files', '*.*'),
        ('Text files', '*.txt'),
        ('Templates files', '.tplate')
    )

    filename = fd.askopenfilename(
        title='Open a file',
        initialdir='/',
        filetypes=filetypes)

    showinfo(
        title='Selected File',
        message=filename
    )
    imgPath = filename
    print(imgPath)


# open button
open_button = tk.Button(
    root,
    text='Open a File',
    pady=30, padx=100,
    command=select_file,
    borderwidth=10,
    fg="cyan", bg="#3e423f"

)

# submit button
submit_button = tk.Button(
    root,
    text="Submit File",
    pady=20, padx=50,
    command=root.destroy,
    borderwidth=5,
    fg="cyan", bg="#3e423f"
)

open_button.pack(expand=True)
submit_button.pack(expand=True)
# run the application

root.mainloop()