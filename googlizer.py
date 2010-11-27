#Windows Googlizer Clone
#Written by Giorgio F. Gilestro
#giorgio@gilestro.tk

import win32clipboard as w
import win32con
import webbrowser


try:
    w.OpenClipboard()
    tq=w.GetClipboardData(win32con.CF_TEXT)
    w.CloseClipboard()
    webbrowser.open("http://www.google.com/search?q=%s" % tq)
except:
    pass



