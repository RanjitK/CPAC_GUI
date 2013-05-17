import wx
import wx.html
from ..windows.generic_class import GenericClass
from constants import control, dtype
from ..utils import CharValidator
class Nuisance(wx.html.HtmlWindow):

    def __init__(self, parent, counter  = 0):
        from urllib2 import urlopen
        wx.html.HtmlWindow.__init__(self, parent, style= wx.html.HW_SCROLLBAR_AUTO)
        self.SetStandardFonts()
        
        self.counter = counter
        self.LoadPage('html/nuisance.html')
            
        
#        try:
#            code = urlopen("http://fcp-indi.github.io/docs/user/nuisance.html").code
#            if (code / 100 < 4):
#                self.LoadPage('http://fcp-indi.github.io/docs/user/nuisance.html')
#            else:
#                self.LoadFile('html/nuisance.html')
#        except:
#            self.LoadFile('html/nuisance.html')
            
            
    def get_counter(self):
        return self.counter
            
class NuisanceCorrection(wx.ScrolledWindow):
    
    def __init__(self, parent, counter = 0):
        wx.ScrolledWindow.__init__(self, parent)
                
        import os
        
        self.counter = counter
        
        self.page = GenericClass(self, "Nuisance Correction")
        
        self.page.add(label="Run Nuisance Signal Correction:", 
                 control=control.CHOICE_BOX, 
                 name='runNuisance', 
                 type=dtype.LSTR, 
                 comment="Run Nuisance Signal Correction", 
                 values=["On","Off"],
                 wkf_switch = True)
        
        self.page.add(label="Standard Harvard Oxford Mask:", 
                     control=control.COMBO_BOX, 
                     name='harvardOxfordMask', 
                     type=dtype.STR, 
                     values = os.path.join(os.environ['FSLDIR'], "data/atlases/HarvardOxford/HarvardOxford-sub-maxprob-thr25-2mm.nii.gz"),
                     comment="Standard FSL Anatomical Brain Image")

        self.page.add(label = "Corrections:",
                      control = control.CHECKLISTBOX_COMBO,
                      name = "Corrections",
                      type = dtype.LDICT,
                      values = ['compcor', 'wm','csf','global','pc1','motion','linear','quadratic'],
                      comment = "Select which nuisance signal corrections to apply:\n"\
                                "compcor = CompCor\n"\
                                 "wm = White Matter\n"\
                                 "csf = CSF\n"\
                                 "gm = Gray Matter\n"\
                                 "global = Global Mean Signal\n"\
                                 "pc1 = First Principle Component\n"\
                                 "motion = Motion\n"\
                                 "linear = Linear Trend\n"\
                                 "quadratic = Quadratic Trend")
                    
        self.page.add(label= "Number of Compoenents:",
                      control = control.TEXT_BOX,
                      name = "nComponents",
                      type = dtype.LNUM,
                      values = "5",
                      validator = CharValidator("no-alpha"),
                      comment = "Number of Principle Components to calculate for CompCor (usually 5 or 6)\n"\
                                 "Only for use when 'compcor' is set to 1")
        self.page.set_sizer()
        parent.get_page_list().append(self)
        
    def get_counter(self):
            return self.counter
        

class MedianAngleCorrection(wx.ScrolledWindow):
    
    def __init__(self, parent, counter = 0):
        wx.ScrolledWindow.__init__(self, parent)
                
        self.counter = counter
        
        self.page = GenericClass(self, "Median Angle Correction")
        
        self.page.add(label="Run Median Angle Correction:", 
                 control=control.CHOICE_BOX, 
                 name='runMedianAngleCorrection', 
                 type=dtype.LSTR, 
                 comment="Run Nuisance Signal Correction", 
                 values=["On","Off"],
                 wkf_switch = True)
        
        self.page.add(label= "Target Angle:",
                      control = control.TEXT_BOX,
                      name = "targetAngleDeg",
                      type = dtype.LNUM,
                      values = "90",
                      validator = CharValidator("no-alpha"),
                      comment = "Target angle for median angle correction")
        
        self.page.set_sizer()
        parent.get_page_list().append(self)
        
    def get_counter(self):
            return self.counter