import wx
from config_window import MainFrame
from dataconfig_window import DataConfig
import wx.lib.agw.aquabutton as AB
import os
ID_NEW = 1
ID_RENAME = 2
ID_CLEAR = 3
ID_DELETE = 4
ID_CREATE = 5
ID_LOAD = 6
ID_EDIT = 7
ID_ADD = 8
ID_SHOW = 9
ID_DISPLAY = 10

class ListBox(wx.Frame):
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title, size=(670, 620))
        
        self.CreateStatusBar()
        self.SetStatusText("The Configurable Pipeline for the Analysis of Connectomes (C-PAC)")
    
        self.pipeline_map = {}
        self.sublist_map= {}
        
        mainPanel = wx.Panel(self)
        mainPanel.SetBackgroundColour('#FAF0E6')
        mainSizer = wx.BoxSizer(wx.VERTICAL)
        
        outerPanel1 = wx.Panel(mainPanel)
        outerSizer1 = wx.BoxSizer(wx.HORIZONTAL)
        
        outerPanel2 = wx.Panel(mainPanel)
        outerSizer2 = wx.BoxSizer(wx.HORIZONTAL)
        
        innerPanel1 = wx.Panel(outerPanel1)
        innerSizer1 = wx.BoxSizer(wx.HORIZONTAL)
         
        innerPanel2 = wx.Panel(outerPanel1, )
        innerSizer2 = wx.BoxSizer(wx.HORIZONTAL)
                
        lboxPanel1 = wx.Panel(innerPanel1)
        lboxSizer1 = wx.BoxSizer(wx.VERTICAL)
        btnPanel1 = wx.Panel(innerPanel1, -1)
        btnSizer1 = wx.BoxSizer(wx.VERTICAL)
        
        label = wx.StaticText(lboxPanel1, -1, "Pipelines")
        label.SetFont(wx.Font(16, wx.SWISS, wx.NORMAL, wx.BOLD))
        self.listbox = wx.CheckListBox(lboxPanel1, -1, size = (160,400))
        
        lboxSizer1.Add(label, 0, wx.ALIGN_CENTER)
        lboxSizer1.Add(self.listbox, 1, wx.EXPAND | wx.ALL, 10)
        lboxPanel1.SetSizer(lboxSizer1)
        
        new = wx.Button(btnPanel1, ID_NEW, 'New', size=(90, 30))
        ren = wx.Button(btnPanel1, ID_RENAME, 'Rename', size=(90, 30))
        dlt = wx.Button(btnPanel1, ID_DELETE, 'Delete', size=(90, 30))
        load = wx.Button(btnPanel1, ID_LOAD, 'Load', size=(90,30))
        edit = wx.Button(btnPanel1, ID_EDIT, 'Edit', size=(90,30))
        shw = wx.Button(btnPanel1, ID_DISPLAY, 'Show', size=(90,30))
        clr = wx.Button(btnPanel1, ID_CLEAR, 'Clear', size=(90, 30))
    
        self.Bind(wx.EVT_BUTTON, self.NewItem, id=ID_NEW)
        self.Bind(wx.EVT_BUTTON, self.OnRename, id=ID_RENAME)
        self.Bind(wx.EVT_BUTTON, self.OnDelete, id=ID_DELETE)
        self.Bind(wx.EVT_BUTTON, self.OnLoad, id=ID_LOAD)
        self.Bind(wx.EVT_BUTTON, self.OnEdit, id=ID_EDIT)
        self.Bind(wx.EVT_BUTTON, self.OnDisplay, id= ID_DISPLAY)
        self.Bind(wx.EVT_BUTTON, lambda event: self.OnClear(event, 1), id=ID_CLEAR)
        self.Bind(wx.EVT_LISTBOX_DCLICK, self.OnDisplay)        

        btnSizer1.Add((-1, 30))
        btnSizer1.Add(new)
        btnSizer1.Add(load, 0, wx.TOP, 5)
        btnSizer1.Add(edit, 0, wx.TOP, 5)
        btnSizer1.Add(shw, 0, wx.TOP, 5)
        btnSizer1.Add(ren, 0, wx.TOP, 5)
        btnSizer1.Add(dlt, 0, wx.TOP, 5)
        btnSizer1.Add(clr, 0, wx.TOP, 5)
        btnPanel1.SetSizer(btnSizer1)
                
        innerSizer1.Add(lboxPanel1, 1, wx.EXPAND | wx.ALL)
        innerSizer1.Add(btnPanel1, 1, wx.EXPAND | wx.ALL)
        
        innerPanel1.SetSizer(innerSizer1)
        
        lboxPanel2 = wx.Panel(innerPanel2)
        lboxSizer2 = wx.BoxSizer(wx.VERTICAL)
        btnPanel2 = wx.Panel(innerPanel2, -1)
        btnSizer2 = wx.BoxSizer(wx.VERTICAL)


        label2 = wx.StaticText(lboxPanel2, -1, "Subject Lists")
        label2.SetFont(wx.Font(16, wx.SWISS, wx.NORMAL, wx.BOLD))
        self.listbox2 = wx.CheckListBox(lboxPanel2, -1, size= (160,400)) 
        self.listbox2.Bind(wx.EVT_LISTBOX_DCLICK, self.OnShow)
        lboxSizer2.Add(label2, 0,wx.ALIGN_CENTER)
        lboxSizer2.Add(self.listbox2, 1, wx.EXPAND | wx.ALL, 10)
        lboxPanel2.SetSizer(lboxSizer2)
                
        create = wx.Button(btnPanel2, ID_CREATE, 'New', size=(90, 30))
        add = wx.Button(btnPanel2, ID_ADD, 'Add', size= (90,30))
        show = wx.Button(btnPanel2, ID_SHOW, 'Show', size= (90,30))
        clr2 = wx.Button(btnPanel2, ID_CLEAR, 'Clear', size=(90, 30))
        self.Bind(wx.EVT_BUTTON, self.CreateItem, id=ID_CREATE)
        self.Bind(wx.EVT_BUTTON, self.AddItem, id=ID_ADD)
        self.Bind(wx.EVT_BUTTON, self.OnShow, id= ID_SHOW)
        self.Bind(wx.EVT_BUTTON, lambda event: self.OnClear(event, 2), id=ID_CLEAR)
        btnSizer2.Add((-1, 30))
        btnSizer2.Add(create)
        btnSizer2.Add(add)
        btnSizer2.Add(show)
        btnSizer2.Add(clr2)
        btnPanel2.SetSizer(btnSizer2)
        
        
        innerSizer2.Add(lboxPanel2, 1, wx.EXPAND | wx.ALL)
        innerSizer2.Add(btnPanel2, 1, wx.EXPAND | wx.ALL)
        
        innerPanel2.SetSizer(innerSizer2)
        
        outerSizer1.Add(innerPanel1, 1, wx.EXPAND | wx.ALL)
        outerSizer1.Add(innerPanel2, 1, wx.EXPAND | wx.ALL)
        
        outerPanel1.SetSizer(outerSizer1)
        
        bmp = wx.Bitmap("images/cpac_logo2.jpg", wx.BITMAP_TYPE_ANY)
        self.runCPAC1 = AB.AquaButton(outerPanel2, bitmap = bmp, label="Run Individual Level Analysis")
        self.runCPAC1.SetFont(wx.Font(13, wx.SWISS, wx.ITALIC, wx.LIGHT))
        self.runCPAC1.Bind(wx.EVT_BUTTON, self.runIndividualAnalysis)
        
        self.runCPAC2 = AB.AquaButton(outerPanel2, bitmap = bmp, label ="Run Group Level Analysis")
        self.runCPAC2.SetFont(wx.Font(13, wx.SWISS, wx.ITALIC, wx.LIGHT))
        self.runCPAC2.Bind(wx.EVT_BUTTON, self.runGroupLevelAnalysis)
        
        outerSizer2.Add(self.runCPAC1, 1, wx.EXPAND | wx.RIGHT, 40)
        outerSizer2.Add(self.runCPAC2, 1, wx.EXPAND | wx.LEFT, 40)
        outerPanel2.SetSizer(outerSizer2)
        
        mainSizer.Add(outerPanel1, 1, wx.EXPAND | wx.ALL, 20)
        mainSizer.Add(wx.StaticLine(mainPanel), 0, wx.EXPAND|wx.TOP|wx.BOTTOM, 20)
        mainSizer.Add(outerPanel2, 0 ,wx.EXPAND | wx.ALL, 20)
        
        mainPanel.SetSizer(mainSizer)

        self.Centre()
        self.Show(True)

    def runIndividualAnalysis(self, event):

        try:
                if (self.listbox.GetChecked() or self.listbox.GetSelection()!= -1) and \
                    (self.listbox2.GetChecked() or self.listbox2.GetSelection()!= -1):
                    
                    pipelines = self.listbox.GetChecked()
                    sublists = self.listbox2.GetChecked()
                    
                    self.runCPAC1.SetPulseOnFocus(True)
                    
                    import CPAC
                    
                    for s in sublists:
                        sublist = self.sublist_map.get(s)
                        for p in pipelines:
                            pipeline = self.pipeline_map.get(p)
                            
                            CPAC.pipeline.cpac_runner.run(pipeline, sublist)
                            print "Pipeline %s successfully ran for subject list %s"%(p,s)
                    
                else:
                    print "no pipeline and subject list selected"
                    
        except ImportError, e:
                wx.MessageBox("Error importing CPAC. %s"%e, "Error") 
                print "Error importing CPAC"
                print e
        except Exception, e:
                print e
                wx.MessageBox(e, "Error") 
                
    def runGroupLevelAnalysis(self, event):
        print "running Group Analysis"

    def get_pipeline_map(self):
        return self.pipeline_map
    
    def get_sublist_map(self):
        return self.sublist_map
    
    def get_pipeline_path(self, id):
        path = self.pipeline_map.get(id)
        return path

    def NewItem(self, event):
        MainFrame(self, "save")

        
    def OnRename(self, event):
        sel = self.listbox.GetSelection()
        if sel!= -1:
            text = self.listbox.GetString(sel)
            renamed = wx.GetTextFromUser('Rename item', 'Rename dialog', text)
            if renamed != '':
                self.listbox.Delete(sel)
                self.listbox.Insert(renamed, sel)
                self.pipeline_map[renamed]= self.pipeline_map[text]
                del self.pipeline_map[text]


    def update_listbox(self, frame, pipeline_id, path):
        
        if self.pipeline_map.get(pipeline_id) == None:
                self.pipeline_map[pipeline_id] = path
                self.listbox.Append(pipeline_id)
                frame.close()
        else:
                dlg = wx.MessageDialog(self, 'Pipeline already exist',
                                   'Error!',
                               wx.OK | wx.ICON_ERROR)
                dlg.ShowModal()
                dlg.Destroy()
                
                
    def OnDelete(self, event):

        def removekey(d, key):
            r = dict(d)
            del r[key]
            return r

        selections = self.listbox.GetChecked()
        for sel in selections[::-1]:
            if sel != -1:
                text = self.listbox.GetString(sel)
                dlg = wx.MessageDialog(self, 'Do you also want to delete the configuration file from your system?',
                                       text, wx.YES | wx.NO | wx.ICON_INFORMATION)
    
                result = dlg.ShowModal()
                
                if  result == wx.ID_YES:
                    file_path = self.pipeline_map.get(text)
                
                    if file_path and os.path.exists(file_path):
                        os.remove(file_path)
                        
                self.listbox.Delete(sel)
                self.pipeline_map = removekey(self.pipeline_map, text)    
                
                dlg.Destroy()

        
    def OnEdit(self, event):
        
        sel = self.listbox.GetSelection()
        if sel != -1:
            text = self.listbox.GetString(sel)
            print "text--> ",text
            path = self.get_pipeline_path(text)
            if os.path.exists(path):
                MainFrame(self, option ="edit", path=path, pipeline_id = text)
            else:
                print "Couldn't find the config file %s "%path
     
    def OnLoad(self, event):
        
        dlg = wx.FileDialog(
            self, message="Choose the config yaml file",
                defaultDir=os.getcwd(), 
                defaultFile="",
                wildcard= "YAML files(*.yaml, *.yml)|*.yaml;*.yml",
                style=wx.OPEN | wx.CHANGE_DIR)
        
        if dlg.ShowModal() == wx.ID_OK:
            path = dlg.GetPath()
                
            if len(path)>0 and os.path.exists(path):
                MainFrame(self, option ="load", path=path)
            else:
                dlg = wx.MessageDialog(self, 'Invalid Path',
                                   'Error!',
                                   wx.OK | wx.ICON_ERROR)
                dlg.Destroy()
            
            dlg.Destroy()
                
                
    def OnClear(self, event, flag):
        if flag ==1:
            self.listbox.Clear()
            self.pipeline_map.clear()
        elif flag ==2:
            self.listbox2.Clear()
            self.sublist_map.clear()

    def CreateItem(self, event):
        DataConfig(self)


    def OnShow(self, event):
        import wx.lib.dialogs
        sel = self.listbox2.GetSelection()
        if sel != -1:
            text = self.listbox2.GetString(sel)
            name = self.sublist_map.get(text)
            if name:
                try:
                    f = open(name, "r")
                    msg = f.read()
                    f.close()
                    dlg = wx.lib.dialogs.ScrolledMessageDialog(self, msg, name, size = (800,800))
                    dlg.ShowModal()
                except:
                    print "Cannot open file %s"%(name)
                    
                    
    def OnDisplay(self, event):
        import wx.lib.dialogs
        sel = self.listbox.GetSelection()
        if sel != -1:
            text = self.listbox.GetString(sel)
            name = self.pipeline_map.get(text)
            if name:
                try:
                    f = open(name, "r")
                    msg = f.read()
                    f.close()
                    dlg = wx.lib.dialogs.ScrolledMessageDialog(self, msg, name, size = (800,1000))
                    dlg.ShowModal()
                except:
                    print "Cannot open file %s"%(name)
    
    
    def AddItem(self, event):
        
        dlg = wx.FileDialog(
            self, message="Choose the CPAC Subject list file",
            defaultDir=os.getcwd(), 
            defaultFile="CPAC_subject_list.yml",
            wildcard="YAML files(*.yaml, *.yml)|*.yaml;*.yml",
            style=wx.OPEN | wx.CHANGE_DIR)
        
        if dlg.ShowModal() == wx.ID_OK:
            path = dlg.GetPath()
            while True:
                dlg2 = wx.TextEntryDialog(self, 'Please enter a alias name for the Subject List',
                                     'Sublist Name', "CPAC_Sublist")
            
                if dlg2.ShowModal() == wx.ID_OK:
                    if len(dlg2.GetValue()) >0:
                        if self.sublist_map.get(dlg2.GetValue()) == None:
                            self.sublist_map[dlg2.GetValue()]= path
                            self.listbox2.Append(dlg2.GetValue())
                            dlg2.Destroy()
                            dlg.Destroy()
                            break
                        else:
                            dlg3 = wx.MessageDialog(self, 'Subject List with this name already exist','Error!',
                              wx.OK | wx.ICON_ERROR)
                            dlg3.ShowModal()
                            dlg3.Destroy()
                        
                    