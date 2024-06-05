[![bioRxiv](https://img.shields.io/badge/bioRxiv-10.1101/2023.01.15.524100-B31B1B.svg)]([https://doi.org/10.1101/2024.05.29.596416](https://doi.org/10.1101/2024.05.29.596416))

# Systematic genetic characterization of the human PKR kinase domain highlights its functional malleability to escape a viral substrate mimic

This repo provides supplementary code and data for the deep mutational scan of human PKR against the poxvirus pseudosubstrate antagonist vaccinia K3  

We generated a library of single-residue variants in the human protein PKR, then screened this library against a pseudosubstrate antagonist, vaccinia K3.  We identified genetic variants that render PKR nonfunctional in the absence of K3, as well as variants that are resistant or susceptible to K3.  This repo provides the code and results used for the analysis and figures included in the manuscript.  Briefly, our analysis can be divided into three portions: (1) design of primers to generate PKR variants, (2) linking PKR variants to genetic barcodes, and (3) analysis of the PKR library screen against vaccinia K3.  Most all figures were generated from the file `results/barseq/pkr-variant-reads_240228.csv` and Jupyter notebooks for analysis are in the `workflow` directory.  

```
dms_human_pkr
├── data
│   ├── dms_primers - supplemental files for the design of pkr 
│   └── pacbio - supplemental files for PacBio sequencing run
├── dms_primer_design - code to design primers to make PKR variant library
├── results
│   ├── alignparse - output contains codon table linking barcodes to pkr variants
│   ├── barseq - output files of barseq experiment for analysis and figures
│   └── figures - images used for manuscript
├── structure_predictions
│   └── AlphaFold2 - structure predictions used for analysis and images in manuscript
├── supplemental_data - supplemental files for manuscript
│   ├── 1_Oligo-Table.xlsx
│   ├── 2_Variant-Primers.xlsx
│   ├── 3_Plasmid-Table.xlsx
│   └── 4_PKR-Functional-Score-Table.csv
└── workflow - code and environment files used for data analysis and figures
    └── notebooks - Jupyter notebooks used for data analysis and figures
```
