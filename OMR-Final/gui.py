from tkinter import *
from tkinter import filedialog
from tkinter import ttk
import tkinter.messagebox
import time
from tkinter.font import Font


class gui:
    def __init__(self, window, title, background):
        self.window = Tk()
        self.background = background
        self.title = title
        self.window.title(f"{self.title}")
        self.window.resizable(0, 0)
        self.window.geometry('924x620')
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
        section_list_1_10 = ['A','B','C','D','E','F']
        section_list_11_Sci = ['A','B','C']
        section_list_12_Sci = ['A','B']
        section_list_11_Com = ['D','E','F']
        section_list_12_Com = ['D','E']
        section_list_11_Hum = ['G']
        section_list_12_Hum = ['F']
        exam_list = ["PA-1", "Term-1", "PA-2", "Term-2"]
        stream_list = ["Science", "Commerce", "Humanities"]
        subject_list_1_10 = ["English", "H,F,S", "Math", "Science", "Social Sci", "A.I"]
        subject_11_12_sci = ["English", "Physics", "Chemistry", "Math,Bio", "PE,CS"]
        subject_11_12_com = ["English", "Accounts", "BST", "Eco", "Math,PE,CS,EP"]
        subject_11_12_hum = ["English", "Pol Science", "Geo", "Psycho", "EP,Bio"]

        def select_folder():
            path = filedialog.askdirectory(initialdir="C:/Users", title="Select a folder...")  # Select a folder
            save_data()
            self.path_var = path
            time.sleep(1.5)
            tkinter.messagebox.showinfo("Folder selected", "Your folder has been uploaded successfully")
            self.window.destroy()

        def class_func():
            if int(class_list_box.get()) in range(1,11):
                section_list_box["state"] = "readonly"
                section_list_box["values"] = section_list_1_10
                ok_button_section["state"] = "active"
                subject_list_box["values"] = subject_list_1_10
            elif int(class_list_box.get()) == 11:
                stream_list_box["state"] = "readonly"
                ok_button_stream["state"] = "active"
            elif int(class_list_box.get()) == 12:
                stream_list_box["state"] = "readonly"
                ok_button_stream["state"] = "active"
            class_list_box["state"] = "disabled"
            ok_button_class["state"] = "disabled"

        def stream_func():
            if int(class_list_box.get()) == 11 :
                section_list_box["state"] = "readonly"
                if stream_list_box.get() == "Science":
                    section_list_box["values"] = section_list_11_Sci
                    subject_list_box["values"] = subject_11_12_sci
                elif stream_list_box.get() == "Commerce":
                    section_list_box["values"] = section_list_11_Com
                    subject_list_box["values"] = subject_11_12_com
                elif stream_list_box.get() == "Humanities":
                    section_list_box["values"] = section_list_11_Hum
                    subject_list_box["values"] = subject_11_12_hum
                    section_list_box.current(newindex=0)
                    section_list_box["state"] = "disabled"
                stream_list_box["state"] = "disabled"
                ok_button_stream["state"] = "disabled"
            elif int(class_list_box.get()) == 12:
                section_list_box["state"] = "readonly"
                if stream_list_box.get() == "Science":
                    section_list_box["values"] = section_list_12_Sci
                    subject_list_box["values"] = subject_11_12_sci
                elif stream_list_box.get() == "Commerce":
                    section_list_box["values"] = section_list_12_Com
                    subject_list_box["values"] = subject_11_12_com
                elif stream_list_box.get() == "Humanities":
                    section_list_box["values"] = section_list_12_Hum
                    subject_list_box["values"] = subject_11_12_hum
                    section_list_box.current(newindex=0)
                    section_list_box["state"] = "disabled"
                stream_list_box["state"] = "disabled"
                ok_button_stream["state"] = "disabled"
            ok_button_section["state"] = "active"

        def section_func():
            section_list_box["state"] = "disabled"
            ok_button_section["state"] = "disabled"
            exam_list_box["state"] = "readonly"
            ok_button_exam["state"] = "active"

        def subject_func():
            subject_list_box["state"] = "disabled"
            ok_button_subject["state"] = "disabled"

        def exam_func():
            subject_list_box["state"] = "readonly"
            ok_button_subject["state"] = "active"
            exam_list_box["state"] = "disabled"
            ok_button_exam["state"] = "disabled"

        class_label = Label(self.window, text="CLASS", font=Font(family="Hussar Ekologiczny", size=26), padx=15, bg=self.background)
        class_list_box = ttk.Combobox(self.window, values=class_list, state="readonly", width=4, font="arial 18 bold")
        class_label.place(x=65, y=69)
        class_list_box.place(x=97, y=130)

        ok_button_class = Button(self.window, text="OK", font="arial 14 bold", padx=7, pady=2, command=class_func)
        ok_button_class.place(x=105, y=180)

        stream_label = Label(self.window, text="Stream", font="algerian 26 ", padx=15, bg=self.background)
        stream_list_box = ttk.Combobox(self.window, values=stream_list, state="disabled", width = 11, font = "arial 18 bold")
        stream_label.place(x=350, y=66)
        stream_list_box.place(x=357, y=130)

        ok_button_stream = Button(self.window, text="OK", state="disabled", font="arial 14 bold", padx=7, pady=2, command=stream_func)
        ok_button_stream.place(x=405, y=180)

        section_label = Label(self.window, text="Section", font="algerian 26 ", bg=self.background)
        section_list_box = ttk.Combobox(self.window, state="disabled", width=3,font="arial 18 bold")
        section_label.place(x=685, y=66)
        section_list_box.place(x=720, y=130)

        ok_button_section = Button(self.window, text="OK", font="arial 14 bold", state="disabled", padx=7, pady=2, command=section_func)
        ok_button_section.place(x=722, y=180)

        subject_label = Label(self.window, text="Subject", font="algerian 26 ", bg=self.background)
        subject_list_box = ttk.Combobox(self.window, state="disabled", width=12,font="arial 18 bold")
        subject_label.place(x=190, y=300)
        subject_list_box.place(x=177, y=366)

        ok_button_subject = Button(self.window, text="OK", font="arial 14 bold", state="disabled", padx=7, pady=2, command=subject_func)
        ok_button_subject.place(x=232, y=420)

        exam_label = Label(self.window, text="Exams", font="algerian 26 ", bg=self.background)
        exam_list_box = ttk.Combobox(self.window, values=exam_list, state="disabled", width=8, font="arial 18 bold")
        exam_label.place(x=555, y=300)
        exam_list_box.place(x=555, y=366)

        ok_button_exam = Button(self.window, text="OK", font="arial 14 bold", state="disabled", padx=7, pady=2, command=exam_func)
        ok_button_exam.place(x=585, y=420)

        button_btn = Button(self.window, text="Select a folder", font="algerian 18 ", padx=5, pady=2,command=select_folder, borderwidth=5)
        button_btn.pack(side=BOTTOM, pady=40)


    def get_Path(self):
        return self.path_var

    def get_Data(self):
        return self.studentData

    def mainloop(self):
        self.window.mainloop()
