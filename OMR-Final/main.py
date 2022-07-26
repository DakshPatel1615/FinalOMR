import os
import random
from gui import gui
import saveData
from scanOMR import read, scan

# Create GUI Window
rainbow = ['#FF8FB1', '#76BA99', '#81CACF', '#395B64', '#FFDEB4', '#CEE5D0', '#3AB4F2', '#7A86B6', '#FBB454', '#54BAB9',
           '#F2D1D1', "#CDF0EA"]
object = gui(object, background=random.choice(rainbow), title="GUI")
object.create_window()
object.mainloop()

folder = object.get_Path()
data = object.get_Data()

className = data['class'] + data['section']
classFile = className + ".xlsx"
exam = data['exam']
stream = data['stream']
subject = data['subject']

# SCANNING AND SAVING

resultPath = r"D:\Daksh\Python\Optical Mark Recognition\FinalOMR-main\OMR-Final\Results"
resultPath = os.path.join(resultPath, className)
if os.path.isdir(resultPath):
    pass
else:
    os.mkdir(resultPath)

fileList = os.listdir(resultPath)

savePath = resultPath + '\\' + classFile

wb = saveData.getWorkbook(classFile, fileList, savePath)
ws = saveData.getWorksheet(exam, wb)

files = os.listdir(folder)
for file in files:
    filename = os.path.join(folder, file)
    img = read(filename)
    storeImgExam = os.path.join(resultPath, exam)
    if os.path.isdir(storeImgExam):
        pass
    else:
        os.mkdir(storeImgExam)
    saveImgPath = os.path.join(storeImgExam, file)
    score, percentage = scan(img, saveImgPath)
    name = (file[:-4])
    saveData.addStudentRecord(ws, name, className, stream, subject, score, percentage)

wb.save(savePath)
