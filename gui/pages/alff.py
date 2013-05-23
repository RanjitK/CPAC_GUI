import wx
import wx.html
from ..utils.generic_class import GenericClass
from ..utils.constants import control, dtype
from ..utils.validator import CharValidator

class ALFF(wx.html.HtmlWindow):

    def __init__(self, parent, counter  = 0):
        from urllib2 import urlopen
        wx.html.HtmlWindow.__init__(self, parent, style= wx.html.HW_SCROLLBAR_AUTO)
        self.SetStandardFonts()
        
        self.counter = counter
        
        self.LoadFile('html/alff.html')
        
#        try:
#            code = urlopen("http://fcp-indi.github.io/docs/user/alff.html").code
#            if (code / 100 < 4):
#                self.LoadPage('http://fcp-indi.github.io/docs/user/alff.html')
#            else:
#                self.LoadFile('html/alff.html')
#        except:
#            self.LoadFile('html/alff.html')
            
            
    def get_counter(self):
        return self.counter
            
class ALFFSettings(wx.ScrolledWindow):
    
    def __init__(self, parent, counter = 0):
        wx.ScrolledWindow.__init__(self, parent)
                
        self.counter = counter
        
        self.page = GenericClass(self, "ALFF and fALFF Options")
        
        self.page.add(label="Calculate ALFF and fALFF ", 
                 control=control.CHOICE_BOX, 
                 name='runALFF', 
                 type=dtype.LSTR, 
                 comment="Calculate ALFF and fALFF for all voxels.", 
                 values=["On","Off"],
                 wkf_switch = True)
        
        self.page.add(label= "fALFF High-Pass Cutoff ",
                 control=control.TEXT_BOX, 
                 name='highPassFreqALFF', 
                 type=dtype.LNUM, 
                 values= "0.01",
                 validator = CharValidator("no-alpha"),
                 comment="Frequency cutoff (in Hz) for the high-pass filter used when calculating fALFF.")
        
        self.page.add(label= "fALFF Low-Pass Cutoff ",
                 control=control.TEXT_BOX, 
                 name='lowPassFreqALFF', 
                 type=dtype.LNUM, 
                 values= "0.1",
                 validator = CharValidator("no-alpha"),
                 comment="Frequency cutoff (in Hz) for the low-pass filter used when calculating fALFF")
        
        self.page.set_sizer()
        parent.get_page_list().append(self)
        
    def get_counter(self):
            return self.counter