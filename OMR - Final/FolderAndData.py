from gui import gui

# Create GUI Window
object = gui(object, background='#a3c3ff', title="GUI")
object.create_window()
object.mainloop()

folder = object.get_Path()
data = object.get_Data()
print(f"Data : {data}\nFolder : {folder}")




