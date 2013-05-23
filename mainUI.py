#!/usr/bin/env python

import wx
from gui.windows.main_window import ListBox


app = wx.App()
ListBox(None, -1, 'Configure & Run CPAC')
app.MainLoop()