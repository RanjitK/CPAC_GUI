import wx
from generic_class import GenericClass
from ..utils import control, dtype
import os

ID_RUN_EXT = 11
ID_RUN_MEXT = 12

class DataConfig(wx.Frame):
    
    
    def __init__(self, parent):

        wx.Frame.__init__(self, parent, title="Data Configuration", size = (800,450))
        
        mainSizer = wx.BoxSizer(wx.VERTICAL)
        
        self.panel = wx.Panel(self)
        
        self.window = wx.ScrolledWindow(self.panel)
        
        self.page = GenericClass(self.window, "Data Setup Configuration")
        
        self.page.add(label="Subject to Include", 
                 control=control.COMBO_BOX, 
                 name = "subjectList", 
                 type = dtype.COMBO, 
                 comment = "List of subjects that are included, can be a text file or a list.\n"\
                            "If None, extract data runs on all the subjects.\n"\
                            "Example1:- /home/data/settings/include_subjects.txt\n"\
                            "Example2:- sub001, sub003", 
                 values = "None")
        
        self.page.add(label="Subject to Exclude", 
                 control=control.COMBO_BOX, 
                 name = "exclusionSubjectList", 
                 type = dtype.COMBO, 
                 comment = "List of subjects that are to be excluded, can be a text file or a list.\n"\
                            "Example1:- /home/data/settings/ex_subjects.txt\n"\
                            "Example2:- sub001, sub003", 
                 values = "None")
        
        self.page.add(label= "Anatomical Template",
                 control = control.TEXT_BOX,
                 name = "anatomicalTemplate",
                 type = dtype.STR,
                 comment = "Path structure to extract anatomical files.\nPut %s where site and subjects are in the path.\n"\
                            "Example 1:- /home/data/Incoming/cambridge_fcon/%s/%s/*/mprage_anonymized.nii.gz\n"\
                            "Example 2:- /home/data/sites/%s/%s/session_1/*/mprage.nii.gz",
                 values ="",
                 style= wx.EXPAND | wx.ALL,
                 size = (532,-1))
        
        self.page.add(label= "Functional Template",
                 control = control.TEXT_BOX,
                 name = "functionalTemplate",
                 type = dtype.STR,
                 comment = "Path structure to extract anatomical files.\nPut %s where site and subjects are in the path.\n"\
                            "Example 1:- /home/data/Incoming/cambridge_fcon/%s/%s/*/rest.nii.gz\n"\
                            "Example 2:- /home/data/sites/%s/%s/session_1/*/rest.nii.gz",
                 values ="",
                 style= wx.EXPAND | wx.ALL,
                 size = (532,-1))
        
        self.page.add(label= "List of Sites",
                 control = control.TEXT_BOX,
                 name = "siteList",
                 type = dtype.STR,
                 comment = "list of sites, can be a text file or a list.\n"\
                            "If None, extract data runs on all sites\n"\
                            "Example:- ABIDE, ADHD-200",
                 values ="None",
                 style= wx.EXPAND | wx.ALL,
                 size = (532,-1))
        
        self.page.add(label="Scan Parameters CSV file", 
                 control=control.COMBO_BOX, 
                 name = "scanParametersCSV", 
                 type = dtype.COMBO, 
                 comment = "Scan Parameters csv file path. This file is mandatory for slice timing correction.\n"\
                           "please use the right format for the csv, refer to http://fcp-indi.github.io/docs/user/slice.html.\n"\
                           "If None, CPAC does not do slice timing correction",
                 values = "None")
        
        self.page.add(label = "Output SubList Directory", 
                      control = control.DIR_COMBO_BOX, 
                      name = "outputSubjectListLocation", 
                      type = dtype.STR, 
                      comment = "Output Directory Location of CPAC Subject List file",
                      values = os.getcwd())
        self.page.set_sizer()
         
        mainSizer.Add(self.window, 1, wx.EXPAND)
        
        btnPanel = wx.Panel(self.panel, -1)
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        
        save = wx.Button(btnPanel, wx.ID_SAVE, "SAVE", (280,10), wx.DefaultSize, 0 )
        self.Bind(wx.EVT_BUTTON, self.save, id=wx.ID_SAVE)
        hbox.Add(save, 0.6, wx.ALIGN_RIGHT|wx.ALL, 5)
    
        run_ext = wx.Button(btnPanel, ID_RUN_EXT, "CREATE SUBLIST", (280,10), wx.DefaultSize, 0 )
        self.Bind(wx.EVT_BUTTON, self.run_extract_data, id=ID_RUN_EXT)
        hbox.Add( run_ext, 0.6, wx.ALIGN_RIGHT|wx.ALL, 5)
        
        #run_mext = wx.Button(btnPanel, ID_RUN_MEXT, "RUN MultiScanExtractData", (280,10), wx.DefaultSize, 0 )
        #self.Bind(wx.EVT_BUTTON, self.run_extract_data, id=ID_RUN_MEXT)
        #hbox.Add( run_mext, 0.6, wx.ALIGN_RIGHT|wx.ALL, 5)
        
        cancel = wx.Button(btnPanel, wx.ID_CANCEL, "CLOSE",(220,10), wx.DefaultSize, 0 )
        self.Bind(wx.EVT_BUTTON, self.cancel, id=wx.ID_CANCEL)
        hbox.Add( cancel, 0.6, wx.ALIGN_RIGHT|wx.ALL, 5)
        btnPanel.SetSizer(hbox)
        
        mainSizer.Add(btnPanel, 0.5, wx.EXPAND | wx.RIGHT, 20)
        
        self.panel.SetSizer(mainSizer)
        
        self.Show()
        
    def cancel(self, event):
        self.Close()
        
    def run_extract_data(self, event):
        import os
        import yaml
        dlg = wx.FileDialog(
            self, message="Choose the data configuration file",
            defaultDir=os.getcwd(), 
            defaultFile="data_config.yaml",
            wildcard="YAML files(*.yaml, *.yml)|*.yaml;*.yml",
            style=wx.OPEN | wx.CHANGE_DIR)
        
        if dlg.ShowModal() == wx.ID_OK:
            path = dlg.GetPath()
            
            try:  
                config_map = yaml.load(open(path, 'r'))
                out_location = os.path.join(\
                               os.path.realpath(config_map.get('outputSubjectListLocation')),\
                               'CPAC_subject_list.yml')
                os.system("python extract_data.py " + path)    
                while True:
                    
                    dlg2 = wx.TextEntryDialog(self, 'Please enter a name for the Subject List',
                                                     'Sublist Name', "CPAC_Sublist")
                    if dlg2.ShowModal() == wx.ID_OK:
                        if len(dlg2.GetValue()) >0:
                            parent = self.Parent
                            map = parent.get_sublist_map()
                            if map.get(dlg2.GetValue()) == None:
                                map[dlg2.GetValue()]= out_location
                                parent.listbox2.Append(dlg2.GetValue())
                                dlg2.Destroy()
                                dlg.Destroy()
                                break
                            else:
                                dlg3 = wx.MessageDialog(self, 'Subject List with this name already exist','Error!',
                                                        wx.OK | wx.ICON_ERROR)
                                dlg3.ShowModal()
                                dlg3.Destroy()
            
        
            except Exception:
                dlg2 = wx.MessageDialog(self, "Error Creating CPAC Subject List.",
                                   'Error!',
                               wx.OK | wx.ICON_ERROR)
                dlg2.ShowModal()
                dlg2.Destroy()
         
         
    def save(self, event):
        
        config_list =[]
        def display(win, msg):
            wx.MessageBox(msg, "Error")
            win.SetBackgroundColour("pink")
            win.SetFocus()
            win.Refresh()
        
        for ctrl in self.page.get_ctrl_list():
            print "validating ctrl-->", ctrl.get_name()
            win = ctrl.get_ctrl()
            print "ctrl.get_selection()", ctrl.get_selection()
            print "type(ctrl.get_selection())", type(ctrl.get_selection())
                    
            value = str(ctrl.get_selection())
            name = ctrl.get_name()
            dtype= ctrl.get_datatype()
                  
            if len(value) == 0:
                display(win,"%s field must contain some text!"%ctrl.get_name())
                return
                        
            if 'Template' in name:
                if value.count('%s') != 2:
                    display(win,"Incorrect template, two \'%s\' values are required. One for site and another for"\
                            " subject location in the path. Please refere to example!")
                    return
            
            if '/' in value and 'Template' not in name:
                if not os.path.exists(ctrl.get_selection()):
                    display(win,"%s field contains incorrect path. Please update the path!"%ctrl.get_name())
                    return
                
            if value.startswith('%s'):
                display(win, "Template cannot start with %s")
                return
            config_list.append((name, value, dtype))
                
        
        dlg = wx.FileDialog(
            self, message="Save file as ...", 
            defaultDir=os.getcwd(), 
            defaultFile="data_config.yaml", 
            wildcard="YAML files(*.yaml, *.yml)|*.yaml;*.yml", 
            style=wx.SAVE)
        
        if dlg.ShowModal() == wx.ID_OK:
            path = dlg.GetPath()
        
            f = open(path, 'w')
            for ctrl in config_list:
    
                if "/" in ctrl[1] or "%s" in ctrl[1] or 'None' in ctrl[1]: 
                    value = ctrl[1]
                else:
                    value =[val.strip() for val in ctrl[1].split(',')]
                
                print name, ":", value, "\n"
                print >>f, ctrl[0], " : ", value, "\n"
            
            f.close()
            
            print "saving %s"%path

            
        dlg.Destroy()
        
#app = wx.App()
#DataConfig(None).Show()
#app.MainLoop()