# GTDB-Treebase
Script for converting a GTDB database to a treebase format in opentreeoflife.

## What we do now

* Map representative genomes to species
* Map suffixed genus names in species to conventional versions
* Trim off the taxon level prefix &ndash; Actually we can do it in the mapper
* Join up bacteria and archaea at a root for single-file upload

## Why some stuff aren't done yet

### More to conventional (NCBI) names

In theory we could use the `auxillary_files/gtdb_vs_ncbi_*.xlsx` to do a deeper species
mapping, but that is quite risky. Mapping on the higher-level taxa feels pointless too.

## Stuff I really should do

* Instead of the taxonomy tsv, fetch the data from GenBank directly. In other words,
  erase GTDB taxonomy and just use the hot mess. Will make OTU mapping a lot smoother...
