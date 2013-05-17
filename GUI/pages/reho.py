import wx
import wx.html
from ..windows.generic_class import GenericClass
from ..utils import control, dtype
from ..utils import CharValidator
class ReHo(wx.html.HtmlWindow):

    def __init__(self, parent, counter  = 0):
        from urllib2 import urlopen
        wx.html.HtmlWindow.__init__(self, parent, style= wx.html.HW_SCROLLBAR_AUTO)
        self.SetStandardFonts()
        
        self.counter = counter
        self.LoadFile('html/reho.html')
        
#        try:
#            code = urlopen("http://fcp-indi.github.io/docs/user/reho.html").code
#            if (code / 100 < 4):
#                self.LoadPage('http://fcp-indi.github.io/docs/user/reho.html')
#            else:
#                self.LoadFile('html/reho.html')
#        except:
#            self.LoadFile('html/reho.html')
            
            
    def get_counter(self):
        return self.counter
            
class ReHoSettings(wx.ScrolledWindow):
    
    def __init__(self, parent, counter = 0):
        wx.ScrolledWindow.__init__(self, parent)
                
        self.counter = counter
        
        self.page = GenericClass(self, "ReHo Settings")
        
        self.page.add(label="Run Regional Homogeneity (ReHo):", 
                 control=control.CHOICE_BOX, 
                 name='runReHo', 
                 type=dtype.LSTR, 
                 comment="Calculate Regional Homogeneity", 
                 values=["On","Off"],
                 wkf_switch = True)
        
        
        self.page.add(label="Cluster Size:", 
                     control=control.CHOICE_BOX, 
                     name='clusterSize', 
                     type=dtype.NUM, 
                     comment="# Cluster size (number of neighboring voxels)\n"
                             "Options are 7, 19, and 27", 
                     values=["27","19", "7"])
        
        self.page.set_sizer()
        parent.get_page_list().append(self)
        
    def get_counter(self):
            return self.counter