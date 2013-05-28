import wx
import wx.html
from ..utils.generic_class import GenericClass
from ..utils.constants import control, dtype
from ..utils.validator import CharValidator
import os

class Settings(wx.html.HtmlWindow):
    def __init__(self, parent, counter  = 0):
        from urllib2 import urlopen
        wx.html.HtmlWindow.__init__(self, parent, style= wx.html.HW_SCROLLBAR_AUTO)
        self.SetStandardFonts()
        
        self.counter = counter
        
        self.LoadFile('html/settings.html')
        
#        try:
#            code = urlopen("http://fcp-indi.github.io/docs/user/compute_config.html").code
#            if (code / 100 < 4):
#                self.LoadPage('http://fcp-indi.github.io/docs/user/compute_config.html')
#            else:
#                self.LoadFile('html/settings.html')
#        except:
#            self.LoadFile('html/settings.html')
            
            
    def get_counter(self):
        return self.counter
        


class ComputerSettings(wx.ScrolledWindow):
    def __init__(self, parent, counter =0):
        wx.ScrolledWindow.__init__(self, parent)
        self.counter = counter
        
        self.page = GenericClass(self, "Computer Settings")
        self.page.add(label="Run CPAC on Grid:", 
                 control=control.CHOICE_BOX, 
                 name='runOnGrid', 
                 type=dtype.BOOL, 
                 comment="True = Run on compute cluster, False = Run on non-cluster machine", 
                 values=["False","True"],
                 wkf_switch = True)

        self.page.add(label="FSL Path ", 
                 control=control.DIR_COMBO_BOX, 
                 name='FSLDIR', 
                 type=dtype.STR, 
                 values = os.environ['FSLDIR'],
                 comment="Full path to the FSL version to be used by CPAC.\n\n"
                         "If you have specified an FSL path in your .bashrc file,\n"
                         "this path will be set automatically.")

        self.page.add(label= "Job Scheduler / Resource Manager ",
                 control=control.CHOICE_BOX, 
                 name='resourceManager', 
                 type=dtype.STR, 
                 values = ["SGE", "PBS"],
                 comment="Sun Grid Engine (SGE) or Portable Batch System (PBS)")
        
        self.page.add(label= 'SGE Parallel Environment ', 
                      control= control.TEXT_BOX, 
                      name= 'parallelEnvironment', 
                      type= dtype.STR, 
                      comment='SGE Parallel Environment to use when running CPAC.', 
                      values= 'cpac')
        
        self.page.add(label='SGE Queue ', 
                      control= control.TEXT_BOX, 
                      name='queue', 
                      type= dtype.STR, 
                      comment='SGE Queue to use when running CPAC.', 
                      values = 'all.q')
        
        
        self.page.add(label= "Number of Cores Per Subject ",
                 control=control.INT_CTRL, 
                 name='numCoresPerSubject', 
                 type=dtype.NUM, 
                 comment="Number of cores (on a single machine) or slots on\n" 
                         "a node (cluster/grid) per subject. Slots are cores\n"
                         "on a cluster/grid node.\n\n"
                         "IMPORTANT: Number of Cores Per Subject multiplied\n"
                         "by Number of Subjects to Run Simultaneously must\n"
                         "not be greater than the total number of cores.", 
                 values=1)

        self.page.add(label= "Number of Subjects to Run Simultaneously ",
                 control=control.INT_CTRL, 
                 name='numSubjectsAtOnce', 
                 type=dtype.NUM, 
                 comment="This number depends on computing resources.", 
                 values=2)
                
        
        self.page.set_sizer() 
        parent.get_page_list().append(self)
        
    def get_counter(self):
        return self.counter
        
class DirectorySettings(wx.ScrolledWindow):
    def __init__(self, parent, counter =0):
        wx.ScrolledWindow.__init__(self, parent)
        
        self.page = GenericClass(self, "Output Settings")
        self.counter = counter
        
        self.page.add(label="Working Directory ", 
         control=control.DIR_COMBO_BOX, 
         name='workingDirectory', 
         type=dtype.STR, 
         comment="Directory where CPAC should store temporary and intermediate files.",
         validation_req = False)
        
        self.page.add(label="Crash Log Directory ", 
         control=control.DIR_COMBO_BOX, 
         name='crashLogDirectory', 
         type=dtype.STR, 
         comment="Directory where CPAC should write crash logs.",
         validation_req = False)
        
        self.page.add(label="Output Directory ", 
         control=control.DIR_COMBO_BOX, 
         name='outputDirectory', 
         type=dtype.STR, 
         comment="Directory where CPAC should place processed data.",
         validation_req = False)

        self.page.add(label="Create Symbolic Links ", 
                 control=control.CHOICE_BOX, 
                 name='runSymbolicLinks', 
                 type=dtype.BOOL, 
                 comment="Create a user-friendly, well organized version of the output directory.\n\n"
                         "We recommend all users enable this option.", 
                 values=["On","Off"])
                
        self.page.add(label="Remove Working Directory ", 
         control=control.CHOICE_BOX, 
         name='removeWorkingDir', 
         type=dtype.BOOL, 
         values = ["False", "True"],
         comment="Deletes the contents of the Working Directory after running.\n\n"
                 "This saves disk space, but any additional preprocessing or analysis\n"
                 "will have to be completely re-run.")
                
        self.page.add(label="Regenerate Outputs ", 
         control=control.CHOICE_BOX, 
         name='reGenerateOutputs', 
         type=dtype.BOOL, 
         values = ["True", "False"],
         comment="Uses the contents of the Working Directory to regenerate all outputs\n"
                 "and their symbolic links.\n\n"
                 "Requires an intact Working Directory.")
        
        self.page.set_sizer() 
        parent.get_page_list().append(self)

    def get_counter(self):
        return self.counter

class GeneralSettings(wx.ScrolledWindow):
    
    def __init__(self, parent, counter =0):
        wx.ScrolledWindow.__init__(self, parent)
        
        self.page = GenericClass(self, "Time Series Options")
        self.counter = counter 
                
                
        self.page.add(label= "First Timepoint ",
                 control=control.INT_CTRL, 
                 name='startIdx', 
                 type=dtype.NUM, 
                 comment="First timepoint to include in analysis.\n\nDefault is 0 (beginning of timeseries).", 
                 values=0)
        
        self.page.add(label= "Last Timepoint ",
                 control=control.TEXT_BOX, 
                 name='stopIdx', 
                 type=dtype.NUM, 
                 values= "None",
                 validator = CharValidator("no-alpha"),
                 comment="Last timepoint to include in analysis.\n\nDefault is None (end of timeseries).")
        
        self.page.add(label= "TR ",
                 control=control.TEXT_BOX, 
                 name='TR', 
                 type=dtype.NUM, 
                 values= "None",
                 validator = CharValidator("no-alpha"),
                 comment="Specify the TR at which images were acquired.\n\nDefault is None (TR information is read from image file header)")
        
        
    
        self.page.set_sizer() 
        parent.get_page_list().append(self)

    def get_counter(self):
        return self.counter

