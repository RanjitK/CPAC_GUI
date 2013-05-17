import wx
import wx.combo
import os
from wx.lib.masked import NumCtrl

class FileSelectorCombo(wx.combo.ComboCtrl):
    def __init__(self, *args, **kw):
        wx.combo.ComboCtrl.__init__(self, *args, **kw)
        bmp = wx.BitmapFromImage(wx.Image('images/folder3.gif'))
        self.SetButtonBitmaps(bmp, False)
        
    # Overridden from ComboCtrl, called when the combo button is clicked
    def OnButtonClick(self):
        path = ""
        name = ""
        wildcard = "CPAC files (*.gz,*.nii,*.txt,*.mat.*.cnf,*.sch)|*gz;*.nii;*.txt;*.cnf;*.sch;*.mat"
        if self.GetValue():
            path, name = os.path.split(self.GetValue())
        
        dlg = wx.FileDialog(self, "Choose File", path, name,
                           wildcard= wildcard, style=wx.FD_OPEN|wx.CHANGE_DIR)
        try:
            if dlg.ShowModal() == wx.ID_OK:
                self.SetValue(dlg.GetPath())
                self.GetTextCtrl().SetValue(dlg.GetPath())
                dlg.Destroy()
        except:
            pass
        
        self.SetFocus()


class DirSelectorCombo(wx.combo.ComboCtrl):
    
    def __init__(self, *args, **kw):
        wx.combo.ComboCtrl.__init__(self, *args, **kw)
        bmp = wx.BitmapFromImage(wx.Image('images/folder7.gif'))
        self.SetButtonBitmaps(bmp, False)
        
    # Overridden from ComboCtrl, called when the combo button is clicked
    def OnButtonClick(self):
        import os
        
        dlg = wx.DirDialog(self, "Choose a directory:",
                                style= wx.DD_NEW_DIR_BUTTON,
                          defaultPath=os.getcwd())

        try:
            if dlg.ShowModal() == wx.ID_OK:
                self.SetValue(dlg.GetPath())
                self.GetTextCtrl().SetValue(dlg.GetPath())
                dlg.Destroy()
        except:
            pass
        
        
        self.SetFocus()
        
class CheckBox(wx.Frame):
    
    def __init__(self, parent, values):
        wx.Frame.__init__(self, parent, title="Select Corrections", size = (200,230))
        sizer = wx.BoxSizer(wx.VERTICAL)
        
        panel = wx.Panel(self)
        self.ctrl = wx.CheckListBox(panel, id = wx.ID_ANY,
                                    choices = values)
        button = wx.Button(panel, -1, 'OK', size= (90,30))
        button.Bind(wx.EVT_BUTTON, self.onButtonClick)
        sizer.Add(self.ctrl, 1, wx.EXPAND | wx.ALL, 10)
        sizer.Add(button,0, wx.ALIGN_CENTER)
        panel.SetSizer(sizer)
        
        self.Show()
    
    def onButtonClick(self,event):
        parent = self.Parent
        if self.ctrl.GetCheckedStrings():
            val=""
            for sel in self.ctrl.GetCheckedStrings():
                if val:
                    val = val+ "," + sel
                else:
                    val = sel
            parent.listbox.Append(val)
            self.Close()
        
class CheckListBoxCombo(wx.Panel):
    
    def __init__(self, parent, size, validator, style,values):
        wx.Panel.__init__(self, parent)
        
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.values = values
        self.listbox = wx.CheckListBox(self, id = wx.ID_ANY, size = (300,120))
        bmp = wx.Bitmap("images/plus12.jpg", wx.BITMAP_TYPE_ANY)
        self.button = wx.BitmapButton(self, -1, bmp, size= (30,30))
        self.button.Bind(wx.EVT_BUTTON, self.onButtonClick)
        sizer.Add(self.listbox,wx.EXPAND | wx.ALL, 10)
        sizer.Add(self.button)
        self.SetSizer(sizer)
        
    def onButtonClick(self, event):
        CheckBox(self, self.values)
        
    def GetListBoxCtrl(self):
        return self.listbox
    


class TextBoxFrame(wx.Frame):

    def __init__(self, parent, values):
        wx.Frame.__init__(self, parent, title="Enter BandPass Frequency", size = (300,140))
        
        panel = wx.Panel(self)
        
        sizer = wx.BoxSizer(wx.VERTICAL)
        
        flexsizer = wx.FlexGridSizer(cols=2, hgap=10, vgap=15) 
        
        label1 = wx.StaticText(panel, -1, label = 'Band Pass Filter Lower Bound')
        self.box1 = NumCtrl(panel, id = wx.ID_ANY, value= values[0],
                            integerWidth=2, fractionWidth = 3, 
                            allowNegative=False, allowNone = True)
        
    
        flexsizer.Add(label1)
        flexsizer.Add(self.box1,0,wx.ALIGN_RIGHT, 5)
        
        label2 = wx.StaticText(panel, -1, label = 'Band Pass Filter Upper Bound')
        self.box2 = NumCtrl(panel, id = wx.ID_ANY, value= values[1],
                            integerWidth=2, fractionWidth = 3, 
                            allowNegative=False, allowNone = True)
        
        flexsizer.Add(label2, 0, wx.EXPAND, 2)
        flexsizer.Add(self.box2,0, wx.ALIGN_RIGHT, 5)
        
        button = wx.Button(panel, -1, 'OK', size= (90,30))
        button.Bind(wx.EVT_BUTTON, self.onButtonClick)
        sizer.Add(flexsizer, 1, wx.EXPAND | wx.ALL, 10)
        sizer.Add(button,0, wx.ALIGN_CENTER)
        panel.SetSizer(sizer)
        
        self.Show()
    
    def onButtonClick(self,event):
        parent = self.Parent
        
        if self.box1.GetValue() and self.box2.GetValue():
            
            if self.box1.GetValue() >= self.box2.GetValue():
                dlg = wx.MessageDialog(self, 'Lower Bound should be less than Upper Bound',
                                       'Error!',
                                   wx.OK | wx.ICON_ERROR)
                dlg.ShowModal()
                dlg.Destroy()
            else:
                val = [self.box1.GetValue() , self.box2.GetValue()]
                parent.listbox.Append(str(val))
                self.Close()
                          

class TextListBoxCombo(wx.Panel):
    
    def __init__(self, parent, size, validator, style,values):
        wx.Panel.__init__(self, parent)
        
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.values = values
        self.listbox = wx.CheckListBox(self, id = wx.ID_ANY, size = (200,100))
        bmp = wx.Bitmap("images/plus12.jpg", wx.BITMAP_TYPE_ANY)
        self.button = wx.BitmapButton(self, -1, bmp, size= (25,25))
        self.button.Bind(wx.EVT_BUTTON, self.onButtonClick)
        sizer.Add(self.listbox,wx.EXPAND | wx.ALL, 10)
        sizer.Add(self.button)
        self.SetSizer(sizer)
        
    def onButtonClick(self, event):
        TextBoxFrame(self, self.values)
        
    def GetListBoxCtrl(self):
        return self.listbox