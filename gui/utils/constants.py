def enum(**enums):
    return type('Enum', (), enums)


control = enum(CHOICE_BOX=0, 
               TEXT_BOX=1, 
               COMBO_BOX=2,
               INT_CTRL=3,
               FLOAT_CTRL = 4,
               DIR_COMBO_BOX = 5,
               CHECKLIST_BOX =6,
               LISTBOX_COMBO = 7)

dtype = enum(BOOL=0,
             STR=1,
             NUM=2,
             LBOOL=3,
             LSTR=4,
             LNUM=5,
             LOFL=6,
             COMBO=7,
             LDICT=8) 


substitution_map = {'On': 1,
                    'Off': 0,
                    "Yes":1,
                    "No": 0,
                   'SCA(voxel_based)': 'sca_seed_Z_to_standard_smooth',
                   'SCA(roi_based)':'sca_roi_Z_to_standard_smooth',
                   'SCA(temporal_regression)':'sca_tempreg_maps_z_files_smooth',
                   'ALFF':'alff_Z_to_standard_smooth',
                   'fALFF':'falff_Z_to_standard_smooth',
                   'VMHC':'vmhc_z_score_stat_map',
                   'ReHo':'reho_Z_to_standard_smooth',
                   'Centrality':'centrality_outputs_smoothed',
                   'Dual_Regression':'dr_tempreg_maps_z_files_smooth'
                   }