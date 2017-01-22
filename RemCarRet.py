# Author simottar@gmail.com
# Removes carriage return and extra whitespace from a file and copies it into the clipboard
# takes in the name of the file as parameter. E.g. RemCarRet.py asdf.txt
import os
import sys
fileName = sys.argv[1]
readFile = open(os.path.join(os.getcwd(),fileName))
clipboardVal = ' '.join((readFile.read().replace('\n', ' ')).split())

import tkinter
r = tkinter.Tk()
r.withdraw()
r.clipboard_clear()
r.clipboard_append(clipboardVal)
r.mainloop()
r.quit()