### Files

stata.do : Manal's original do file
stata_2.do: My changes
stata_data.csv: New dataset
farc_muni.csv: Municipalities where FARC is present, as generated in stata.do

### Changes to dataset

#### FARC Municipalities
Using Manal's do file, I added "FARC" column to indicate if municipality if FARC or not. The list of municipalies can be found in *farc_muni.csv* and it's the list that can be found in
Manal's do file, just under "// DEFINE IF MUN ARE FARC RELATED"

#### post15
I simply implemented what Manal did

#### post13
I did the same as post15 but for 13 as I suggested in the what'sapp group, just in case we want to use it. 

### Do file
Same computations that Manal did, but now without the cleaning part. Also I tried using "diff" package I found online. 
See here on how to use it_ https://mpra.ub.uni-muenchen.de/43943/1/simplifying_the_estimation_of_difference_in_differences_treatment_effects_with_stata.pdf

