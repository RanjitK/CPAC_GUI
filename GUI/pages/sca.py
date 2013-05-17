import wx
import wx.html
from ..windows.generic_class import GenericClass
from constants import control, dtype
from ..utils import CharValidator

class SCA(wx.html.HtmlWindow):

    def __init__(self, parent, counter  = 0):
        from urllib2 import urlopen
        wx.html.HtmlWindow.__init__(self, parent, style= wx.html.HW_SCROLLBAR_AUTO)
        self.SetStandardFonts()
        
        self.counter = counter
        
        self.LoadFile('html/sca.html')
        
#        try:
#            code = urlopen("http://fcp-indi.github.io/docs/user/sca.html").code
#            if (code / 100 < 4):
#                self.LoadPage('http://fcp-indi.github.io/docs/user/sca.html')
#            else:
#                self.LoadFile('html/sca.html')
#        except:
#            self.LoadFile('html/sca.html')
            
            
    def get_counter(self):
        return self.counter
    
class SCASettings(wx.ScrolledWindow):
    
    def __init__(self, parent, counter = 0):
        wx.ScrolledWindow.__init__(self, parent)
                
        self.counter = counter
        
        self.page = GenericClass(self, "Seed-based Correlation Analysis (SCA)")
        
        self.page.add(label="Run Seed-based Correlation Analysis (SCA):", 
                     control=control.CHOICE_BOX, 
                     name='runSCA', 
                     type=dtype.LSTR, 
                     comment="Run Seed-based Correlation Analysis", 
                     values=["Off","On"],
                     wkf_switch = True)
        
        self.page.set_sizer()
        parent.get_page_list().append(self)
        
    def get_counter(self):
            return self.counter
        
        
class MultipleRegressionSCA(wx.ScrolledWindow):
    
    def __init__(self, parent, counter = 0):
        wx.ScrolledWindow.__init__(self, parent)
                
        self.counter = counter
        
        self.page = GenericClass(self, "SCA using Multiple Regression")
        
        self.page.add(label="Run SCA using Multiple Regression:", 
                 control=control.CHOICE_BOX, 
                 name='runMultRegSCA', 
                 type=dtype.LSTR, 
                 comment="As an additional option, you can use multiple regression as implemented in\n"
                          "fsl_glm to generate sca maps for each extracted timeseries", 
                 values=["Off","On"],
                 wkf_switch = True)
        
        self.page.add(label="Demean the  TimeSeries:", 
                     control=control.CHOICE_BOX, 
                     name='mrsDemean', 
                     type=dtype.BOOL, 
                     values = ["True", "False"],
                     comment="do you want to demean your timeseries maps and input functional\n"
                             "data (True / False)")
                
        self.page.add(label="Normalize the TimeSeries:", 
                     control=control.CHOICE_BOX, 
                     name='mrsNorm', 
                     type=dtype.BOOL, 
                     values = ["True", "False"],
                     comment="Normalize the timeseries (True / False)")
        
        self.page.set_sizer()
        parent.get_page_list().append(self)
        
    def get_counter(self):
            return self.counter