from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter.messagebox import showerror
import os
file_to_print = ''
def print_any_file(file=None):
    if os.path.exists(file):
        try:
            os.startfile(file, "print")
            l1.config(text='')
        except Exception as e:
            showerror('Error',message='printing Error',detail=e)
    else:
        showerror('Printing Error',message='Please Select a file to print.')
        
def selectfile():
    global file_to_print
    file= askopenfilename(filetypes =[('Text Files', '*.txt')])
    if file:
        file_to_print=file
        l1.config(text=file)
root = Tk()
root.title('Simple print Example')
l = Label(text='Select ur desired file to print',bg='gray')
l.pack(fill=X)
btn_select = Button(text='Select File',width=15,bg='dark green',command=selectfile).pack()
l1 = Label(text='')
l1.pack(fill=X)


btn = Button(root,text='Print',width=15,command=lambda:print_any_file(file_to_print)).pack()
root.mainloop()
