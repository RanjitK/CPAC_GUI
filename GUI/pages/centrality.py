import wx
import wx.html
from ..windows.generic_class import GenericClass
from ..utils import control, dtype
from ..utils import CharValidator


class Centrality(wx.html.HtmlWindow):

    def __init__(self, parent, counter  = 0):
        from urllib2 import urlopen
        wx.html.HtmlWindow.__init__(self, parent, style= wx.html.HW_SCROLLBAR_AUTO)
        self.SetStandardFonts()
        
        self.counter = counter
        
        self.LoadFile('html/centrality.html')
        
#        try:
#            code = urlopen("http://fcp-indi.github.io/docs/user/centrality.html").code
#            if (code / 100 < 4):
#                self.LoadPage('http://fcp-indi.github.io/docs/user/centrality.html')
#            else:
#                self.LoadFile('html/centrality.html')
#        except:
#            self.LoadFile('html/centrality.html')
            
            
    def get_counter(self):
        return self.counter
            
class CentralitySettings(wx.ScrolledWindow):
    
    def __init__(self, parent, counter = 0):
        wx.ScrolledWindow.__init__(self, parent)
                
        self.counter = counter
        
        self.page = GenericClass(self, "Network Centrality")
        
        self.page.add(label="Run Network Centrality:", 
                 control=control.CHOICE_BOX, 
                 name='runNetworkCentrality', 
                 type=dtype.LSTR, 
                 comment="Calculate network centrality measures", 
                 values=["Off","On"],
                 wkf_switch = True)
        
        self.page.add(label = "Centrality Method Options:",
                      control = control.CHECKLIST_BOX,
                      name = "centralityMethodOptions",
                      type = dtype.LBOOL,
                      values = ['Degree', 'EigenVector'],
                      comment = "Select which centrality measures to calculate\n"\
                                "First Value = Degree Centrality \n Second value = Eigenvector Centrality")
        
        self.page.add(label = "Centrality Weight Options:",
                      control = control.CHECKLIST_BOX,
                      name = "centralityWeightOptions",
                      type = dtype.LBOOL,
                      values = ['Binarized', 'Weighted'],
                      comment = "Specify how connections are defined during graph construction\n"\
                                "First value = Binarized (connection strenth is either 0 or 1)\n"\
                                "Second value = Weighted (connection strength is a correlation value)")
        
        self.page.add(label="Centrality Threshold Options:", 
                     control=control.CHOICE_BOX, 
                     name='correlationThresholdOption', 
                     type=dtype.NUM, 
                     comment="Select what type of threshold is applied to create an adjacency matrix\n"\
                             "0 = Significance threshold (P-value)\n"\
                             "1 = Sparsity threshold (Sparsity value)\n"\
                             "2 = Correlation threshold (Pearson's r)", 
                     values=["0","1", "2"])
        
        self.page.add(label="Correlation Threshold:", 
                     control=control.FLOAT_CTRL, 
                     name='correlationThreshold', 
                     type=dtype.NUM, 
                     comment="Based on the type of threshold selected above, enter the appropriate value\n"\
                             "Significance threshold = P-value\n"\
                             "Sparsity threshold = sparsity value\n"\
                             "Correlation threshold = Pearsons' r value", 
                     values=0.001)
        
        self.page.add(label="Template Specification File:", 
                     control=control.COMBO_BOX, 
                     name='templateSpecificationFile', 
                     type=dtype.STR, 
                     values = "/path/to/file_containing_templates.txt",
                     comment="File containing ROI definitions or masks\n"\
                            "Using ROIs will result in node-based centrality measures\n"\
                            "Using a mask will result in voxel-based centrality measures\n"\
                            "Each line of file contains full path to ROI or mask files\n"\
                            "Example:\n"\
                            "/path/to/template_1.nii.gz\n"\
                            "/path/to/template_2.nii.gz\n"\
                            "/path/to/template_3.nii.gz")
        
        self.page.add(label="Memory Allocated for Degree Centrality:", 
                     control=control.FLOAT_CTRL, 
                     name='memoryAllocatedForDegreeCentrality', 
                     type=dtype.NUM, 
                     comment="Memory allocated for degree centrality in GB\n"\
                              "Note:- If eigen vector is turned on, CPAC will take extra memory to calculate\n"\
                              "eigen vector centrality. This memory is based on size of mask/template used.", 
                     values=2)
        
        
        self.page.set_sizer()
        parent.get_page_list().append(self)
        
    def get_counter(self):
            return self.counter