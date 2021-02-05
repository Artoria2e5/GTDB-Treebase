#!/bin/bash

base_url=https://data.gtdb.ecogenomic.org/releases/release95/95.0/
data_files=(
    bac120_r95.tree.gz
    ar122_r95.tree.gz
    bac120_taxonomy_r95.tsv
    ar122_taxonomy_r95.tsv
)

for d in "${data_files[@]}"; do
    if [[ ! -e data/$d ]]; then
        curl --output-dir data -O -- "$base_url$d" || exit 2
    fi
    if [[ $d == *.gz ]]; then
        gzip -d -k "$d"
    fi
done

touch data/data_fetched
