 # script to add PKR metadata

import pandas as pd
import numpy as np

def add_pkr_metadata(df):
    # pkr site
    df['site'] = df.loc[:, 'pkr'].str.split('-').str[-1].str[1:-1] 
    df['site'].replace('', np.nan, inplace=True)
    df['site'] = df.loc[:, 'site'].astype(float)
    
    region_sites = [(255,278),(371,385),(448,455),(480,506)]
    site_map = {}
    for i,n in enumerate(region_sites):
        region_n = i+1
        start = n[0]
        end = n[1]
        while start != end + 1:
            site_map[start] = f'Region {region_n}'
            start = start + 1
    
    df['pkr_regions'] = df.loc[:, 'site'].map(site_map)   
    
    def wt_aa(row):
        """Return the WT residue of PKR variant"""
        variant = row['pkr'].split('-')[-1]
        if variant == "WT" or variant == '':
            return None
        else:
            return variant[0]
    
    def var_aa(row):
        """Return the variant residue of the PKR variant"""
        variant = row['pkr'].split('-')[-1]
        if variant == "WT" or variant == '':
            return None
        else:
            return variant[-1]
    
    df['pkr'].replace(np.nan, '', inplace=True)
    df['wt_aa'] = df.apply(wt_aa, axis=1)
    df['var_aa'] = df.apply(var_aa, axis=1)
    
    # organize variants by AA type
    aa_list = ['H','K','R','D','E','C','M','N','Q','S','T','A','I','L','V','F','W','Y','G','P','*']
    aa_pos = ['H','K','R']
    aa_neg = ['D','E']
    aa_neutral = ['C','N','Q','S','T']
    aa_nonpolar = ['A','I','L','M','V']
    aa_aromatic = ['F','W','Y']
    aa_unique = ['G','P']
    aa_stop = ['*']
    
    full_list = [aa_pos,aa_neg,aa_neutral,aa_nonpolar,aa_aromatic,aa_unique,aa_stop]
    aa_categories = ['Positive Charge','Negative Charge','Polar-Neutral','Non-Polar','Aromatic','Unique','Stop']
    
    aa_dict = {key:value for key,value in zip(aa_categories,full_list)}
    
    # Define a function to map the values
    def map_aa(value):
        for key, values_list in aa_dict.items():
            if value in values_list:
                return key
        return None
    
    # Apply the mapping function to the column
    df['wt_cat'] = df.loc[:, 'wt_aa'].apply(map_aa)
    df['var_cat'] = df.loc[:, 'var_aa'].apply(map_aa)
    
    # positive selection and conserved sites
    # Dar 2005 conserved residues in ISR kinases
    dar_red = [262,263,266,450,480,487,490,495,498,499] # highly conserved
    dar_blue = [267,273,274,273,274,276,278,451,454,481] # well conserved
    dar_map = {site:"Conserved Kinase Residue" for site in dar_red + dar_blue}
    df['isr_kinase_conservation'] = df.loc[:, 'site'].map(dar_map)
    
    # Elde 2009 primate positive selection 
    elde_pos=[6,7,24,44,49,86,122,123,125,139,185,206,224,242,255,259,261,265,275,322,330,336,338,344,351,376,380,462,489,492,496,502,506,516,538]
    elde_map = {site:"Primate Positive Selection" for site in elde_pos}
    df['elde_primate_positive_selection'] = df.loc[:, 'site'].map(elde_map)
    
    # Rothenburg 2009 selection pressure, Figure S3
    # Red=pos sele across vertebrates
    roth_red = [261,269,270,271,272,307,314,322,360,368,375,378,379,382,385,389,394,405,428,448,449,462,471,483,486,488,491,493,500,502,504,505,514,520,524]
    roth_map = {site:"Vertebrate Positive Selection" for site in roth_red}
    df['vertebrate_positive_selection'] = df.loc[:, 'site'].map(roth_map)
    
    # Green = conserved PKR residues among homologs, light=>90%, dark=100%
    roth_90 = [263,267,277,278,283,298,309,315,317,319,365,366,397,401,410,430,437,445,446,451,455,469,474,476,477,490,511,519,523]
    roth_100 = [276,279,281,296,308,312,320,323,327,362,364,367,369,374,377,404,406,407,411,412,413,414,415,416,417,419,420,429,431,432,433,444,445,450,454,457,458,459,465,470,475,480,526]
    roth_conserved = {site:"Conserved PKR Residue" for site in roth_90 + roth_100}
    df['pkr_conservation'] = df.loc[:, 'site'].map(roth_conserved)

    # Jaquet primate positive selection sites
    jaquet_pss_primates = [5,6,24,26,28,49,122,125,139,166,170,180,185,193,206,227,242,255,259,261,265,275,322,330,336,344,351,380,449,489,492,496,502,506,516,525,538,542]
    jaquet_map = {site:"Primate Positive Selection" for site in jaquet_pss_primates}
    df['jaquet_primate_positive_selection'] = df.loc[:, 'site'].map(jaquet_map)
    
    # combine columns
    df['vert_sele_analysis'] = df['vertebrate_positive_selection'].combine_first(df['pkr_conservation'])
    df['elde_primate_sele_analysis'] = df['elde_primate_positive_selection'].combine_first(df['pkr_conservation'])
    df['jaquet_primate_sele_analysis'] = df['jaquet_primate_positive_selection'].combine_first(df['pkr_conservation'])

    return df