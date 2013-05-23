import wx
import generic_class
from .constants import control, dtype, substitution_map
import os
import ast
import yaml
        

ID_RUN = 11

class ModelConfig(wx.Frame):
    
    
    def __init__(self, parent):

        wx.Frame.__init__(self, parent=parent, title="FSL Model Setup", size = (900,590))
        
        mainSizer = wx.BoxSizer(wx.VERTICAL)
        
        self.panel = wx.Panel(self)
        
        self.window = wx.ScrolledWindow(self.panel)
        
        self.page = generic_class.GenericClass(self.window, "FSL Model Setup") 
                
        self.page.add(label= "Columns/EV in Model",
                 control = control.TEXT_BOX,
                 name = "columnsInModel",
                 type = dtype.LSTR,
                 comment = "Specify which phenotypic variables and regressors to include in model \n"\
                            "These names should match column names in the template phenotypic csv",
                 values ="AgeAtScan, MeanFD, site, DxGroup",
                 style= wx.EXPAND | wx.ALL,
                 size = (600,-1))
        
        self.page.add(label= "Subject Column",
                 control = control.TEXT_BOX,
                 name = "subjectColumn",
                 type = dtype.STR,
                 comment = "Column Specifying subject id in phenotypic csv",
                 values ="subject_id",
                 style= wx.EXPAND | wx.ALL,
                size = (160,-1))
        
        self.page.add(label= "Categorical Vs Directional",
                 control = control.TEXT_BOX,
                 name = "categoricalVsDirectional",
                 type = dtype.LNUM,
                 comment = "Set a type for each of the variables/regressors entered above.\n"\
                            "1 = categorical, 0 = directional",
                 values ="0,0,1,1",
                 style= wx.EXPAND | wx.ALL,
                 size = (160,-1))
        
        self.page.add(label= "DeMean",
                 control = control.TEXT_BOX,
                 name = "deMean",
                 type = dtype.LNUM,
                 comment = "Specify whether to de-mean each column",
                 values ="1,1,0,0",
                 style= wx.EXPAND | wx.ALL,
                 size = (160,-1))
        

        
        self.page.add(label="Model Group Variance Seperately:", 
                 control=control.CHOICE_BOX, 
                 name='modelGroupVariancesSeparately', 
                 type=dtype.NUM, 
                 comment="This variable is used to setup different groups for different variances.\n"\
                         "When this option is set to 1, you need to specify the group column name below from the phenotypic file.\n" \
                         "This will result in giving different group number to different groups in the .grp file", 
                 values=["No", "Yes"])
        
        self.page.add(label= "Grouping Variable",
                 control = control.TEXT_BOX,
                 name = "groupingVariable",
                 type = dtype.STR,
                 comment = "Column name/EV which is used to assign different groups for the model.For more information\n"\
                            "Please refer to http://fsl.fmrib.ox.ac.uk/fsl/fslwiki/FEAT/UserGuide#Appendix_A:_Brief_Overview_of_GLM_Analysis",
                 values ="None",
                 size = (160,-1))
        
        self.page.add(label="Phenotypic Filepath", 
                 control=control.COMBO_BOX, 
                 name = "phenotypicFile", 
                 type = dtype.STR, 
                 comment = "Specify the full path to template_phenotypic.csv.",
                 values = "/path/to/template_phenotypic.csv")
        
        self.page.add(label = "SubjectList FilePath", 
                      control = control.COMBO_BOX, 
                      name = "subjectListFile", 
                      type = dtype.STR, 
                      comment = "Specify the full path to subject list for this model",
                      values = '/path/to/subject_list_group_analysis.txt')
        
        self.page.add(label = "Output Model CSV File", 
                      control = control.TEXT_BOX, 
                      name = "outputModelFile", 
                      type = dtype.STR, 
                      comment = "Specify teh path for the model file .csv to be output. This file will be created by the tool.",
                      values = './model_fsl.csv',
                      style= wx.EXPAND | wx.ALL,
                      size = (600,-1),
                      validation_req = False)
        
        self.page.add(label = "Contrast File for the Model", 
                      control = control.COMBO_BOX, 
                      name = "contrastFile", 
                      type = dtype.STR, 
                      comment = "Full path to a contrast file. Columns names should be -\n"\
                                "'columnnames__value' for categorical variables & 'columnname' for directional variables.\n"\
                                "Also, f_test_1 f_test_2 ... f_test_n for n f tests. if no ftest then don't specify this column.\n"\
                                "Note:- if you want to drop a column from the model then don't mention the column name.",
                      values = '/path/to/contrasts.csv')
    
        self.page.add(label= "Model Name",
                 control = control.TEXT_BOX,
                 name = "modelName",
                 type = dtype.STR,
                 comment = "Specify a name for the model",
                 values ="my_model",
                 size = (200,-1))

        
        self.page.add(label = "Output Model Files Directory", 
                      control = control.DIR_COMBO_BOX, 
                      name = "outputModelFilesDirectory", 
                      type = dtype.STR, 
                      comment = "Path to directory where the output model files will be put.",
                      values = os.getcwd())
        
        
        self.page.set_sizer()
         
        mainSizer.Add(self.window, 1, wx.EXPAND)
        
        btnPanel = wx.Panel(self.panel, -1)
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        
        run = wx.Button(btnPanel, ID_RUN, "CREATE MODEL", (280,-1), wx.DefaultSize, 0 )
        self.Bind(wx.EVT_BUTTON, lambda event: self.save(event,'run'), id=ID_RUN)
        hbox.Add( run, 0, flag=wx.LEFT|wx.ALIGN_LEFT, border=10)
         
        buffer = wx.StaticText(btnPanel, label = "\t\t\t\t\t\t")
        hbox.Add(buffer)
              
        cancel = wx.Button(btnPanel, wx.ID_CANCEL, "CANCEL",(220,10), wx.DefaultSize, 0 )
        self.Bind(wx.EVT_BUTTON, self.cancel, id=wx.ID_CANCEL)
        hbox.Add( cancel, 0, flag=wx.LEFT|wx.BOTTOM, border=5)
        
        load = wx.Button(btnPanel, wx.ID_ADD, "LOAD Settings", (200,-1),wx.DefaultSize, 0)
        self.Bind(wx.EVT_BUTTON, self.load, id = wx.ID_ADD)
        hbox.Add(load, 0.6, flag = wx.LEFT| wx.BOTTOM, border = 5)
        
        save = wx.Button(btnPanel, wx.ID_SAVE, "SAVE Settings", (200,-1), wx.DefaultSize, 0 )
        self.Bind(wx.EVT_BUTTON, lambda event: self.save(event,'save'), id=wx.ID_SAVE)
        hbox.Add(save, 0.6, flag=wx.LEFT|wx.BOTTOM, border=5)
    
        btnPanel.SetSizer(hbox)
        
        
        mainSizer.Add(btnPanel, 0.5,  flag=wx.ALIGN_RIGHT|wx.RIGHT, border=20)
        
        self.panel.SetSizer(mainSizer)
        
        self.result = []
        
        self.Show()
        
    def cancel(self, event):
        self.Close()
        
    def display(self,win, msg):
        wx.MessageBox(msg, "Error")
        win.SetBackgroundColour("pink")
        win.SetFocus()
        win.Refresh()
        raise ValueError
            
    def validate(self, config_map):
        try:
            import ast
            
            columns = [v.strip() for v in config_map.get('columnsInModel')[1].split(",")]
            
            
            if not columns:
                self.display(config_map.get('columnsInModel')[0], "No columns specified for the model")
                return -1 
            
            for key, val in config_map.iteritems():
                
                if key != 'groupingVariable' and len(val[1]) == 0:
                    self.display(val[0],"%s field is empty!"%key)
                    
                if '/' in val[1] and val[2]: 
                    if not os.path.exists(val[1]) :
                        self.display(val[0],"%s field contains incorrect path. Please enter correct path!"%key)
                                   
                
                if key == 'categoricalVsDirectional' or key == 'deMean':
                    value = [int(v) for v in val[1].split(",")]
                    for v in value:
                        if v not in [1,0]:
                            self.display(val[0], "Invalid Entry. Only 1 and 0 entry allowed")
                    
                    if len(value) != len(columns):
                        self.display(val[0], "Number of values in %s do not match specified columns in the model"%key)
       
                if key == 'groupingVariable':
                    if str(config_map.get('modelGroupVariancesSeparately')[1]) == "Yes":
                        if len(val[1]) ==0:
                            self.display(val[0],"%s field is empty!"%key)
                            
                        if val[1] not in columns:
                            self.display(val[0], "Grouping variable/column not a valid column in the model. Please verify the name")
                

                
            return 1
      
        except Exception:
            return -1
    
    
    def run_model(self, config):
        try:
            print "executing fsl model"
            import CPAC
            CPAC.utils.create_fsl_model.run(config)
            return 1
        except ImportError, e:
            wx.MessageBox("Error importing CPAC. Unable to run FSL Create Model tool.", "Error") 
            print "Error importing CPAC"
            print e
            return -1
        except Exception, e:
            wx.MessageBox("Error running fsl create model. %s"%e, "Error")
            print "Error running fsl create model tool. Problem with the configuration"
            print e
            return -1
         
    def save(self, event, flag):
        
        config_list =[]
        config_map = {}
        
        for ctrl in self.page.get_ctrl_list():
            
            print "validating ctrl-->", ctrl.get_name()
            print "ctrl.get_selection()", ctrl.get_selection()
            print "type(ctrl.get_selection())", type(ctrl.get_selection())
            
            win = ctrl.get_ctrl()        
            value = str(ctrl.get_selection())
            name = ctrl.get_name()
            dtype= ctrl.get_datatype()
            validation = ctrl.get_validation()
            help = ctrl.get_help()
            
            config_list.append((name, value, dtype, help))
            config_map[name] = [win, value, validation]
            
        try:
            if self.validate(config_map) >0:
                dlg = wx.FileDialog(self, message="Save file as ...", 
                defaultDir=os.getcwd(), 
                defaultFile="config_fsl.yaml", 
                wildcard="YAML files(*.yaml, *.yml)|*.yaml;*.yml", 
                style=wx.SAVE)
        
                if dlg.ShowModal() == wx.ID_OK:
                    
                    path = dlg.GetPath()
                    f = open(path, 'w')
                    dlg.Destroy()
                    for item in config_list:
                        if item[2] == 2:
                            value = substitution_map.get(str(item[1]))
                            if value is None:
                                value = ast.literal_eval(item[1])
                        elif item[2] == 5:
                            value = [v for v in ast.literal_eval(item[1])]
                        elif item[2] == 4:
                            value = [str(v.strip()) for v in item[1].split(',')]
                        else:
                            value = str(item[1])
                        
                        for lines in item[3].split('\n'):
                            print >> f, "#", lines
                                       
                        print >> f, item[0], ": ", value, "\n"
                
                print "saving %s"%path               
                f.close()
                            
                if flag == 'run':
                    if self.run_model(path) >0:
                        self.result = []
                        self.result.append(config_map.get('outputModelFilesDirectory')[1])
                        self.result.append(config_map.get('subjectListFile')[1])
                        
                
                if len(self.result) ==2:
                    self.Parent.box1.GetTextCtrl().SetValue(self.result[0])
                    self.Parent.box2.GetTextCtrl().SetValue(self.result[1])
                
                self.Close()
   
        except Exception:
            print "error writing temp file "
            raise
        
    def load(self, event):
        import os
        dlg = wx.FileDialog(
            self, message="Choose the config fsl yaml file",
                defaultDir=os.getcwd(), 
                defaultFile="",
                wildcard= "YAML files(*.yaml, *.yml)|*.yaml;*.yml",
                style=wx.OPEN | wx.CHANGE_DIR)
        
        if dlg.ShowModal() == wx.ID_OK:
            path = dlg.GetPath()
                
            config_map = yaml.load(open(path, 'r'))
            
            for ctrl in self.page.get_ctrl_list():
                name = ctrl.get_name()
                value = config_map.get(name)
                dtype = ctrl.get_datatype()
                if isinstance(value, list):
                    val = None
                    for v in value:
                        if val:
                            val = val + "," + str(v)
                        else:
                            val = str(v)
                else:
                    val = substitution_map.get(value)
                    if val == None:
                        val = value
            
                #print "setting value in ctrl name, value -->", name, val             
                ctrl.set_value(str(val))
            
                    
            dlg.Destroy()
        
