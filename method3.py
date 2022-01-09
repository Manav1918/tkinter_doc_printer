from tkinter import *
from tkinter import ttk
import win32api
import win32print
import tempfile
from tkinter.messagebox import showinfo

def installed_printer():
    printers = win32print.EnumPrinters(2)
    for p in printers:
        return(p)

printerdef = ''

def locprinter():
    pt = Toplevel()
##    pt.geometry("250x250")
    pt.title("choose printer")
    var1 = StringVar()
    LABEL = Label(pt, text="Select Printer",bg='goldenrod2',fg='black').pack(fill=X)
    PRCOMBO = ttk.Combobox(pt, width=35)
    print_list = []
    printers = list(win32print.EnumPrinters(2))
    for i in printers:
        print_list.append(i[2])
    print(print_list)
    # Put printers in combobox
    PRCOMBO['values'] = print_list
    defprinter= win32print.GetDefaultPrinter()
    print('Default selected Printer:',defprinter)
    PRCOMBO.set(defprinter)
    PRCOMBO.pack(padx=5,pady=5)
    
    def select():
        global printerdef
        printerdef = PRCOMBO.get()
        pt.destroy()
        print_in_default_printer()
    BUTTON = ttk.Button(pt, text="Print",width=30,command=select).pack(pady=10)

root = Tk()
root.title("printer selection in tkinter")
root.geometry("400x400")


menubar = Menu(root)
root.config(menu=menubar)

file_menu = Menu(menubar,tearoff=0)
menubar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="print", command=locprinter)


LAB = Label(root, text="Write Something Here")
T2 = Text(root, width=40, height=10, wrap=WORD)
LAB.pack()
T2.pack(fill=BOTH,padx=5,pady=5)

def print_in_default_printer():
    printText = T2.get("1.0", END)
    print(printText)
    print(printerdef)
    
    win32print.SetDefaultPrinter(printerdef)
    filename = tempfile.mktemp(".txt")
    open(filename, "w").write(printText)
    # Bellow is call to print text from T2 textbox
    win32api.ShellExecute(
        0,
        "printto",
        filename,
        '"%s"' % win32print.GetDefaultPrinter(),
        ".",
        0
    )
    showinfo(title='Success',message='Print Successful',detail='Printing is done . thank You!')

root.mainloop()
