import wx
import wx.html
from ..utils.generic_class import GenericClass
from ..utils.constants import control, dtype
from ..utils.validator import CharValidator


class AnatomicalPreprocessing(wx.html.HtmlWindow):

    def __init__(self, parent, counter  = 0):
        from urllib2 import urlopen
        wx.html.HtmlWindow.__init__(self, parent, style= wx.html.HW_SCROLLBAR_AUTO)
        self.SetStandardFonts()
        
        self.counter = counter
        self.LoadPage('html/anat.html')
        
#        try:
#            code = urlopen("http://fcp-indi.github.io/docs/user/anat.html").code
#            if (code / 100 < 4):
#                self.LoadPage('http://fcp-indi.github.io/docs/user/anat.html')
#            else:
#                self.LoadFile('html/anat.html')
#        except:
#            self.LoadFile('html/anat.html')
            
            
    def get_counter(self):
        return self.counter
            
class Anatomical(wx.ScrolledWindow):
    
    def __init__(self, parent, counter = 0):
        wx.ScrolledWindow.__init__(self, parent)
                
        self.counter = counter
        
        self.page = GenericClass(self, "Anatomical Preprocessing")
        self.page.add(label="Gather Anatomical Data:", 
                 control=control.CHOICE_BOX, 
                 name='runAnatomicalDataGathering', 
                 type=dtype.LSTR, 
                 comment="option to fetch anatomical data", 
                 values=["On","Off"])
        
        self.page.add(label= "Run Anatomical Processing",
                 control=control.CHOICE_BOX, 
                 name='runAnatomicalPreprocessing', 
                 type=dtype.LSTR, 
                 comment="option to run anatomical processing", 
                 values=["On","Off"],
                 wkf_switch = True)
        
        self.page.set_sizer()
        parent.get_page_list().append(self)
        
    def get_counter(self):
            return self.counter

class Segmentation(wx.ScrolledWindow):

    
    def __init__(self, parent, counter =0):
        wx.ScrolledWindow.__init__(self, parent)
        import os
        
        self.counter = counter
                
        self.page = GenericClass(self, "Anatomical Segmentation")
        
        self.page.add(label="Run Tissue Segmentation:", 
                 control=control.CHOICE_BOX, 
                 name='runSegmentationPreprocessing', 
                 type=dtype.LSTR, 
                 comment="Run automatic tissue segmentation using fsl fast", 
                 values=["On","Off"],
                 wkf_switch = True)
        
        self.page.add(label= "Path to Priors:",
                 control=control.DIR_COMBO_BOX, 
                 name='prior_path', 
                 type=dtype.STR, 
                 values= os.path.join(os.environ['FSLDIR'], 'data/standard/tissuepriors/$standardResolution'),
                 comment="Tissue Prior Directory")
        
        self.page.add(label= "Prior CSF Tissue Path",
                 control=control.COMBO_BOX, 
                 name='PRIOR_CSF', 
                 type=dtype.STR, 
                 values = '$prior_path/avg152T1_csf_bin.nii.gz',
                 comment="location of your prior CSF tissue file")
        
        self.page.add(label= "Prior Gray Matter Tissue Path",
                 control=control.COMBO_BOX, 
                 name='PRIOR_GRAY', 
                 type=dtype.STR, 
                 values = '$prior_path/avg152T1_gray_bin.nii.gz',
                 comment="location of your prior gray matter tissue file")
                
        self.page.add(label= "Prior White Matter Path",
                 control=control.COMBO_BOX, 
                 name='PRIOR_WHITE', 
                 type=dtype.STR, 
                 values = '$prior_path/avg152T1_white_bin.nii.gz',
                 comment="location of your prior White matter tissue file")
                
        self.page.add(label= "CSF threshold",
                 control=control.TEXT_BOX, 
                 name='cerebralSpinalFluidThreshold', 
                 type=dtype.LNUM, 
                 values = "0.98",
                 validator = CharValidator("no-alpha"),
                 comment="CSF threshold. It can have one value eg: 0.98 or" \
                         "list of values seprated by comma eg: 0.98, 0.95",
                 size=(100,-1))
        
        self.page.add(label= "White matter threshold",
                 control=control.TEXT_BOX, 
                 name='whiteMatterThreshold', 
                 type=dtype.LNUM, 
                 values= "0.98",
                 validator = CharValidator("no-alpha"),
                 comment="White matter threshold. It can have one value eg: 0.98 or"\
                         "list of values seprated by comma eg: 0.98, 0.95")
        
        self.page.add(label = 'Gray matter threshold',
                 control =control.TEXT_BOX,
                 name = 'grayMatterThreshold',
                 type =dtype.LNUM,
                 values= "0.7",
                 validator = CharValidator("no-alpha"),
                 comment= "Gray matter threshold")
        
        self.page.set_sizer()
        parent.get_page_list().append(self)
        
    def get_counter(self):
        return self.counter
    
class Registration(wx.ScrolledWindow):
    def __init__(self, parent, counter = 0):
        wx.ScrolledWindow.__init__(self, parent)
        
        self.counter = counter
                
        self.page = GenericClass(self, "Anatomical Registration")
        
        self.page.add(label="Run Registration:", 
                     control=control.CHOICE_BOX, 
                     name='runRegistrationPreprocessing', 
                     type=dtype.LSTR, 
                     comment="Run anatomical registration to generate anatomical-mni linear and non-linear transforms", 
                     values=["On","Off"],
                     wkf_switch = True)
        
        self.page.add(label="Standard Resolution:", 
                      control=control.CHOICE_BOX, 
                      name='standardResolutionAnat', 
                      type=dtype.STR, 
                      values = ["2mm", "1mm", "3mm"],
                      comment="The resolution (in mm) to which functional images are transformed during registration")
        
        self.page.add(label="Standard Brain only Template (anatomical resolution):", 
                     control=control.COMBO_BOX, 
                     name='standardResolutionBrainAnat', 
                     type=dtype.STR, 
                     values = "$FSLDIR/data/standard/MNI152_T1_${standardResolutionAnat}_brain.nii.gz",
                     comment="Standard FSL Skull Stripped Template. Used as a reference image for anatomical registration")

        self.page.add(label="Standard Template with Skull (anatomical resolution):", 
                     control=control.COMBO_BOX, 
                     name='standardAnat', 
                     type=dtype.STR, 
                     values = "$FSLDIR/data/standard/MNI152_T1_${standardResolutionAnat}.nii.gz",
                     comment="Standard FSL Template with Skull. Used as a reference image for anatomical registration")

        self.page.set_sizer()
        parent.get_page_list().append(self)
        
    def get_counter(self):
        return self.counter
                