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
        
        self.page.add(label="Working Directory:", 
         control=control.DIR_COMBO_BOX, 
         name='workingDirectory', 
         type=dtype.STR, 
         comment="Directory where CPAC should store temporary and intermediate files.")
        
        self.page.add(label="Crash Log Directory:", 
         control=control.DIR_COMBO_BOX, 
         name='crashLogDirectory', 
         type=dtype.STR, 
         comment="Directory where CPAC should write crash logs.")
        
        self.page.add(label="Output Directory:", 
         control=control.DIR_COMBO_BOX, 
         name='outputDirectory', 
         type=dtype.STR, 
         comment="Directory where CPAC should place processed data.")
                
        self.page.add(label="Remove Working Directory:", 
         control=control.CHOICE_BOX, 
         name='removeWorkingDir', 
         type=dtype.BOOL, 
         values = ["False", "True"],
         comment="Truncate Working Directory after subject run. This helps remove the space occupied by intermediate files")
                
        self.page.add(label="Regenerate Outputs Option:", 
         control=control.CHOICE_BOX, 
         name='reGenerateOutputs', 
         type=dtype.BOOL, 
         values = ["True", "False"],
         comment="Regenerates all the outputs for all the subjects and their symlinks")
        
        self.page.set_sizer() 
        parent.get_page_list().append(self)

    def get_counter(self):
        return self.counter

class GeneralSettings(wx.ScrolledWindow):
    
    def __init__(self, parent, counter =0):
        wx.ScrolledWindow.__init__(self, parent)
        
        self.page = GenericClass(self, "General Settings")
        self.counter = counter
                
        self.page.add(label="FSL Directory Path:", 
                 control=control.DIR_COMBO_BOX, 
                 name='FSLDIR', 
                 type=dtype.STR, 
                 values = os.environ['FSLDIR'],
                 comment="Directory where FSL is located. If you have added FSL to your .bashrc file, this will be set automatically")
                
        self.page.add(label= "First Timepoint (start Index):",
                 control=control.INT_CTRL, 
                 name='startIdx', 
                 type=dtype.NUM, 
                 comment="Ignore volumes before this timepoint. Defaults to beginning of timeseries", 
                 values=0)
        
        self.page.add(label= "Last Timepoint (stop Index):",
                 control=control.TEXT_BOX, 
                 name='stopIdx', 
                 type=dtype.NUM, 
                 values= "None",
                 validator = CharValidator("no-alpha"),
                 comment="Ignore volumes after this timepoint. Options are an integer or None (defaults to end of timeseries)")
        
        self.page.add(label= "TR:",
                 control=control.TEXT_BOX, 
                 name='TR', 
                 type=dtype.NUM, 
                 values= "None",
                 validator = CharValidator("no-alpha"),
                 comment="Specify a TR other than what is listen in image headers.Options are an integer or None (defaults to header information)")
        
        self.page.add(label="Create Symbolic Links:", 
                 control=control.CHOICE_BOX, 
                 name='runSymbolicLinks', 
                 type=dtype.BOOL, 
                 comment="Option to Create Symbolic links of the outputs and creates a pretty output structure.\n" 
                         "We suggest you to always put this option ON", 
                 values=["On","Off"])
    
        self.page.set_sizer() 
        parent.get_page_list().append(self)

    def get_counter(self):
        return self.counter

