from selenium import webdriver
import pyautogui
import tkinter as tk
from tkinter import filedialog, Text
import os
import time

#chrome driver
exec_path = r"C:\Users\JoshAlder\OneDrive - Principle One\Documents\VS Code\URLs Project\chromedriver.exe"
driver = webdriver.Chrome(executable_path=exec_path)
driver.set_page_load_timeout(30) #after 30 secs - time out    
driver.maximize_window()

canvascol = '#316879'
framecol = '#7fe7dc'
txtcol = '#ced7d8'
lblcol = '#f47a60'

# root, canvas + frame
root = tk.Tk() 
canvas = tk.Canvas(root, height=500, width=500, bg=canvascol)
canvas.pack()
frame = tk.Frame(root, bg=framecol)
frame.place(relwidth=0.8,relheight=0.4,relx=0.1,rely=0.1)

# button to import URL text file:
files = [] # appending array because i dont know how to set variables which can be called outside of the function
def getFile():
    # for widget in frame.winfo_children(): # delete label when user goes to select new file 
    #     widget.destroy()
    urlTxtFile = filedialog.askopenfilename(initialdir='/', title='Select File',
                                          filetypes = (('text files', '*.txt'),
                                          ('All files', '*.*')))
    label = tk.Label(frame, text=urlTxtFile, bg=lblcol)
    if not urlTxtFile == '': # add label to root if a file is selected
            label.pack()
    getFile.file = urlTxtFile # this doesn't do anything but the app seems to crash more if i delete it... maybe im just mental
    files.append(urlTxtFile)

openFile = tk.Button(root, text = 'Import URLs', padx=10,
                     pady=5, fg=txtcol, bg=canvascol, command=getFile)
openFile.pack()


# button to choose destination folder
folders = []
def getFolder():
    # for widget in frame.winfo_children(): 
    #     widget.destroy()
    destFolder = filedialog.askdirectory()
    label = tk.Label(frame, text=destFolder, bg=lblcol)
    if not destFolder == '':
            label.pack()
    getFolder.folder = destFolder
    folders.append(destFolder)

chooseFolder = tk.Button(root, text = 'Choose Destination', padx=10,
                     pady=5, fg=txtcol, bg=canvascol,command=getFolder)
chooseFolder.pack()


# Temi's screenshot function with folder as param
def screenshot(d,folder):
    time_string = time.asctime().replace(":", " ")
    file_name = folder + time_string + ".png"
    d.save_screenshot(file_name)

# Temi's processURLs function modified to open file + folder as param
def processURLs(txtfile,folder):
    if not txtfile or txtfile == '':
        print('select file')
    else:
        file = open(txtfile,"r")
        for x in file: #go through each url in the txt file
            try:
                driver.get(x)
            except:
                print((x) + 'took too long - time out') #if browser takes too long, print error message
            else:
                screenshot(driver,folder)

getScreenshots = tk.Button(root, text = 'Run Application', padx=10,
                     pady=5, fg=txtcol, bg=canvascol, command=lambda: processURLs(files[0],folders[0]))
getScreenshots.pack()

# run app
root.mainloop()