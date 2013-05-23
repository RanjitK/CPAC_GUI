import wx
import wx.html
from ..utils.generic_class import GenericClass
from ..utils.constants import control, dtype
from ..utils.validator import CharValidator

class VMHC(wx.html.HtmlWindow):

    def __init__(self, parent, counter  = 0):
        from urllib2 import urlopen
        wx.html.HtmlWindow.__init__(self, parent, style= wx.html.HW_SCROLLBAR_AUTO)
        self.SetStandardFonts()
        
        self.counter = counter
        
        self.LoadFile('html/vmhc.html')
        
#        try:
#            code = urlopen("http://fcp-indi.github.io/docs/user/vmhc.html").code
#            if (code / 100 < 4):
#                self.LoadPage('http://fcp-indi.github.io/docs/user/vmhc.html')
#            else:
#                self.LoadFile('html/vmhc.html')
#        except:
#            self.LoadFile('html/vmhc.html')
            
            
    def get_counter(self):
        return self.counter
            
class VMHCSettings(wx.ScrolledWindow):
    
    def __init__(self, parent, counter = 0):
        wx.ScrolledWindow.__init__(self, parent)
                
        self.counter = counter
        
        self.page = GenericClass(self, "VMHC Settings")
        
        self.page.add(label="Voxel-mirrored Homotopic Connectivity (VMHC):", 
                 control=control.CHOICE_BOX, 
                 name='runVMHC', 
                 type=dtype.LSTR, 
                 comment="Calculate VMHC for all gray matter voxels", 
                 values=["On","Off"],
                 wkf_switch = True)
        
        self.page.add(label="Symmetric Brain only Template:", 
         control=control.COMBO_BOX, 
         name='brainSymmetric', 
         type=dtype.STR, 
         values = "$FSLDIR/data/standard/MNI152_T1_2mm_brain_symmetric.nii.gz",
         comment="Symmetric template. MUST BE DOWNLOADED AS PART OF cpac_resources.tgz (see User Guide)")
        
        self.page.add(label="Symmetric Template with Skull:", 
         control=control.COMBO_BOX, 
         name='symmStandard', 
         type=dtype.STR, 
         values = "$FSLDIR/data/standard/MNI152_T1_2mm_symmetric.nii.gz",
         comment="Symmetric skull stripped template. MUST BE DOWNLOADED AS PART OF cpac_resources.tgz (see User Guide)")

        self.page.add(label="Dilated Symmetric Brain Mask:", 
         control=control.COMBO_BOX, 
         name='twommBrainMaskDiluted', 
         type=dtype.STR, 
         values = "$FSLDIR/data/standard/MNI152_T1_2mm_brain_mask_symmetric_dil.nii.gz",
         comment="FSL Dilated symmetric brain mask used by VMHC.")
        
        self.page.add(label="FLIRT configuration file:", 
         control=control.COMBO_BOX, 
         name='configFileTwomm', 
         type=dtype.STR, 
         values = "$FSLDIR/etc/flirtsch/T1_2_MNI152_2mm.cnf",
         comment="FSL FLIRT Configuration file in 2mm. Required by VMHC.")
        
        
        self.page.set_sizer()
        parent.get_page_list().append(self)
        
    def get_counter(self):
            return self.counter