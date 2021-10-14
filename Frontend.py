#STYLING CODE
import tkinter as tk
from tkinter import StringVar, filedialog
from tkinter.filedialog import askopenfilename, test, askdirectory

#import other files
#from selenium import webdriver
import Screenshots as S
import ScreenshotFunctions as F

#define root. Root holds structure of app
root = tk.Tk()

#specify canvas size to make GUI bigger
canvas = tk.Canvas(root, height=700, width=700, bg="#d1d1e0")
#attach canvas to root
canvas.pack()

#Add heading text to GUI
headingText = tk.Label(root, text="Digital Forensics Unit URL Processing Tool", bg="#d1d1e0", font=("Calibri", 15, 'bold'))
headingText.pack()

#Description text
descriptionText = tk.Label(root, text="Click on the button below to attach your text file \nand process the URLs", bg="#d1d1e0", font=("Calibri", 13,), anchor='center')

#button - upload txt file
upload_btn = tk.Button(root,text = "Upload Your File", command=F.upload_file, padx = 10, pady = 5, fg="black", bg="#ffffff")
upload_btn.pack()

#button - choose folder to save screenshots to
choose_folder_btn  = tk.Button(root,text = "Choose Folder to Save Images", command=F.choose_folder, padx = 10, pady = 5, fg="black", bg="#ffffff")
choose_folder_btn.pack()

#button - screenshot
shot_btn = tk.Button(root,text = "Screenshot URLs", command=F.snap, padx = 10, pady = 5, fg="black", bg="#ffffff")
shot_btn.pack()

# place the button on the window
headingText.place(x=180, y=250)
descriptionText.place(x=180, y=300)
upload_btn.place(x=300, y=400)
choose_folder_btn.place(x=265, y=450)
shot_btn.place(x=300, y=500)

#run GUI
root.mainloop()

