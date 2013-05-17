import wx
from GUI.windows.firstWindow import ListBox


app = wx.App()
ListBox(None, -1, 'Configure & Run CPAC')
app.MainLoop()