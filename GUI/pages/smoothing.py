import wx
import wx.html
from ..windows.generic_class import GenericClass
from constants import control, dtype
from ..utils import CharValidator

class Smoothing(wx.html.HtmlWindow):

    def __init__(self, parent, counter  = 0):
        from urllib2 import urlopen
        wx.html.HtmlWindow.__init__(self, parent, style= wx.html.HW_SCROLLBAR_AUTO)
        self.SetStandardFonts()
        
        self.counter = counter
        self.LoadFile('html/smoothing.html')
        
#        try:
#            code = urlopen("http://fcp-indi.github.io/docs/user/smoothing.html").code
#            if (code / 100 < 4):
#                self.LoadPage('http://fcp-indi.github.io/docs/user/smoothing.html')
#            else:
#                self.LoadFile('html/smoothing.html')
#        except:
#            self.LoadFile('html/smoothing.html')
            
            
    def get_counter(self):
        return self.counter
            
class SmoothingSettings(wx.ScrolledWindow):
    
    def __init__(self, parent, counter = 0):
        wx.ScrolledWindow.__init__(self, parent)
                
        self.counter = counter
        
        self.page = GenericClass(self, "Smoothing Settings")
        
        self.page.add(label= "Gaussian Kernel Width (in mm):",
                 control=control.TEXT_BOX, 
                 name='fwhm', 
                 type=dtype.LNUM, 
                 values= "4",
                 validator = CharValidator("no-alpha"),
                 comment="Width (FWHM, in mm) of the Gaussian kernel used for spatial smoothing")
        
        self.page.set_sizer()
        parent.get_page_list().append(self)
        
    def get_counter(self):
            return self.counter