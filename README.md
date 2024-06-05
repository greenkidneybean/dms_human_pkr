# Systematic genetic characterization of the human PKR kinase domain highlights its functional malleability to escape a viral substrate mimic

This repo provides supplementary code and data for the deep mutational scan of human PKR against the poxvirus pseudosubstrate antagonist vaccinia K3  

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
