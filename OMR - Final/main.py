import os
import scanOMR


#{'class':'12', 'section':'A','exam':'PA-1'}

folder = "D:\\Daksh\\Python\\Optical Mark Recognition\\FinalOMR-main\\12-A"
files = os.listdir(folder)

for file in files:
    imgPath = f"{folder}\\{file}"
    img = scanOMR.read(imgPath)
    scanOMR.scan(img)
