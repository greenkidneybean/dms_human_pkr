# PyMol Commands

A cheatsheet for PyMol commands used to check AlphaFold2 predicted structures against crystal structures and identify PKR residues close to eIf2α and K3.

## Contents
- "pkr_eif2a" - Object, AlphaFold2 best model of human PKR kinase domain in complex with human eIF2α
- "(pkr)" - Selection /pkr_eif2a//A, PKR kinase domain from "pkr_eif2a" object
- "pkr_k3" - AlphaFold2 best model of human PKR kinase domain in complex with vaccinia (VACV) K3
- "aln_pkr-k3-2-pkr-eif2a" - Alignment, alignment of the PKR kinase domains from "pkr_k3" to "pkr_eif2a"
- "2a1a" - Object PDB 2A1A, crystal structure of PKR kinase domain in complex with eIF2α
- "(2a1a_eif2a)" - Selection /2a1a/A/A, eIF2α from "2a1a" crystal structure
- "aln_2a1a-2-pkr-eif2a" - Alignment, alignment of the PKR kinase domains from "2a1a" to "pkr_eif2a"
- "1luz" - Object PDB 1LUZ, crystal structure of vaccinia (VACV) K3 protein
- "(1luz_k3)" - Selection /1luz/A/A, selection of vaccinia K3 protein
- "aln_1luz-k3-to-2a1a-eif2a" - Alignment, alignment of vaccinia K3 crystal structure to eIF2α crystal structure

## Useful Commands
```
# open file
open AlphaFold2/PKR-Kinase-Domain_VACV-K3/best_model.pdb

# get PDB structure
fetch 2a1a

# rename object
set_name best_model, pkr_k3

# create selection
select pkr, /pkr_k3//A

# reset residue numbering to start at 250
alter (pkr),resi=str(int(resi)+249)

# select PKR residues with branches within 5 angstroms of K3
sele (k3_contacts), br. (/pkr_k3//A) within 5 of (/pkr_k3//B)

# name the residues in the selection
iterate (k3_contacts) and name CA, print (resi, resn)

# sequence alignment
align /2a1a/B/B, /pkr_k3//A

# superimpose similar structures
# similar to "align" but uses different algorithm
super /2a1a/B/B, /pkr_k3//A

# store a view
view 1, store
```
