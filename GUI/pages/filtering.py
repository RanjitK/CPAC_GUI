import wx
import wx.html
from ..windows.generic_class import GenericClass
from constants import control, dtype
from ..utils import CharValidator

class Filtering(wx.html.HtmlWindow):

    def __init__(self, parent, counter  = 0):
        from urllib2 import urlopen
        wx.html.HtmlWindow.__init__(self, parent, style= wx.html.HW_SCROLLBAR_AUTO)
        self.SetStandardFonts()
        
        self.counter = counter
        
        self.LoadFile('html/temporal.html')
        
#        try:
#            code = urlopen("http://fcp-indi.github.io/docs/user/temporal.html").code
#            if (code / 100 < 4):
#                self.LoadPage('http://fcp-indi.github.io/docs/user/temporal.html')
#            else:
#                self.LoadFile('html/temporal.html')
#        except:
#            self.LoadFile('html/temporal.html')
            
            
    def get_counter(self):
        return self.counter
            
class FilteringSettings(wx.ScrolledWindow):
    
    def __init__(self, parent, counter = 0):
        wx.ScrolledWindow.__init__(self, parent)
                
        self.counter = counter
        
        self.page = GenericClass(self, "Filtering Settings")
        
        self.page.add(label="Run Temporal Filtering:", 
                 control=control.CHOICE_BOX, 
                 name='runFrequencyFiltering', 
                 type=dtype.LSTR, 
                 comment="Apply Temporal Filtering", 
                 values=["On","Off"],
                 wkf_switch = True)
        
        self.page.add(label = "BandPass Filter Frequency:",
                      control = control.TEXTLISTBOX_COMBO,
                      name = "nuisanceBandpassFreq",
                      type = dtype.LOFL,
                      values = [0.01, 0.1],
                      comment = "First value = Lower bound for a band-pass filter\n"\
                                "Second value = Upper bound for a band-pass filter")

        
        self.page.set_sizer()
        parent.get_page_list().append(self)
        
    def get_counter(self):
            return self.counter