import wx
import wx.html
from ..utils.generic_class import GenericClass
from ..utils.constants import control, dtype

class DualRegression(wx.html.HtmlWindow):

    def __init__(self, parent, counter  = 0):
        wx.html.HtmlWindow.__init__(self, parent, style= wx.html.HW_SCROLLBAR_AUTO)
        self.SetStandardFonts()
        
        self.counter = counter
        self.LoadPage('html/dual_reg.html')
            
    def get_counter(self):
        return self.counter

class DualRegressionOptions(wx.ScrolledWindow):
    
    def __init__(self, parent, counter = 0):
        wx.ScrolledWindow.__init__(self, parent)
                
        self.counter = counter
        
        self.page = GenericClass(self, "Dual Regression")
        
        self.page.add(label="Run Dual Regression:", 
                 control=control.CHOICE_BOX, 
                 name='runDualReg', 
                 type=dtype.LSTR, 
                 comment="Run Dual Regression. In Order to run Dual Regression, \n"
                          "You must also run Spatial Regression for the Timeseries Extraction.", 
                 values=["Off","On"],
                 wkf_switch = True)
        
        self.page.add(label="Normalize the  TimeSeries:", 
                     control=control.CHOICE_BOX, 
                     name='drNorm', 
                     type=dtype.BOOL, 
                     values = ["True", "False"],
                     comment="Normalize the timeseries (True / False)")
                

        self.page.set_sizer()
        parent.get_page_list().append(self)
        
    def get_counter(self):
        return self.counter