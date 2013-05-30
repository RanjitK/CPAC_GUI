import wx
import wx.html
import os
from ..utils.generic_class import GenericClass
from ..utils.constants import control, dtype
from ..utils.validator import CharValidator


class TimeSeries(wx.html.HtmlWindow):

    def __init__(self, parent, counter=0):
        from urllib2 import urlopen
        wx.html.HtmlWindow.__init__(
            self, parent, style=wx.html.HW_SCROLLBAR_AUTO)
        self.SetStandardFonts()

        self.counter = counter
        self.LoadFile('html/tse.html')

#        try:
#            code = urlopen("http://fcp-indi.github.io/docs/user/tse.html").code
#            if (code / 100 < 4):
#                self.LoadPage('http://fcp-indi.github.io/docs/user/tse.html')
#            else:
#                self.LoadFile('html/tse.html')
#        except:
#            self.LoadFile('html/tse.html')

    def get_counter(self):
        return self.counter


class GenerateSeeds(wx.ScrolledWindow):

    def __init__(self, parent, counter=0):

        wx.ScrolledWindow.__init__(self, parent)

        self.counter = counter

        self.page = GenericClass(self, "Define New Seeds")

        self.page.add(label="Use Seed in Analysis:", 
         control=control.CHECKLIST_BOX, 
         name='useSeedInAnalysis', 
         type=dtype.LNUM, 
         comment="use the seeds specified in seedSpecificationFile in the following analysis \n"\
                 "1 = use in roi timeseries extraction \n"\
                 "2 = use in voxel timeseries extraction \n"\
                 "3 = use in network centrality \n"\
                 "users can specify a combination of these options",
         values=[ 'None', 'ROI Timeseries', 'Voxel Timeseries', 'Network Centrality'],
         size = (180,80),
         validation_req = False)

        self.page.add(label="Seed Specification File ",
                      control=control.COMBO_BOX,
                      name="seedSpecificationFile",
                      type=dtype.STR,
                      comment="If you wish to specify new seeds (for use in Time Series Extraction and/or Seed-based Correlation Analysis), this field should contain the full path to a text file containing seed definitions.\n\nIf you do not wish to specify new seeds, this field should be set to None.\n\nSeeds are defined by providing a seed label number, x/y/z coordinates in MNI space, seed radius (in mm), and resolution.\n\nExample:\n1 -28 -40 -12 2 3mm\n2 -4 48 24 3 2mm\n\nIf multiple seeds are specified with the same resolution, they will be grouped into a single file containing multiple seeds, with the values within each seed ROI set to the seed label number.\n\nNote that CPAC does not check for overlapping seeds. In the event that a voxel is present in multiple seeds defined here, the value of that voxel will be set to the sum of the two seed label numbers (effectively resulting in a new seed). Users should confirm the seeds they define do not overlap before running CPAC.",
                      values="None")

        self.page.add(label="Seed Output Directory ",
                      control=control.DIR_COMBO_BOX,
                      name="seedOutputLocation",
                      type=dtype.STR,
                      comment="Directory where CPAC should write the NIfTI file for new seeds.",
                      values=os.getcwd())


        self.page.set_sizer()
        parent.get_page_list().append(self)

    def get_counter(self):
            return self.counter


class ROITimeseries(wx.ScrolledWindow):

    def __init__(self, parent, counter=0):
        import os

        wx.ScrolledWindow.__init__(self, parent)

        self.counter = counter

        self.page = GenericClass(self, "ROI Average Time Series Extraction Options")

        self.page.add(label="Extract ROI Average Time Series ",
                      control=control.CHOICE_BOX,
                      name='runROITimeseries',
                      type=dtype.LSTR,
                      comment="Extract the average time series of one or more ROIs/seeds. Must be enabled if you wish to run Seed-based Correlation Analysis.",
                      values=["Off", "On"],
                      wkf_switch=True)

        self.page.add(label="ROI Specification File ",
                      control=control.COMBO_BOX,
                      name="roiSpecificationFile",
                      type=dtype.STR,
                      comment="Full path to a text file containing a list ROI files.\n\nEach line in this file should be the path to a NIfTI file containing one or more ROIs.\n\nIf you only wish to extract time series for newly defined spherical seed ROIs, set this field to None.",
                      values="None")

        self.page.add(label="Output Options ",
                      control=control.CHECKLIST_BOX,
                      name="roiTSOutputs",
                      type=dtype.LBOOL,
                      values=['CSV', 'NUMPY'],
                      comment="By default, extracted time series are written as both a text file and a 1D file. Additional output formats are as a .csv spreadsheet or a Numpy array.")

        self.page.set_sizer()
        parent.get_page_list().append(self)

    def get_counter(self):
            return self.counter


class VOXELTimeseries(wx.ScrolledWindow):

    def __init__(self, parent, counter=0):
        wx.ScrolledWindow.__init__(self, parent)

        self.counter = counter

        self.page = GenericClass(self, "ROI Voxelwise Time Series Extraction Options")

        self.page.add(label="Extract ROI Voxelwise Time Series ",
                      control=control.CHOICE_BOX,
                      name='runVoxelTimeseries',
                      type=dtype.LSTR,
                      comment="Extract the time series of all voxels within one or more ROIs/seeds.",
                      values=["Off", "On"],
                      wkf_switch=True)

        self.page.add(label="Output Options ",
                      control=control.CHECKLIST_BOX,
                      name="voxelTSOutputs",
                      type=dtype.LBOOL,
                      values=['CSV', 'NUMPY'],
                      comment="By default, extracted time series are written as both a text file and a 1D file. Additional output formats are as a .csv spreadsheet or a Numpy array.")

        self.page.add(label="ROI Specification File ",
                      control=control.COMBO_BOX,
                      name="maskSpecificationFile",
                      type=dtype.STR,
                      comment="Full path to a text file containing a list ROI files.\n\nEach line in this file should be the path to a NIfTI file containing a single ROI.\n\nIf you only wish to extract time series for newly defined spherical seed ROIs, set this field to None.",
                      values="None")

        self.page.set_sizer()
        parent.get_page_list().append(self)

    def get_counter(self):
            return self.counter


class SpatialRegression(wx.ScrolledWindow):

    def __init__(self, parent, counter=0):
        wx.ScrolledWindow.__init__(self, parent)

        self.counter = counter

        self.page = GenericClass(self, "Spacial Regression")

        self.page.add(label="Run Spatial Regression:",
                      control=control.CHOICE_BOX,
                      name='runSpatialRegression',
                      type=dtype.LSTR,
                      comment="Extract timeseries from existing spatial/ica maps\n"
                      "Required if you wish to run dual regression",
                      values=["Off", "On"],
                      wkf_switch=True)

        self.page.add(label="Spatial Pattern Maps Specification File:",
                      control=control.COMBO_BOX,
                      name="spatialPatternMaps",
                      type=dtype.STR,
                      comment="Path to file containing the paths to Spatial Pattern maps \n"
                      "All spatial patterns for one analysis have to be volumes in one 4D file \n"
                      "(see User Guide)",
                      values="/path/to/mask_definitions_file")

        self.page.add(label="Demean Spatial Pattern Maps:",
                      control=control.CHOICE_BOX,
                      name='spatialDemean',
                      type=dtype.BOOL,
                      values=["True", "False"],
                      comment="do you want to demean your spatial pattern maps and input data (True / False)")

        self.page.set_sizer()
        parent.get_page_list().append(self)

    def get_counter(self):
            return self.counter


class VerticesTimeSeries(wx.ScrolledWindow):

    def __init__(self, parent, counter=0):
        wx.ScrolledWindow.__init__(self, parent)

        self.counter = counter

        self.page = GenericClass(self, "Vertices Timeseries")

        self.page.add(label="Run Surface Registration:",
                      control=control.CHOICE_BOX,
                      name='runSurfaceRegistraion',
                      type=dtype.LSTR,
                      comment="Register timeseries data to a surface model built by FreeSurfer.\n"
                      "Required to run vertex timeseries extraction. CPAC currently doesn't\n"
                      "fully support surface extraction. Not Recommended.",
                      values=["Off", "On"],
                      wkf_switch=True)

        self.page.add(label="Recon Subject Directory:",
                      control=control.DIR_COMBO_BOX,
                      name="reconSubjectsDirectory",
                      type=dtype.STR,
                      comment="Directory where FreeSurfer outputs surface data.\n"
                      "This should be the same as SUBJECTS_DIR in .bashrc",
                      values=os.getcwd())

        self.page.add(label="Run Vertices Timeseries:",
                      control=control.CHOICE_BOX,
                      name='runVerticesTimeSeries',
                      type=dtype.LSTR,
                      comment="Extract timeseries data for surface vertices.CPAC currently doesn't\n"
                      "fully support surface extraction. Not Recommended.",
                      values=["Off", "On"])

        self.page.add(label="Vertices Timeseries Output Formats:",
                      control=control.CHECKLIST_BOX,
                      name="verticesTSOutputs",
                      type=dtype.LBOOL,
                      values=['CSV', 'NUMPY'],
                      comment="Export vertices timeseries data\n"
                      "First value = Output .csv \n"
                      "Second value = Output numPy array\n")

        self.page.set_sizer()
        parent.get_page_list().append(self)

    def get_counter(self):
            return self.counter
