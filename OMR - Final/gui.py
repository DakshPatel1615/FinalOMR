from tkinter import *
from tkinter import filedialog, ttk
import tkinter.messagebox
import time


class gui:
    def __init__(self, window, title, background):
        self.window = Tk()
        self.background = background
        self.title = title
        self.window.title("GUI")
        self.window.resizable(0, 0)
        self.window.geometry('724x380')
        self.window.config(bg=self.background)
        show_msg = False

    def create_window(self):
        def save_data():
            data = {}
            data["class"] = class_list_box.get()
            data["section"] = section_list_box.get()
            data["exam"] = exam_list_box.get()
            print(data)  # Prints the data dictionary

        def select_folder():
            path = filedialog.askdirectory(initialdir="C:/Users", title="Select a folder...")  # Select a folder
            path_var = path  # Saves path location in path variable
            save_data()
            print(f"Selected folder: {path_var}")  # Prints the selected path
            time.sleep(1)
            tkinter.messagebox.showinfo("Folder selected", "Your folder has been uploaded successfully")
            self.window.destroy()

        class_list = [i for i in range(1, 13)]  # List of classes
        section_list = [chr(i) for i in range(65, 65 + 8)]  # List of sections
        exam_list = ["PA-1", "Term-1", "PA-2", "Term-2"]

        class_label = Label(self.window, text="Class", font="algerian 26 bold", padx=15, bg=self.background)
        class_list_box = ttk.Combobox(self.window, values=class_list, state="readonly", width=4, font="arial 24 bold")
        class_label.place(x=62, y=69)
        class_list_box.place(x=85, y=130)

        section_label = Label(self.window, text="Section", font="algerian 26 bold", padx=15, bg=self.background)
        section_list_box = ttk.Combobox(self.window, values=section_list, state="readonly", width=5,
                                        font="arial 24 bold")
        section_label.place(x=290, y=66)
        section_list_box.place(x=312, y=130)

        exam_label = Label(self.window, text="Exam", font="algerian 26 bold", bg=self.background)
        exam_list_box = ttk.Combobox(self.window, values=exam_list, state="readonly", width=7, font="arial 24 bold")
        exam_label.place(x=545, y=66)
        exam_list_box.place(x=525, y=130)

        button_btn = Button(self.window, text="Select a folder", font="algerian 26 bold", padx=5, pady=2,command=select_folder, borderwidth=5)
        button_btn.pack(side=BOTTOM, pady=50)




    def mainloop(self):
        self.window.mainloop()


if __name__ == "__main__":
    object = gui(object, background='#a3c3ff')
    object.create_window()
    object.mainloop()
