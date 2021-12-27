from shutil import move
import tkinter as tk
import fileMover
import time

root= tk.Tk()

canvas1 = tk.Canvas(root, width = 300, height = 300)
canvas1.pack()

def moveFiles ():
    fileMover.copyPastaFiles()  
    label1 = tk.Label(root, text= 'Files Moved!', fg='green', font=('helvetica', 12, 'bold'))
    canvas1.create_window(150, 200, window=label1)
    
button1 = tk.Button(text='Move Files',command=moveFiles, bg='green',fg='white')
canvas1.create_window(150, 150, window=button1)
closeBtn = tk.Button(text='Close',command=root.destroy, bg='brown',fg='white')
canvas1.create_window(280, 285, window=closeBtn)

root.mainloop()
input('Press <Enter> to end the program')