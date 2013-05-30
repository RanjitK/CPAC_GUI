import wx
from ..utils.constants import substitution_map
from ..pages import WorkflowConfig, Motion, AnatomicalPreprocessing, \
    Segmentation,  Registration, FunctionalPreProcessing,\
    MotionOptions, Scrubbing, AnatToFuncRegistration, FuncToMNIRegistration,\
    VMHC, VMHCSettings, ReHo, ReHoSettings, \
    SCA, SCASettings, MultipleRegressionSCA,\
    Settings, ComputerSettings, DirectorySettings, \
    Nuisance, NuisanceCorrection, \
    CentralitySettings, Centrality,\
    ALFF, ALFFSettings,\
    Smoothing, SmoothingSettings,\
    Filtering, FilteringSettings,\
    TimeSeries, ROITimeseries, VOXELTimeseries, \
    SpatialRegression, GenerateSeeds, VerticesTimeSeries,\
    GroupAnalysis, GPASettings, BASCSettings,\
    BASC, CWAS, CWASSettings,\
    DualRegression, DualRegressionOptions, TimeSeriesOptions

ID_SUBMIT = 6


class Mybook(wx.Treebook):

    def __init__(self, parent):
        wx.Treebook.__init__(self, parent, wx.ID_ANY, style=
                             wx.BK_DEFAULT)
        self.page_list = []

        # create the page windows as children of the notebook
        page1 = Settings(self)
        page2 = ComputerSettings(self)
        page3 = DirectorySettings(self)
        page4 = WorkflowConfig(self)

        page5 = AnatomicalPreprocessing(self)
        page6 = Registration(self, 1)
        page7 = Segmentation(self, 2)

        page8 = FunctionalPreProcessing(self)
        page9 = TimeSeriesOptions(self)
        page10 = AnatToFuncRegistration(self, 5)
        page11 = FuncToMNIRegistration(self, 6)

        page12 = Nuisance(self)
        page13 = NuisanceCorrection(self, 7)

        page14 = Filtering(self)
        page15 = FilteringSettings(self, 9)

        page16 = Motion(self)
        page17 = MotionOptions(self)
        page18 = Scrubbing(self, 4)

        page19 = TimeSeries(self)
        page20 = GenerateSeeds(self)
        page21 = ROITimeseries(self)
        page22 = VOXELTimeseries(self)
        page23 = VerticesTimeSeries(self)
        page24 = SpatialRegression(self)

        page25 = SCA(self)
        page26 = SCASettings(self)
        page27 = MultipleRegressionSCA(self)

        page28 = DualRegression(self)
        page29 = DualRegressionOptions(self)

        page30 = VMHC(self)
        page31 = VMHCSettings(self)

        page32 = ALFF(self)
        page33 = ALFFSettings(self)

        page34 = Centrality(self)
        page35 = CentralitySettings(self)

        page36 = ReHo(self)
        page37 = ReHoSettings(self)

        page38 = Smoothing(self)
        page39 = SmoothingSettings(self)

        page40 = BASC(self)
        page41 = BASCSettings(self)

        page42 = CWAS(self)
        page43 = CWASSettings(self)

        page44 = GroupAnalysis(self)
        page45 = GPASettings(self)

        # add the pages to the notebook with the label to show on the tab
        self.AddPage(page1, "Environment Setup", wx.ID_ANY)
        self.AddSubPage(page2, "Computer Settings", wx.ID_ANY)
        self.AddSubPage(page3, "Output Settings", wx.ID_ANY)
        self.AddSubPage(page4, "Preprocessing Workflow Options", wx.ID_ANY)

        self.AddPage(page5, "Anatomical Preprocessing", wx.ID_ANY)
        self.AddSubPage(page6, "Anatomial Registration", wx.ID_ANY)
        self.AddSubPage(page7, "Tissue Segmentation", wx.ID_ANY)

        self.AddPage(page8, "Functional Preprocessing", wx.ID_ANY)
        self.AddSubPage(page9, "Time Series Options", wx.ID_ANY)
        self.AddSubPage(page10, "Anatomical to Functional Registration", wx.ID_ANY)
        self.AddSubPage(page11, "Functional to MNI Registration", wx.ID_ANY)

        self.AddPage(page12, "Nuisance", wx.ID_ANY)
        self.AddSubPage(page13, "Nuisance Correction", wx.ID_ANY)

        self.AddPage(page14, "Temporal Filtering", wx.ID_ANY)
        self.AddSubPage(page15, "Temporal Filtering Options", wx.ID_ANY)

        self.AddPage(page16, "Motion Correction", wx.ID_ANY)
        self.AddSubPage(page17, "Motion Correction Options", wx.ID_ANY)
        self.AddSubPage(page18, "Scrubbing Options", wx.ID_ANY)

        self.AddPage(page19, "Time Series Extraction", wx.ID_ANY)
        self.AddSubPage(page20, "Define New Seeds", wx.ID_ANY)
        self.AddSubPage(page21, "ROI Average Time Series", wx.ID_ANY)
        self.AddSubPage(page22, "ROI Voxelwise Time Series", wx.ID_ANY)
        self.AddSubPage(page23, "Surface Vertices Time Series", wx.ID_ANY)
        self.AddSubPage(page24, "Spatial Regression", wx.ID_ANY)

        self.AddPage(page25, "SCA", wx.ID_ANY)
        self.AddSubPage(page26, "SCA Settings", wx.ID_ANY)
        self.AddSubPage(page27, "Mutiple Regression SCA", wx.ID_ANY)

        self.AddPage(page28, "Dual Regression", wx.ID_ANY)
        self.AddSubPage(page29, "Dual Regression Options", wx.ID_ANY)

        self.AddPage(page30, "Voxel-mirrored Homotopic Connectivity", wx.ID_ANY)
        self.AddSubPage(page31, "VMHC Settings", wx.ID_ANY)

        self.AddPage(page32, "ALFF and f/ALFF", wx.ID_ANY)
        self.AddSubPage(page33, "ALFF and f/ALFF Options", wx.ID_ANY)

        self.AddPage(page34, "Network Centrality", wx.ID_ANY)
        self.AddSubPage(page35, "Network Centrality Options", wx.ID_ANY)

        self.AddPage(page36, "Regional Homogeneity (ReHo)", wx.ID_ANY)
        self.AddSubPage(page37, "ReHo Options", wx.ID_ANY)

        self.AddPage(page38, "Spatial Smoothing", wx.ID_ANY)
        self.AddSubPage(page39, "Spatial Smoothing Options", wx.ID_ANY)

        self.AddPage(page40, "BASC", wx.ID_ANY)
        self.AddSubPage(page41, "BASC Settings", wx.ID_ANY)

        self.AddPage(page42, "CWAS", wx.ID_ANY)
        self.AddSubPage(page43, "CWAS Settings", wx.ID_ANY)

        self.AddPage(page44, "Group Analysis", wx.ID_ANY)
        self.AddSubPage(page45, "Group Analysis Settings", wx.ID_ANY)

        self.Bind(wx.EVT_TREEBOOK_PAGE_CHANGED, self.OnPageChanged)
        self.Bind(wx.EVT_TREEBOOK_PAGE_CHANGING, self.OnPageChanging)

        # This is a workaround for a sizing bug on Mac...
        wx.FutureCall(100, self.AdjustSize)

        self.Refresh()

    def OnPageChanged(self, event):
        old = event.GetOldSelection()
        new = event.GetSelection()
        sel = self.GetSelection()
        event.Skip()

    def OnPageChanging(self, event):
        old = event.GetOldSelection()
        new = event.GetSelection()
        sel = self.GetSelection()
        event.Skip()

    def AdjustSize(self):
        self.GetTreeCtrl().InvalidateBestSize()
        self.SendSizeEvent()

    def get_page_list(self):
        return self.page_list

    def get_page(self, index):
        return self.page_list[index]


class MainFrame(wx.Frame):

    def __init__(self, parent, option='save', path="", pipeline_id=""):
        wx.Frame.__init__(
            self, parent=parent, title="CPAC Pipeline Configuration", size=(1200, 500))

        # Here we create a panel and a notebook on the panel
        self.p = wx.Panel(self)
        self.nb = Mybook(self.p)
        self.path = path
        self.pipeline_id = pipeline_id
        self.option = option
        self.parent = parent

        btnPanel = wx.Panel(self.p, -1)
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        submit = wx.Button(btnPanel, wx.ID_SAVE, "Save", (
            280, 10), wx.DefaultSize, 0)
        hbox.Add(submit, 0.6, wx.ALIGN_RIGHT | wx.ALL, 5)
        self.Bind(wx.EVT_BUTTON, self.submit_item, id=wx.ID_SAVE)
        cancel = wx.Button(btnPanel, wx.ID_CANCEL, "Cancel", (
            220, 10), wx.DefaultSize, 0)
        self.Bind(wx.EVT_BUTTON, self.cancel, id=wx.ID_CANCEL)
        hbox.Add(cancel, 0, wx.ALIGN_RIGHT | wx.ALL, 5)
        btnPanel.SetSizer(hbox)

        # finally, put the notebook in a sizer for the panel to manage
        # the layout
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.nb, 1, wx.EXPAND)
        sizer.Add(btnPanel, 0.6, wx.EXPAND | wx.RIGHT, 20)

        self.p.SetSizer(sizer)

        self.Layout()
        self.Show()
        if option == 'edit' or option == 'load':
            self.load()

    def load(self):

        import yaml
        try:
            config_file_map = yaml.load(open(self.path, 'r'))
        except:
            Exception("Error importing file - %s , Make"
                      " sure it is in correct yaml format")

        for page in self.nb.get_page_list():
            ctrl_list = page.page.get_ctrl_list()

            for ctrl in ctrl_list:
                name = ctrl.get_name()
                val = config_file_map.get(str(name))
                print "loading ctrl -> value", name, "->", val
                sample_list = ctrl.get_values()
                if val:
                    if isinstance(val, list):
                        if ctrl.get_datatype() == 8:
                            value = []
                            for item in val:
                                data = ""
                                for k, v in item.iteritems():
                                    if v == 1 and k in sample_list:
                                        if data:
                                            data = data + "," + k
                                        else:
                                            data = k
                                value.append(data)

                        elif ctrl.get_datatype() == 6:
                            value = []
                            for v in val:
                                value.append(str(v))

                        elif ctrl.get_datatype() == 3:
                            value = [sample_list[i]
                                     for i, x in enumerate(val) if x == True]

                        elif ctrl.get_datatype() == 4:
                            s_map = dict((v, k)
                                         for k, v in substitution_map.iteritems())
                            value = [s_map.get(item)
                                     for item in val if s_map.get(item) != None]
                            if not value:
                                value = [ str(item) for item in val]
                                
                        elif ctrl.get_datatype() == 5 and ctrl.get_type() == 6:
                                value = [sample_list[v] for v in val]
                                
                        else:
                            value = None
                            for v in val:
                                if value:
                                    value = value + "," + str(v)
                                else:
                                    value = str(v)
                    else:
                        if ctrl.get_datatype() == 2 and ctrl.get_type == 0:
                            value = sample_list[v]
                        else:
                            value = str(val)
                else:
                    value = ""

                print "setting value in ctrl -->", value
                print "type -->", type(value)
                ctrl.set_value(value)

    def submit_item(self, event):
        import os
        import linecache

        def display(win, msg, changeBg=True):
            wx.MessageBox(msg, "Error")
            if changeBg:
                win.SetBackgroundColour("pink")
            win.SetFocus()
            win.Refresh()

        config_list = []
        hash_val = 0
        wf_counter = []

        print "self.nb.get_page_list()", self.nb.get_page_list()
        for page in self.nb.get_page_list():
            print "page ----> ", page
            switch = page.page.get_switch()
            print "switch ---->", switch
            ctrl_list = page.page.get_ctrl_list()
            validate = False

            if switch:
                switch_val = str(switch.get_selection()).lower()
                print "switch_val ---->", switch_val
                if switch_val == 'on' or switch_val == 'true' or switch_val == '1':
                    validate = True
                    wf_counter.append(page.get_counter())

            for ctrl in ctrl_list:
                
                #validating
                if (switch == None or validate) and ctrl.get_validation():


                    win = ctrl.get_ctrl()
                    print "validating ctrl-->", ctrl.get_name()
                    print "ctrl.get_selection()", ctrl.get_selection()
                    print "type(ctrl.get_selection())", type(ctrl.get_selection())

                    if isinstance(ctrl.get_selection(), list):
                        value = ctrl.get_selection()
                        if not value:
                            display(
                                win, "%s field is empty or the items are not checked!" % ctrl.get_name(), False)
                            return
                    else:
                        value = str(ctrl.get_selection())

                    if len(value) == 0:
                        display(win, "%s field is empty!" % ctrl.get_name())
                        return
                        
                    if '/' in value and '$' not in value and not isinstance(value, list):

                        if not os.path.exists(ctrl.get_selection()):
                            display(
                                win, "%s field contains incorrect path. Please update the path!" % ctrl.get_name())
                            return

                config_list.append(ctrl)

        dlg = wx.FileDialog(
            self, message="Save CPAC configuration file as ...", defaultDir=os.getcwd(),
            defaultFile="", wildcard="YAML files(*.yaml, *.yml)|*.yaml;*.yml", style=wx.SAVE)
        dlg.SetFilterIndex(2)

        if dlg.ShowModal() == wx.ID_OK:
            self.path = dlg.GetPath()

            self.write(self.path, config_list)
            dlg.Destroy()
            if self.option != 'edit':
                for counter in wf_counter:
                    if counter != 0:
                        hash_val += 2 ** counter
                print "wf_counter -- ", wf_counter
                print "hashval --> ", hash_val
                pipeline_id = linecache.getline('pipeline_names.py', hash_val)
                print "pipeline_id ==", pipeline_id
                if os.path.exists(self.path):
                    self.update_listbox(pipeline_id)
            else:
                pipeline_map = self.parent.get_pipeline_map()
                pipeline_map[self.pipeline_id] = self.path
            self.SetFocus()
            self.Close()

    def cancel(self, event):
        self.Close()

    def update_listbox(self, value):

        while True:
            dlg = wx.TextEntryDialog(
                self, 'Please enter a unique pipeline id for the configuration',
                'Pipeline Id', value.strip())
            dlg.SetValue(str(value.strip()))
            dlg.Restore()
            if dlg.ShowModal() == wx.ID_OK:
                if len(dlg.GetValue()) > 0:
                    self.pipeline_id = dlg.GetValue()
                    pipeline_map = self.parent.get_pipeline_map()
                    if pipeline_map.get(self.pipeline_id) == None:
                        pipeline_map[self.pipeline_id] = self.path
                        self.Parent.listbox.Append(self.pipeline_id)
                        dlg.Destroy()
                        break
                    else:

                        dlg2 = wx.MessageDialog(
                            self, 'Pipeline already exist. Please enter a new name',
                            'Error!',
                            wx.OK | wx.ICON_ERROR)
                        dlg2.ShowModal()
                        dlg2.Destroy()

    def write(self, path, config_list):
        import ast

        try:
            f = open(path, 'w')

            for item in config_list:
                label = item.get_name()
                value= item.get_selection()
                dtype = item.get_datatype()
                type = item.get_type()

                sample_list = item.get_values()
                comment = item.get_help()
                print "*****label : type : value -->", label, " : ", dtype, " : ", value
                for line in comment.split("\n"):
                    if line:
                        print>>f, "#", line

                if dtype ==0 or dtype==1:
                    print >>f, label, ": ", str(value)
                    print >>f,"\n"
                elif dtype ==2:
                    if type ==0:
                        value = sample_list.index(value)
                    else:
                        if value != 'None':
                            value = ast.literal_eval(str(value))
                    print >>f, label, ": ", value
                    print >>f,"\n"
                elif dtype ==3:
                    map = ast.literal_eval(str(value))
                    values = []
                    for x in range(0, len(map.keys())):
                        values.append(False)
                    for k, v in map.iteritems():
                        item, idx = k
                        values[idx] = v
                    print>> f, label, ": ", values
                    print>>f,"\n"
                elif dtype ==4:
                    values=[]

                    if isinstance(value, list):
                        value = ast.literal_eval(str(value))
                    else:
                        value = str(value).split(",")

                    for val in value:
                        val = val.strip()
                        sval = substitution_map.get(val)
                        print "val, sval -->", val, sval
                        if sval != None:
                            values.append(sval)
                        else:
                            values.append(val)
                    print>> f, label, ": ", values
                    print>>f,"\n"
                elif dtype ==5:
                    value = ast.literal_eval(str(value))
                    if isinstance(value, tuple):
                        value = list(value)
                    elif isinstance(value, list):
                        value = [sample_list.index(val) for val in value]
                    else:
                        value = [value]
                    print>>f, label, ":", value
                    print>>f, "\n"
                elif dtype ==6:
                    values = [] 
                    for val in ast.literal_eval(str(value)):
                        values.append(ast.literal_eval(val))
                    print>>f, label, ":", values
                    print>>f, "\n"
                elif dtype ==8:
                    print>>f, label,":"

                    value = ast.literal_eval(str(value))
                    for val in value:
                        val = val.split(',')
                        print "val-->", val
                        f.write("  - ")
                        flag = 0
                        for sample in sample_list:
                            if flag == 0:
                                space = ""
                                flag = 1
                            else:
                                space = "    "
                            if sample in val:
                                print>>f, space, sample, ": ", 1
                            else:
                                print>>f, space, sample, ": ", 0
                    print >>f, "\n"

                else:
                    value = ast.literal_eval(str(value))
                    print>>f, label, ":", value
                    print>>f, "\n"

            f.close()
        except Exception, e:
            print e
            print "Error Writing the pipeline configuration file %s" % path
            raise Exception
