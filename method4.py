# Import the required libraries
from tkinter import *
import pyautogui
from PIL import ImageTk, Image
import time
import win32api,win32print
import tempfile
# Create an instance of tknter frame or window
win = Tk()

# Set the size of the window
win.geometry("700x350")


# Define a function to take the screenshot
def printImage(img):
    filename = tempfile.mktemp(".png")
    img.save(filename)
    win32api.ShellExecute(
        0,
        "printto",
        filename,
        '"%s"' % win32print.GetDefaultPrinter(),
        ".",
        0
    )
def take_screenshot():
   x = 0
   y = 0
   a= win.geometry()
   a = a.split('+')
   x = int(a[1])
   y = int(a[-1])
   w = a[0].split('x')[0]
   h = a[0].split('x')[-1]
   print(x,y,w,h)
   # Take the screenshot in the given corrds
   time.sleep(1)
   capImg = pyautogui.screenshot(region=(x, y, w, h))
   
   printImage(capImg)#if you want to print directly
##   
##   # Create a toplevel window
##   top = Toplevel(win)
##   im1 = ImageTk.PhotoImage(capImg)
##
##   # Add the image in the label widget
##   image1 = Label(top, image=im1)
####   image1.image = im1
##   image1.pack(fill=BOTH)
##   btn = Button(top,text='Print',width=15,bg='green',command=lambda:printImage(capImg)).pack(pady=5)
##   top.mainloop()

Button(win, text='Take ScreenShot', command=take_screenshot).pack(padx=10, pady=10)

win.mainloop()
