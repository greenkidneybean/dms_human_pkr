# DMS Primer Design for PKR

Code to generate single-residue PKR variants across 4 windows of interest in the kinase domain, using the  [v2.1 release of dms_primer_design](https://github.com/greenkidneybean/dms_primer_design/releases/tag/v2.1)

The `primer_design.py` requires the input files `pkr_config.yaml`, `pkr_wt.gb`, and `pkr_vector.gb` to design a list of doped primers in the output `.tsv` and `.fa` files.  The designed primers were used to generate a library of single-residue variants attained by a single nucleotide change (or SNP) from the canonical PKR coding sequence (Ensemble ENSG00000055332; CDS EIF2AK2-001). Original inputs are provided in the `input` directory. Variants are generated across "tiles" of the coding sequence that are listed as Features in the `.gb` files and listed under **variant_windows** in the `pkr_config.yaml`.  Note that the variant codons are flanked with synonymous changes to the **vector_seq** file.

## Quick Start
```
# activate environment
cd
conda env create -f environment.yaml
conda activate dms_primer_design_env

# design primers
python primer_design.py input/pkr_config.yaml

# check primers
python primer_check.py input/pkr_config.yaml

# sort primers by length
python primer_sort.py --out output/sorted_primers.tsv output/pkr.tsv
```

## Config File Parameters
- **output_prefix:** (string) The name of the gene of interest  
- **output_path:** (string) Directory where `.tsv` file will be saved  
- **rng_seed:** (integer) Used to seed where synonymous and stop variants are designed  
- **wt_seq:** (string) Path to `.gb` file containing the coding sequence for the gene of interest from which SNP-accesible variants are designed  
- **vector_seq:** (string) Path to alternate `.gb` file containing the coding sequence for the gene of interest.  Can be identical to the wt_seq path, but provides the option to design variants for a wildtype nucleotide sequence that may differ from a codon-optimized nucleotide sequence on the vector plasmid  
- **homology_length:** (integer) Length of homology arms for Gibson Assembly of PCR fragments  
- **max_oligo_length:** (integer) The ideal maximum length for each primer, but will extend if necessary to increase the melting temperature of the primer  
- **fwd_primer_melt_temp:** (integer) Melting temperature of the forward doped primer that generates the variant  
- **rev_primer_melt_temp:** (integer) Melting temperature of the reverse primer for a given tile  
- **mutagenesis_type:** (string) Default is "missense" to generate only SNP-accessible variants, currently no option for saturation mutagenesis
- **variant_windows:** (list of strings) A list of feature names in the `.gb` file that specify where each tile of variants should be made  
- **synonymous_variant_rate:** (floag) Value ranging from 0-1 denoting the percent of synonymous variants, e.g a value of .05 would result in 5% of the designed primers encoding synonymous variants, used to generate control variants  
   **remove_stop_variant_rate:** (float) Value ranging from 0-1 denoting the percent of stop variants removed from primer design, e.g a value of 1.0 would result in all stop variants being excluded from the primer design, used to generate control variants  

## Output Log
```
$ python primer_design.py input/pkr_config.yaml
CONFIGURATION:
output_prefix: pkr
output_path: ./output/
rng_seed: 55
wt_seq: ./input/pkr_wt.gb
vector_seq: ./input/pkr_vector.gb
homology_length: 20
max_oligo_length: 60
fwd_primer_melt_temp: 50
rev_primer_melt_temp: 55
mutagenesis_type: missense
variant_windows: ['pkr_1-1', 'pkr_1-2', 'pkr_1-3', 'pkr_1-4', 'pkr_1-5', 'pkr_2-1', 'pkr_2-2', 'pkr_2-3', 'pkr_3-1', 'pkr_3-2', 'pkr_4-1', 'pkr_4-2', 'pkr_4-3', 'pkr_4-4', 'pkr_4-5']
synonymous_variant_rate: 0.05
remove_stop_variant_rate: 0.9
codon_table: Standard

Total variants: 435
Missense variants: 431
Synonymous variants: 4
Synonymous variant location: [260, 264, 371, 484]
Fraction of stop variants: 4/31
Stop variant location: [275, 376, 453, 480]
Doped variant primers: 196
Variant sub-windows: 14

$ python primer_check.py input/pkr_config.yaml
CONFIGURATION:
output_prefix: pkr
output_path: ./output/
rng_seed: 55
wt_seq: ./input/pkr_wt.gb
vector_seq: ./input/pkr_vector.gb
homology_length: 20
max_oligo_length: 60
fwd_primer_melt_temp: 50
rev_primer_melt_temp: 55
mutagenesis_type: missense
variant_windows: ['pkr_1-1', 'pkr_1-2', 'pkr_1-3', 'pkr_1-4', 'pkr_1-5', 'pkr_2-1', 'pkr_2-2', 'pkr_2-3', 'pkr_3-1', 'pkr_3-2', 'pkr_4-1', 'pkr_4-2', 'pkr_4-3', 'pkr_4-4', 'pkr_4-5']
synonymous_variant_rate: 0.05
remove_stop_variant_rate: 0.9
codon_table: Standard

Predicting variants from file: ./input/pkr_wt.gb
Extracting designed variants from file: ./output/pkr.tsv

Designed primers are missing 27 stop ('*') variants

4 synonymous variants indluded in designed primers:
G264G
V484V
K371K
D260D
```
