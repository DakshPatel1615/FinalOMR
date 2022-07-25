from tkinter import *
from tkinter import filedialog
from tkinter import ttk
import tkinter.messagebox
import time


class gui:
    def __init__(self, window, title, background):
        self.window = Tk()
        self.background = background
        self.title = title
        self.window.title(f"{self.title}")
        self.window.resizable(0, 0)
        self.window.geometry('924x530')
        self.window.config(bg=self.background)
        self.path_var = ''
        self.studentData = {}

    def create_window(self):
        def save_data():
            self.studentData["class"] = class_list_box.get()
            self.studentData["section"] = section_list_box.get()
            self.studentData["exam"] = exam_list_box.get()
            self.studentData["stream"] = stream_list_box.get()
            self.studentData["subject"] = subject_list_box.get()

        class_list = [i for i in range(1, 13)]  # List of classes
        section_list = []  # List of sections
        exam_list = ["PA-1", "Term-1", "PA-2", "Term-2"]  # List of Exams
        stream_list = ["Science", "Commerce", "Humanities"]  # List of streams
        subject_list = ["English", "Physics", "Chemistry", "Mathematics", "CS"]  # List of subjects

        def select_folder():
            path = filedialog.askdirectory(initialdir="C:/Users", title="Select a folder...")  # Select a folder
            save_data()
            self.path_var = path
            time.sleep(1.5)
            tkinter.messagebox.showinfo("Folder selected", "Your folder has been uploaded successfully")
            self.window.destroy()

        def allow_stream(*args):
            if class_list_box.current() in range(0, 10):
                global section_list
                section_list = ['A', 'B', 'C', 'D', 'E', 'F']
                section_list_box["state"] = "readonly"

            if class_list_box.current() in [10, 11]:
                stream_list_box["state"] = "readonly"

        def section_select(*args):
            if class_list_box.current() == 10 and stream_list_box.current() == 0:
                global section_list
                section_list = ['A', 'B', 'C']
                section_list_box["state"] = "readonly"


        class_label = Label(self.window, text="Class", font="algerian 26 bold", padx=15, bg=self.background)
        class_list_box = ttk.Combobox(self.window, values=class_list, state="readonly", width=4, font="arial 18 bold")
        class_label.place(x=65, y=69)
        class_list_box.place(x=97, y=130)

        class_list_box.bind("<<ComboboxSelected>>", allow_stream)

        stream_label = Label(self.window, text="Stream", font="algerian 26 bold", padx=15, bg=self.background)
        stream_list_box = ttk.Combobox(self.window, values=stream_list, state="disabled", width = 11, font = "arial 18 bold")
        stream_label.place(x=350, y=66)
        stream_list_box.place(x=357, y=130)

        stream_list_box.bind("<<ComboboxSelected>>", section_select)

        section_label = Label(self.window, text="Section", font="algerian 26 bold", bg=self.background)
        section_list_box = ttk.Combobox(self.window, values=section_list, state="disabled", width=3,font="arial 18 bold")
        section_label.place(x=685, y=66)
        section_list_box.place(x=720, y=130)

        subject_label = Label(self.window, text="Subject", font="algerian 26 bold", bg=self.background)
        subject_list_box = ttk.Combobox(self.window, values=subject_list, state="disabled", width=12,font="arial 18 bold")
        subject_label.place(x=190, y=200)
        subject_list_box.place(x=177, y=266)

        exam_label = Label(self.window, text="Exams", font="algerian 26 bold", bg=self.background)
        exam_list_box = ttk.Combobox(self.window, values=exam_list, state="disabled", width=8, font="arial 18 bold")
        exam_label.place(x=555, y=200)
        exam_list_box.place(x=555, y=266)

        button_btn = Button(self.window, text="Select a folder", font="algerian 18 bold", padx=5, pady=2,command=select_folder, borderwidth=5)
        button_btn.pack(side=BOTTOM, pady=50)


    def get_Path(self):
        return self.path_var

    def get_Data(self):
        return self.studentData

    def mainloop(self):
        self.window.mainloop()
