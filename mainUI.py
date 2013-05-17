import wx
from gui.windows.firstWindow import ListBox


app = wx.App()
ListBox(None, -1, 'Configure & Run CPAC')
app.MainLoop()