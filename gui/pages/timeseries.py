import wx
import wx.html
from ..windows.generic_class import GenericClass
from ..utils import control, dtype
from ..utils import CharValidator


class TimeSeries(wx.html.HtmlWindow):

    def __init__(self, parent, counter  = 0):
        from urllib2 import urlopen
        wx.html.HtmlWindow.__init__(self, parent, style= wx.html.HW_SCROLLBAR_AUTO)
        self.SetStandardFonts()
        
        self.counter = counter
        self.LoadFile('html/tse.html')
        
#        try:
#            code = urlopen("http://fcp-indi.github.io/docs/user/tse.html").code
#            if (code / 100 < 4):
#                self.LoadPage('http://fcp-indi.github.io/docs/user/tse.html')
#            else:
#                self.LoadFile('html/tse.html')
#        except:
#            self.LoadFile('html/tse.html')
            
            
    def get_counter(self):
        return self.counter
    
class GenerateSeeds(wx.ScrolledWindow):
    
    def __init__(self, parent, counter = 0):
        
        import os
        
        wx.ScrolledWindow.__init__(self, parent)
                
        self.counter = counter
        
        self.page = GenericClass(self, "Generate Seeds")
        
        self.page.add(label="Use Seed in Analysis:", 
         control=control.CHOICE_BOX, 
         name='useSeedInAnalysis', 
         type=dtype.LSTR, 
         comment="use the seeds specified in seedSpecificationFile in the following analysis \n"\
                 "1 = use in roi timeseries extraction \n"\
                 "2 = use in voxel timeseries extraction \n"\
                 "3 = use in network centrality \n"\
                 "users can specify a combination of these options",
         values=["Off","On"],
         wkf_switch = True)
        
        self.page.add(label="Seed Specification File:", 
                 control=control.COMBO_BOX, 
                 name = "seedSpecificationFile", 
                 type = dtype.STR, 
                 comment = "Path to Seed Specification File \n " 
                            "If seedSpecificationFile is not None and \n"
                            "points to a valid text file \n"
                            "CPAC Creates ROI file given user specifications \n"
                            "The ROI nifti file is saved in seed Output Location \n" 
                            "If seed Output Location does not exist, we create it for \n"
                            "as long as you specify it in the setting \n"
                            "If different Resolutions are specified then \n"
                            "the software will group the ROI's having the same \n"
                            "resolution and put each group in seperate nifti files \n"
                            "NOTE: We DO NOT detect for overlapping ROIS \n"
                            "The overlapping regions of the ROIS will have \n"
                            "intensity which the sum of intensity of individual \n"
                            "regions. Please check and avoid this prior to running CPAC \n"
                            "Each line in the file contains \n"
                            "seed_label x y z radius resolution \n"
                            "example : \n"
                            "10    -6   52  -2  4 2mm \n"
                            "70    -8  -56  26  4 2mm \n"
                            "60     0   52  6   4 1mm \n"
                            "1     -54 -54  28  4 4mm \n"
                            "7     -60 -24 -18  4 4mm",
                 values = "None")
        
        self.page.add(label = "Seed Output Location:", 
                      control = control.DIR_COMBO_BOX, 
                      name = "seedOutputLocation", 
                      type = dtype.STR, 
                      comment = "Output Directory Location where the ROI files for \n"\
                                "the newly created seeds will be present",
                      values = os.getcwd())
        
        self.page.set_sizer()
        parent.get_page_list().append(self)
        
    def get_counter(self):
            return self.counter
            
class ROITimeseries(wx.ScrolledWindow):
    
    def __init__(self, parent, counter = 0):
        import os
        
        wx.ScrolledWindow.__init__(self, parent)
        
        self.counter = counter
        
        self.page = GenericClass(self, "ROI Timeseries")
        
        self.page.add(label="Run ROI Timeseries:", 
                 control=control.CHOICE_BOX, 
                 name='runROITimeseries', 
                 type=dtype.LSTR, 
                 comment="Extract an average timeseries for each ROI \n"\
                         "Required if you wish to run ROI-based SCA", 
                 values=["Off","On"],
                 wkf_switch = True)
        
        self.page.add(label = "ROI Timeseries Output Formats:",
                      control = control.CHECKLIST_BOX,
                      name = "roiTSOutputs",
                      type = dtype.LBOOL,
                      values = ['CSV', 'NUMPY'],
                      comment = "Export ROI timeseries data"
                                "First value = Output .csv \n"
                                "Second value = Output numPy array\n"
                                "Note:- By default 1D and text formats timeseries files are always generated")
        
        self.page.add(label = "ROI Specification File:", 
                      control = control.COMBO_BOX, 
                      name = "roiSpecificationFile", 
                      type = dtype.STR, 
                      comment = "Path to file containing ROI definitions \n"\
                                "For best performance, all ROIs should be in a single file (see User Guide)",
                      values = "/path/to/roi_definitions_file")
        
        self.page.set_sizer()
        parent.get_page_list().append(self)
        
    def get_counter(self):
            return self.counter
        
        
class VOXELTimeseries(wx.ScrolledWindow):
    
    def __init__(self, parent, counter = 0):
        wx.ScrolledWindow.__init__(self, parent)
                
        self.counter = counter
        
        self.page = GenericClass(self, "Voxel Timeseries")
        
        self.page.add(label="Run Voxel Timeseries:", 
                 control=control.CHOICE_BOX, 
                 name='runVoxelTimeseries', 
                 type=dtype.LSTR, 
                 comment="Extract timeseries data for all individual voxels within a mask \n"\
                         "Required if you wish to run voxel-based SCA", 
                 values=["Off","On"],
                 wkf_switch = True)
        
        self.page.add(label = "Voxel Timeseries Output Formats:",
                      control = control.CHECKLIST_BOX,
                      name = "voxelTSOutputs",
                      type = dtype.LBOOL,
                      values = ['CSV', 'NUMPY'],
                      comment = "Export voxel timeseries data"
                                "First value = Output .csv \n"
                                "Second value = Output numPy array\n"
                                "Note:- By default 1D and text formats timeseries files are always generated")
        
        self.page.add(label = "Mask Specification File:", 
                      control = control.COMBO_BOX, 
                      name = "maskSpecificationFile", 
                      type = dtype.STR, 
                      comment = "Path to file containing mask definitions",
                      values = "/path/to/mask_definitions_file")
        
        
        self.page.set_sizer()
        parent.get_page_list().append(self)
        
    def get_counter(self):
            return self.counter
        

class SpatialRegression(wx.ScrolledWindow):
    
    def __init__(self, parent, counter = 0):
        wx.ScrolledWindow.__init__(self, parent)
                
        self.counter = counter
        
        self.page = GenericClass(self, "Spacial Regression")
        
        self.page.add(label="Run Spatial Regression:", 
                 control=control.CHOICE_BOX, 
                 name='runSpatialRegression', 
                 type=dtype.LSTR, 
                 comment="Extract timeseries from existing spatial/ica maps\n"\
                         "Required if you wish to run dual regression", 
                 values=["Off","On"],
                 wkf_switch = True)

        self.page.add(label = "Spatial Pattern Maps Specification File:", 
                      control = control.COMBO_BOX, 
                      name = "spatialPatternMap", 
                      type = dtype.STR, 
                      comment = "Path to file containing the paths to Spatial Pattern maps \n"\
                                "All spatial patterns for one analysis have to be volumes in one 4D file \n"\
                                "(see User Guide)",
                      values = "/path/to/mask_definitions_file")
        
        
        self.page.add(label="Demean Spatial Pattern Maps:", 
                     control=control.CHOICE_BOX, 
                     name='spatialDemean', 
                     type=dtype.BOOL, 
                     values = ["True", "False"],
                     comment="do you want to demean your spatial pattern maps and input data (True / False)")
        
        self.page.set_sizer()
        parent.get_page_list().append(self)
        
    def get_counter(self):
            return self.counter
        
        