# ChimeraX Commands

A cheatsheet for ChimeraX commands used to make the figure images.

## Contents
- Object #1 - AlphaFold2 best model of human PKR kinase domain in complex with human eIF2α
- Object #2 - AlphaFold2 best model of human PKR kinase domain in complex with vaccinia (VACV) K3

## Style Guide
- colors:
  - white: #d9d5d5
  - PKR: #6dc091 (green)
  - eIF2a: gray
  - K3L: #786bac (purple)
- lighting depthCue False
- surface images:
  - lighting soft
  - no shadows
  - graphics silhouettes false
  - surface resolution 5.5
- cartoon images:
  - preset cylinders
  - graphics silhouettes true
- dashed outlines of contact sites: I selected sites within 5 Angstroms of PKR, colored the selection to contrast with the rest of the PKR kinase domain, saved an image using the "flat" graphics setting, imported to Adobe Illustrator to create a dashed outline of the contact site to overlay on other structural images

## Useful Commands
```
hide #1/A cartoon
show #1/A surface
color #1/A #6dc091 surface

# rename residues
renumber #1/A:1 start 250

# save view
view name 1; turn y 180, view name 2; view 1

# select residues within 5 Angstroms
name eif2a_contacts #1/B :< 5

# select zone
select zone #1/B 5 #1/A residues true

# list residues in zone
info residues sel

# stylize atoms
style sel stick; show sel atoms

# measure distance
distance #2/A:455@CA #2/B:47@CA

# align structures
mm

# show sequence: Tools > Sequence > Show Sequence Viewer

# color gradient
rainbow #2/B pallette BuPu

# alphafold2 prediction coloring
color bfactor #1 palette alphafold

# save image
save file.png width 900 height 900 transparentBackground true supersample 10

# movie
movie record supersample 3; crossfade; transparency #2/B:6-88 50 surface; wait 30; turn y 2 180; wait 180; crossfade; transparency #2/B:6-88 0 surface; wait 30; movie encode file.mp4
```

## Code Snippets for Figures
```
# pkr windows, surface
color #2/A #6dc091 surface; color #2/A:255-278 #ffb000 surface; color #2/A:371-385 #fe6100 surface; color #2/A:448-455 #dc267f surface; color #2/A:480-506 #7b215a surface


# pkr windows, cartoon
color #2/A #6dc091 cartoon; color #2/A:255-278 #ffb000 cartoon; color #2/A:371-385 #fe6100 cartoon; color #2/A:448-455 #dc267f cartoon; color #2/A:480-506 #7b215a cartoon

# positive selection sites
color #2/A #6dc091 surface; color #2/A:261,269,270,271,272,307,314,322,360,368,375,378,379,382,385,389,394,405,428,448,449,462,471,483,486,488,491,493,500,502,504,505,514,520,524 #E62929 surface
```
