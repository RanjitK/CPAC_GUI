import wx
import wx.html
from ..windows.generic_class import GenericClass
from constants import control, dtype
from ..utils import CharValidator

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
        
        self.page = GenericClass(self, "FSL Group Analysis")
        
        self.page.add(label="Run Group Analysis:", 
                      control=control.CHOICE_BOX, 
                      name='runGroupAnalysis', 
                      type=dtype.LSTR, 
                      comment="Calculate group statistics", 
                      values=["Off","On"],
                      wkf_switch = True)
        
        self.page.add(label = "Select Derivatives:",
                    control = control.CHECKLIST_BOX,
                    name = "derivativeList",
                    type = dtype.LSTR,
                    values = ['SCA(voxel_based)', 
                              'SCA(roi_based)',
                              'SCA(temporal_regression)',
                              'ALFF', 
                              'fALFF',
                              'VMHC', 
                              'ReHo',
                              'Centrality',
                              'Dual_Regression'],
                    comment = "Select which measures should be included in group analysis:\n"\
                              "Voxel-based SCA = sca_seed_Z_to_standard_smooth\n"\
                              "ROI based SCA = sca_roi_Z_to_standard_smooth\n"\
                              "Temporal REgression based SCA = sca_tempreg_maps_z_files_smooth\n"\
                              "ALFF = alff_Z_to_standard_smooth\n"\
                              "fALFF = falff_Z_to_standard_smooth\n"\
                              "VMHC = vmhc_z_score_stat_map\n"\
                              "Reho = reho_Z_to_standard_smooth\n"\
                              "Dual Regression = dr_tempreg_maps_z_files_smooth")
        
        self.page.add(label="Model Subjects Specification File:", 
                     control=control.COMBO_BOX, 
                     name='modelFile', 
                     type=dtype.STR, 
                     values = "/path/to/file_containing_templates.txt",
                     comment="Location of a text file containing a list of FSL models\n"\
                             "Each line in this file should be the path\n"\
                             "to a model directory space subject list for that model\n"\
                             "Each model directory should contain a .mat, .con, and .grp file\n"\
                             "If fTest = True (see below), model directories must also contain a .fts file\n"\
                             "These models can be generated through FSL, or using create_fsl_model.py\n"\
                             "For instructions on using create_fsl_model.py, see the user guide\n\n"\
                             "It can be a file with model and subject list(for that model) path in each line\n"\
                             "Example: /path.to/model_directory /path/to/model_list_and_subject_list.txt\n"\
                             "Note:- This file should have full path to model directory space full path to subject list for that model\n"\
                             "or\n"\
                             "It can be yaml list\n"\
                             "   modelFile:\n"\
                             "   -\n"\
                             "     - /home/data/configs/model_a\n"\
                             "     - /home/data/configs/subject_list_group_analysis_a.txt\n"\
                             "   -\n"\
                             "     - /home/data/configs/model_b\n"\
                             "     - /home/data/configs/subject_list_group_analysis_b.txt\n\n"\
                            "or\n"\
                            "it can be a simple list\n"\
                            "  modelFile : [ ['/home/data/configs/model_a', '/home/data/configs/model_a_sublist.txt']\n" \
                            "                ['/home/data/configs/model_b', '/home/data/configs/model_b_sublist.txt'] ]")
        
        self.page.add(label="Z threshold:", 
                     control=control.FLOAT_CTRL, 
                     name='zThreshold', 
                     type=dtype.NUM, 
                     comment="Z Statistic threshold value for cluster thresholding. It is the Z value used to\n"\
                             "determine what level of activation would be statistically significant.\n"\
                             "Increasing this will result in higher estimates of required effect.", 
                     values=2.3)

        self.page.add(label="P threshold:", 
                     control=control.FLOAT_CTRL, 
                     name='pThreshold', 
                     type=dtype.NUM, 
                     comment="Probability threshold for cluster thresholding", 
                     values=0.05)
        
        self.page.add(label="Run F-test:", 
                 control=control.CHOICE_BOX, 
                 name='fTest', 
                 type=dtype.BOOL, 
                 comment = "Ftest help investigate several contrasts at the same time\n"\
                           "for example to see whether any of them (or any combination of them) is\n"\
                           "significantly non-zero. Also, the F-test allows you to compare the\n"\
                           "contribution of each contrast to the model and decide on significant\n"\
                           "and non-significant ones", 
                 values=["False","True"])
                
        self.page.add(label="Run Mixed Scan Analysis:", 
                 control=control.CHOICE_BOX, 
                 name='mixedScanAnalysis', 
                 type=dtype.BOOL, 
                 comment="Specify whether to include all scans from a subject or only a single session\n"\
                         "If a subject has multiple scans:\n"\
                         "False = Consider only the first scan session during group analysis\n"\
                         "True = Consider all scan sessions", 
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