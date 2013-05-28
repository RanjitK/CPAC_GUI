import wx
import wx.html
import os
from ..utils.generic_class import GenericClass
from ..utils.constants import control, dtype
from ..utils.validator import CharValidator

class FunctionalPreProcessing(wx.html.HtmlWindow):
    def __init__(self, parent, counter  = 0):
        from urllib2 import urlopen
        wx.html.HtmlWindow.__init__(self, parent, style= wx.html.HW_SCROLLBAR_AUTO)
        self.SetStandardFonts()
        
        self.counter = counter
        
        self.LoadFile('html/functional.html')
        
#        try:
#            code = urlopen("http://fcp-indi.github.io/docs/user/motion.html").code
#            if (code / 100 < 4):
#                self.LoadPage('http://fcp-indi.github.io/docs/user/motion.html')
#            else:
#                self.LoadFile('html/functional.html')
#        except:
#            self.LoadFile('html/functional.html')
            
            
    def get_counter(self):
        return self.counter
    
class Functional(wx.ScrolledWindow):
    
    def __init__(self, parent, counter = 0):
        wx.ScrolledWindow.__init__(self, parent)
                
        self.counter = counter
        
        self.page = GenericClass(self, "Functional Preprocessing")
        self.page.add(label="Gather Functional Data:", 
                 control=control.CHOICE_BOX, 
                 name='runFunctionalDataGathering', 
                 type=dtype.LSTR, 
                 comment="option to fetch functional data", 
                 values=["On","Off"],
                 wkf_switch = False)
        
        self.page.add(label= "Run Functional Processing:",
                 control=control.CHOICE_BOX, 
                 name='runFunctionalPreprocessing', 
                 type=dtype.LSTR, 
                 comment="option to run functional processing", 
                 values=["On","Off"],
                 wkf_switch = True)
        
        self.page.add(label="Generate Motion Statistics:", 
                 control=control.CHOICE_BOX, 
                 name='runGenerateMotionStatistics', 
                 type=dtype.LSTR, 
                 comment="Generate FD and DVARS motion statistics. Required to run scrubbing, but can also be used as regressors in a GLM", 
                 values=["On","Off"])
        
        self.page.add(label="Generate Friston Motion Statistics:", 
                 control=control.CHOICE_BOX, 
                 name='runFristonModel', 
                 type=dtype.LSTR, 
                 comment="Generate motion statistics based on the 24 parameter Friston model", 
                 values=["On","Off"])
        
        self.page.set_sizer()
        parent.get_page_list().append(self)
        
    def get_counter(self):
            return self.counter

class Scrubbing(wx.ScrolledWindow):
    
    def __init__(self, parent, counter =0):
        wx.ScrolledWindow.__init__(self, parent)
        
        self.counter = counter
                
        self.page = GenericClass(self, "Scrubbing Options")
        
        self.page.add(label="Run Scrubbing ", 
                 control=control.CHOICE_BOX, 
                 name='runScrubbing', 
                 type=dtype.LSTR, 
                 comment="Remove volumes exhibiting excessive motion.", 
                 values=["Off","On"],
                 wkf_switch = True)
                        
        self.page.add(label= "Framewise Displacement (FD) Threshold ",
                 control=control.TEXT_BOX, 
                 name='scrubbingThreshold', 
                 type=dtype.LNUM, 
                 values = "0.2",
                 validator = CharValidator("no-alpha"),
                 comment="Specify the maximum acceptable Framewise Displacement (FD) in millimeters.\n\nAny volume exhibiting FD greater than this value will be removed.",
                 size=(100,-1))
        
        self.page.add(label= "Preceeding Volumes to Remove ",
                 control=control.INT_CTRL, 
                 name='numRemovePrecedingFrames', 
                 type=dtype.NUM, 
                 comment="Number of volumes to remove preceeding a volume with excessive FD.", 
                 values=1)
        
        self.page.add(label= "Subsequent Volumes to Remove ",
                 control=control.INT_CTRL, 
                 name='numRemoveSubsequentFrames', 
                 type=dtype.NUM, 
                 comment="Number of volumes to remove subsequent to a volume with excessive FD.", 
                 values=2)        
        
        self.page.set_sizer()
        parent.get_page_list().append(self)
        
    def get_counter(self):
        return self.counter
    
class AnatToFuncRegistration(wx.ScrolledWindow):
    def __init__(self, parent, counter = 0):
        wx.ScrolledWindow.__init__(self, parent)
        
        self.counter = counter
                
        self.page = GenericClass(self, "Anatomical to Functional Registration")
        
        fsl = os.environ.get('FSLDIR')
        if fsl == None:
            fsl = "$FSLDIR"
        
        
        self.page.add(label="Run Anatomical to Functional Registration:", 
                     control=control.CHOICE_BOX, 
                     name='runAnatomicalToFunctionalRegistration', 
                     type=dtype.LSTR, 
                     comment="Run Anatomical to Functional Registration", 
                     values=["On","Off"],
                     wkf_switch = True)
        
        self.page.add(label="Functional Standard Resolution:", 
                     control=control.CHOICE_BOX, 
                     name='standardResolution', 
                     type=dtype.STR, 
                     values = ["3mm", "2mm", "1mm"],
                     comment="The resolution (in mm) to which functional images are transformed during registration")
        
        self.page.add(label="Standard Brain only Template (functional resolution):", 
                      control=control.COMBO_BOX, 
                      name='standardResolutionBrain', 
                      type=dtype.STR, 
                      values = str(os.path.join(fsl,"data/standard/MNI152_T1_${standardResolution}_brain.nii.gz")),
                      comment="Standard FSL Skull Stripped Template. Used as a reference image for functional registration")
        
        self.page.add(label="Standard Template with Skull (functional resolution):", 
                      control=control.COMBO_BOX, 
                      name='standard', 
                      type=dtype.STR, 
                      values =  str(os.path.join(fsl,"data/standard/MNI152_T1_$standardResolution.nii.gz")),
                      comment="Standard FSL Anatomical Brain Image with Skull")
        
        self.page.set_sizer()
        parent.get_page_list().append(self)
        
    def get_counter(self):
        return self.counter
    
class FuncToMNIRegistration(wx.ScrolledWindow):
    def __init__(self, parent, counter = 0):
        wx.ScrolledWindow.__init__(self, parent)
        
        self.counter = counter
                
        self.page = GenericClass(self, "Functional to MNI Registration")
        
        fsl = os.environ.get('FSLDIR')
        if fsl == None:
            fsl = "$FSLDIR"
        
        self.page.add(label="Run Functional to MNI Registration:", 
                     control=control.CHOICE_BOX, 
                     name='runRegisterFuncToMNI', 
                     type=dtype.LSTR, 
                     comment="Run Functional to MNI Registration. Required for derivatives.", 
                     values=["On","Off"],
                     wkf_switch = True)
        
        self.page.add(label="Standard Identity Matrix:", 
                     control=control.COMBO_BOX, 
                     name='identityMatrix', 
                     type=dtype.STR, 
                     values = str(os.path.join(fsl,"etc/flirtsch/ident.mat")),
                    comment="Matrix with all 1's. Used as a transformation matrix for re-sampling an image by flirt ")
                    
        self.page.add(label="Boundary Based Registration Scheduler:", 
                     control=control.COMBO_BOX, 
                     name='boundaryBasedRegistrationSchedule', 
                     type=dtype.STR, 
                     values = str(os.path.join(fsl,"etc/flirtsch/bbr.sch")),
                     comment="Standard FSL Scheduler used for Boundary Based Registration. Available in FSL 5.0")
     
        self.page.set_sizer()
        parent.get_page_list().append(self)
        
    def get_counter(self):
        return self.counter
