
# Import Required Library
from tkinter import *
import win32api
from tkinter import filedialog
from pyautogui import alert
  
# Create Tkinter Object
root = Tk()
  
# Set Title and geometry
root.title('Print Hard Copies')
root.geometry("200x200")
  
# Print File Function
def print_file():
    
    # Ask for file (Which you want to print)
    file_to_print = filedialog.askopenfilename(
      initialdir="/", title="Select file", 
      filetypes=(("Text files", "*.txt"), ("all files", "*.*")))
      
    if file_to_print:
        
        # Print Hard Copy of File
        win32api.ShellExecute(0,              # NULL since it's not associated with a window
             "print",        # execute the "print" verb defined for the file type
             file_to_print,  # path to the document file to print
             None,           #no parameters, since the target is a document file
             ".",            #current directory, same as NULL here
             0)              # SW_HIDE passed to app associated with the file type                   
    alert(text="Print Successful",title="Success",button='ok',root=root)
# Make Button
Button(root, text="Print FIle", command=print_file).pack()
  
# Execute Tkinter
root.mainloop()
