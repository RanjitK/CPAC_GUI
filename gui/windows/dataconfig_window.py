import wx
from ..utils.generic_class import GenericClass
from ..utils.constants import control, dtype
import os

ID_RUN_EXT = 11
ID_RUN_MEXT = 12

class DataConfig(wx.Frame):
    
    
    def __init__(self, parent):

        wx.Frame.__init__(self, parent, title="CPAC - Subject List Setup", size = (800,450))
        
        mainSizer = wx.BoxSizer(wx.VERTICAL)
        
        self.panel = wx.Panel(self)
        
        self.window = wx.ScrolledWindow(self.panel)
        
        self.page = GenericClass(self.window, "Subject List Setup")
        
        self.page.add(label= "Anatomical File Path Template ",
                 control = control.TEXT_BOX,
                 name = "anatomicalTemplate",
                 type = dtype.STR,
                 comment = "File Path Template for Anatomical Files\n\n"
                           "Replace the site- and subject-level directories with %s.\n\n"
                           "See User Guide for more detailed instructions.",
                 values ="",
                 style= wx.EXPAND | wx.ALL,
                 size = (532,-1))
        
        self.page.add(label= "Functional File Path Template ",
                 control = control.TEXT_BOX,
                 name = "functionalTemplate",
                 type = dtype.STR,
                 comment = "File Path Template for Functional Files\n\n"
                           "Replace the site- and subject-level directories with %s.\n\n"
                           "See User Guide for more detailed instructions.",
                 values ="",
                 style= wx.EXPAND | wx.ALL,
                 size = (532,-1))

        self.page.add(label="Subjects to Include (Optional) ", 
                 control=control.COMBO_BOX, 
                 name = "subjectList", 
                 type = dtype.COMBO, 
                 comment = "Include only a sub-set of the subjects present in the folders defined above.\n\n"
                           "List subjects in this box (e.g., sub101, sub102) or provide the path to a\n"
                           "text file with one subject on each line.\n\n"
                           "If 'None' is specified, CPAC will include all subjects.", 
                 values = "None")
        
        self.page.add(label="Subject to Exclude (Optional) ", 
                 control=control.COMBO_BOX, 
                 name = "exclusionSubjectList", 
                 type = dtype.COMBO, 
                 comment = "Exclude a sub-set of the subjects present in the folders defined above.\n\n"
                           "List subjects in this box (e.g., sub101, sub102) or provide the path to a\n"
                           "text file with one subject on each line.\n\n"
                           "If 'None' is specified, CPAC will not exclude any subjects.", 
                 values = "None")
        
        self.page.add(label= "Sites to Include (Optional) ",
                 control = control.TEXT_BOX,
                 name = "siteList",
                 type = dtype.STR,
                 comment = "Include only a sub-set of the sites present in the folders defined above.\n\n"
                           "List sites in this box (e.g., NYU, UCLA) or provide the path to a text\n"
                           "file with one site on each line.\n\n"
                           "If 'None' is specified, CPAC will include all sites.",
                 values ="None",
                 style= wx.EXPAND | wx.ALL,
                 size = (532,-1))
        
        self.page.add(label="Scan Parameters File (Optional) ", 
                 control=control.COMBO_BOX, 
                 name = "scanParametersCSV", 
                 type = dtype.COMBO, 
                 comment = "Required for Slice Timing Correction.\n\n"
                           "Path to a .csv file containing information about scan acquisition parameters.\n\n"
                           "For instructions on how to create this file, see the User Guide.\n\n"
                           "If 'None' is specified, CPAC will skip Slice Timing Correction.",
                 values = "None")
        
        self.page.add(label = "Output Directory ", 
                      control = control.DIR_COMBO_BOX, 
                      name = "outputSubjectListLocation", 
                      type = dtype.STR, 
                      comment = "Directory where CPAC should place subject list files.",
                      values = os.getcwd())
        self.page.set_sizer()
         
        mainSizer.Add(self.window, 1, wx.EXPAND)
        
        btnPanel = wx.Panel(self.panel, -1)
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        

        self.multiscan = wx.CheckBox(btnPanel, -1, label = "Multiscan Data")
        hbox.Add(self.multiscan, 0.6, flag = wx.RIGHT| wx.BOTTOM, border =5)
        
        run_ext = wx.Button(btnPanel, ID_RUN_EXT, "Generate Sublist", (280,10), wx.DefaultSize, 0 )
        self.Bind(wx.EVT_BUTTON, self.run_extract_data, id=ID_RUN_EXT)
        hbox.Add( run_ext, 1, flag=wx.LEFT|wx.ALIGN_LEFT, border=10)
        
        buffer = wx.StaticText(btnPanel, label = "\t\t\t\t")
        hbox.Add(buffer)
    
        cancel = wx.Button(btnPanel, wx.ID_CANCEL, "Cancel",(220,10), wx.DefaultSize, 0 )

        self.Bind(wx.EVT_BUTTON, self.cancel, id=wx.ID_CANCEL)
        hbox.Add( cancel, 0, flag=wx.LEFT|wx.BOTTOM, border=5)
        
        load = wx.Button(btnPanel, wx.ID_ADD, "Load Settings", (280,10), wx.DefaultSize, 0 )
        self.Bind(wx.EVT_BUTTON, self.save, id=wx.ID_ADD)
        hbox.Add(load, 0.6, flag=wx.LEFT|wx.BOTTOM, border=5)
        
        save = wx.Button(btnPanel, wx.ID_SAVE, "Save Settings", (280,10), wx.DefaultSize, 0 )
        self.Bind(wx.EVT_BUTTON, self.save, id=wx.ID_SAVE)
        hbox.Add(save, 0.6, flag=wx.LEFT|wx.BOTTOM, border=5)
    
        btnPanel.SetSizer(hbox)
        
        mainSizer.Add(btnPanel, 0.5,  flag=wx.ALIGN_RIGHT|wx.RIGHT, border=20)
        
        self.panel.SetSizer(mainSizer)
        
        self.Show()
        
    def cancel(self, event):
        self.Close()
        
        
    def run(self, event):
        pass
        
        
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
         
         
    def save(self, event, flag):
        
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
                    
                if value.startswith('%s'):
                    display(win, "Template cannot start with %s")
                    return
            
            if '/' in value and 'Template' not in name:
                if not os.path.exists(ctrl.get_selection()):
                    display(win,"%s field contains incorrect path. Please update the path!"%ctrl.get_name())
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