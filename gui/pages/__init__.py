from .anatomical import Anatomical, AnatomicalPreprocessing, Segmentation,  Registration
from .functional_tab import FunctionalPreProcessing, Functional, Scrubbing, AnatToFuncRegistration, FuncToMNIRegistration
from .vmhc import VMHC, VMHCSettings
from .reho import ReHo, ReHoSettings
from .sca import SCA, SCASettings, MultipleRegressionSCA
from .settings import Settings, ComputerSettings, GeneralSettings, DirectorySettings
from .nuisance import Nuisance, NuisanceCorrection, MedianAngleCorrection 
from .centrality import CentralitySettings, Centrality
from .alff import ALFF, ALFFSettings
from .smoothing import Smoothing, SmoothingSettings
from .filtering import Filtering, FilteringSettings
from .timeseries import TimeSeries, ROITimeseries, VOXELTimeseries, SpatialRegression, GenerateSeeds, VerticesTimeSeries
from .group_analysis import GroupAnalysis, GPASettings, BASCSettings, BASC, CWAS, CWASSettings
from .dualreg import DualRegression, DualRegressionOptions


__all__ = ['Anatomical', 'AnatomicalPreprocessing', \
           'Segmentation',  'Registration', 'FunctionalPreProcessing',\
           'Functional', 'Scrubbing','AnatToFuncRegistration, FuncToMNIRegistration',\
           'VMHC', 'VMHCSettings', 'ReHo', 'ReHoSettings', \
           'SCA', 'SCASettings', 'MultipleRegressionSCA'\
           'Settings', 'ComputerSettings', 'GeneralSettings', 'DirectorySettings', \
           'Nuisance', 'NuisanceCorrection', 'MedianAngleCorrection', \
           'CentralitySettings', 'Centrality',\
           'ALFF', 'ALFFSettings',\
           'Smoothing', 'SmoothingSettings',\
           'Filtering', 'FilteringSettings',\
           'TimeSeries', 'ROITimeseries', 'VOXELTimeseries', \
           'SpatialRegression', 'GenerateSeeds', 'VerticesTimeSeries',\
           'GroupAnalysis', 'GPASettings', 'BASCSettings',\
           'BASC', 'CWAS', 'CWASSettings'\
           'DualRegression', 'DualRegressionOptions']