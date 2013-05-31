import wx
import wx.html
from ..utils.generic_class import GenericClass
from ..utils.constants import control, dtype
from ..utils.validator import CharValidator

class GroupAnalysis(wx.html.HtmlWindow):
    def __init__(self, parent, counter  = 0):
        from urllib2 import urlopen
        wx.html.HtmlWindow.__init__(self, parent, style= wx.html.HW_SCROLLBAR_AUTO)
        self.SetStandardFonts()
        
        self.counter = counter
        
        self.LoadFile('html/group_analysis.html')
        
#        try:
#            code = urlopen("http://fcp-indi.github.io/docs/user/fsl_ga.html").code
#            if (code / 100 < 4):
#                self.LoadPage('http://fcp-indi.github.io/docs/user/fsl_ga.html')
#            else:
#                self.LoadFile('html/group_analysis.html')
#        except:
#            self.LoadFile('html/group_analysis.html')
#            
            
    def get_counter(self):
        return self.counter
    
    
class GPASettings(wx.ScrolledWindow):
    
    def __init__(self, parent, counter = 0):
        wx.ScrolledWindow.__init__(self, parent)
                
        self.counter = counter
        
        self.page = GenericClass(self, "FSL/FEAT Group Analysis Options")
        
        self.page.add(label="Run Group Analysis ", 
                      control=control.CHOICE_BOX, 
                      name='runGroupAnalysis', 
                      type=dtype.LSTR, 
                      comment="Run group analysis using FSL/FEAT.", 
                      values=["Off","On"],
                      wkf_switch = True)
        
        self.page.add(label = "Select Derivatives ",
                    control = control.CHECKLIST_BOX,
                    name = "derivativeList",
                    type = dtype.LSTR,
                    values = ['ROI Average SCA', 
                              'Voxelwise SCA',
                              'Multiple Regression SCA',
                              'Dual Regression',
                              'VMHC',
                              'ALFF', 
                              'f/ALFF', 
                              'ReHo',
                              'Network Centrality'],
                    comment = "Select which derivatives you would like to include when running group analysis.\n\nWhen including Dual Regression, make sure to correct your P-value for the number of maps you are comparing.\n\nWhen including Multiple Regression SCA, you must have more degrees of freedom (subjects) than there were time series.",
                    size = (220,160))
 
        self.page.add(label = "Models to Run ",
                      control = control.LISTBOX_COMBO,
                      name = 'modelFile',
                      type = dtype.LOFL,
                      values = "",
                      comment="Use the + to add FSL models to be run.",
                      size = (400,100),
                      combo_type = 3)

        self.page.add(label="Models Contain F-tests ", 
                 control=control.CHOICE_BOX, 
                 name='fTest', 
                 type=dtype.BOOL, 
                 comment = "Set this option to True if any of the models specified above contain F-tests.", 
                 values=["False","True"])
        
        self.page.add(label="Z threshold ", 
                     control=control.FLOAT_CTRL, 
                     name='zThreshold', 
                     type=dtype.NUM, 
                     comment="Only voxels with a Z-score higher than this value will be considered significant.", 
                     values=2.3)

        self.page.add(label="Cluster Significance Threshold ", 
                     control=control.FLOAT_CTRL, 
                     name='pThreshold', 
                     type=dtype.NUM, 
                     comment="Significance threshold (P-value) to use when doing cluster correction for multiple comparisons.", 
                     values=0.05)

        self.page.add(label="Include All Scans ", 
                 control=control.CHOICE_BOX, 
                 name='mixedScanAnalysis', 
                 type=dtype.BOOL, 
                 comment="In cases where each subject has more than one functional scan, specify whether all or only the first scan should be included when running group analysis.", 
                 values=["False","True"])
                
        self.page.set_sizer()
        parent.get_page_list().append(self)
        
    def get_counter(self):
            return self.counter
        
        
class BASC(wx.html.HtmlWindow):
    def __init__(self, parent, counter  = 0):
        from urllib2 import urlopen
        wx.html.HtmlWindow.__init__(self, parent, style= wx.html.HW_SCROLLBAR_AUTO)
        self.SetStandardFonts()
        
        self.counter = counter
        
        self.LoadFile('html/basc.html')
        
#        try:
#            code = urlopen("http://fcp-indi.github.io/docs/user/basc.html").code
#            if (code / 100 < 4):
#                self.LoadPage('http://fcp-indi.github.io/docs/user/basc.html')
#            else:
#                self.LoadFile('html/basc.html')
#        except:
#            self.LoadFile('html/basc.html')
            
            
    def get_counter(self):
        return self.counter
    
    
    
class BASCSettings(wx.ScrolledWindow):
    
    def __init__(self, parent, counter = 0):
        wx.ScrolledWindow.__init__(self, parent)
                
        self.counter = counter
        
        self.page = GenericClass(self, "Bootstrap Analysis of Stable Clusters (BASC)")
        
        self.page.add(label="Run BASC:", 
                      control=control.CHOICE_BOX, 
                      name='runBASC', 
                      type=dtype.LSTR, 
                      comment="Run BASC", 
                      values=["Off","On"],
                      wkf_switch = True)
        
        self.page.add(label="BASC ROI File:", 
                     control=control.COMBO_BOX, 
                     name='bascROIFile', 
                     type=dtype.STR, 
                     values = "/path/to/basc_mask_file",
                     comment="Path to a mask file. Voxels outside this mask will be excluded from BASC.")
        
        self.page.add(label="BASC Affinity Threshold File:", 
                     control=control.COMBO_BOX, 
                     name='bascAffinityThresholdFile', 
                     type=dtype.STR, 
                     values = "/path/to/basc_affinity_threshold_file",
                     comment="Path to a text file containing Affinity Thresholds for each subject.\n"\
                            "These are correlation thresholds applied prior to spectral clustering.\n"\
                            "Can be subject specific when subjects have differing numbers of timepoints.\n"\
                            "Subjects should be in the same order as in the main subject list.")
        
        self.page.add(label= "BASC Clusters",
                 control=control.INT_CTRL, 
                 name='bascClusters', 
                 type=dtype.NUM, 
                 comment="Number of clusters at both the individual and group level.", 
                 values=6)
        
        self.page.add(label= "Number of Timeseries Bootstraps",
                 control=control.INT_CTRL, 
                 name='bascTimeseriesBootstraps', 
                 type=dtype.NUM, 
                 comment="Number of bootstraps to apply to original timeseries data.", 
                 values=100)
            
        self.page.add(label= "Number of Dataset Bootstraps",
                 control=control.INT_CTRL, 
                 name='bascDatasetBootstraps', 
                 type=dtype.NUM, 
                 comment="Number of bootstraps to apply to individual stability matrices.", 
                 values=100)
        
        self.page.set_sizer()
        parent.get_page_list().append(self)
        
    def get_counter(self):
            return self.counter
        
class CWAS(wx.html.HtmlWindow):
    def __init__(self, parent, counter  = 0):
        from urllib2 import urlopen
        wx.html.HtmlWindow.__init__(self, parent, style= wx.html.HW_SCROLLBAR_AUTO)
        self.SetStandardFonts()
        
        self.counter = counter
        self.LoadFile('html/cwas.html')
        
#        try:
#            code = urlopen("http://fcp-indi.github.io/docs/user/cwas.html").code
#            if (code / 100 < 4):
#                self.LoadPage('http://fcp-indi.github.io/docs/user/cwas.html')
#            else:
#                self.LoadFile('html/cwas.html')
#        except:
#            self.LoadFile('html/cwas.html')
            
            
    def get_counter(self):
        return self.counter
    
    
    
class CWASSettings(wx.ScrolledWindow):
    
    def __init__(self, parent, counter = 0):
        wx.ScrolledWindow.__init__(self, parent)
                
        self.counter = counter
        
        self.page = GenericClass(self, "Connectome-wide Association Studies (CWAS)")
        
        self.page.add(label="Run CWAS:", 
                      control=control.CHOICE_BOX, 
                      name='runCWAS', 
                      type=dtype.LSTR, 
                      comment="Run CWAS", 
                      values=["Off","On"],
                      wkf_switch = True)
        
        self.page.add(label="CWAS ROI File:", 
                     control=control.COMBO_BOX, 
                     name='cwasROIFile', 
                     type=dtype.STR, 
                     values = "/path/to/cwas_mask_file",
                     comment="Path to a mask file. Voxels outside this mask will be excluded from CWAS.")
        
        self.page.add(label="CWAS Regressor File:", 
                     control=control.COMBO_BOX, 
                     name='cwasRegressorFile', 
                     type=dtype.STR, 
                     values= '/path/to/cwas_regressor_file',
                     comment = "Path to a text file containing phenotypic regressor.")
        
        self.page.add(label= "CWAS FSamples",
                 control=control.INT_CTRL, 
                 name='cwasFSamples', 
                 type=dtype.NUM, 
                 comment="Number of permutation tests to run on the Psuedo-F statistic.", 
                 values=5000)
            
        self.page.add(label= "CWAS Parallel Nodes",
                 control=control.INT_CTRL, 
                 name='cwasParallelNodes', 
                 type=dtype.NUM, 
                 comment="Number of NiPype nodes to be created while computing CWAS.\n"\
                         "This number depends on computing resources.", 
                 values=10)
        
        self.page.set_sizer()
        parent.get_page_list().append(self)
        
    def get_counter(self):
            return self.counter