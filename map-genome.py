#!/usr/bin/env python3
"""Maps genome nodes to species."""
import csv
import re
from Bio import Phylo
from typing import Dict, Iterator, Callable


NEW_GENUS_PATTERN = re.compile('^(s__[A-Z][-a-zA-Z0-9_]+?)_[A-Z] (.+)$')

def crunch_tax(filename: str) -> Dict[str, str]:
    ret = {}
    with open(filename, "r") as f:
        for line in f:
            (genome_id, tax) = line.split("\t")
            # dpcofgs
            (_, _, _, _, _, _, species) = tax.split(";")
            species = species.removesuffix('\n')
            species = NEW_GENUS_PATTERN.sub('\\1 \\2', species)
            # Gotta put the genome_id in due to dupes :(
            ret[genome_id] = f"{species} {genome_id}"
    return ret


def traverse_tree_depth(
    clade: Phylo.BaseTree.Clade, predicate: Callable[[Phylo.BaseTree.Clade], bool]
) -> Iterator[Phylo.BaseTree.Clade]:
    if predicate(clade):
        yield clade
    else:
        for c in clade:
            yield from traverse_tree_depth(c, predicate)


def map_tree(file: str) -> None:
    components = i.removesuffix('.tree').removeprefix('data/').split('_')
    tree = Phylo.read(file, "newick")
    clade = components[0]
    rev = components[1]
    tax = crunch_tax(f"data/{clade}_taxonomy_{rev}.tsv")

    # Map representative nodes to species
    for node in traverse_tree_depth(tree.clade, lambda c: c.is_terminal()):
        node.name = tax.get(node.name, node.name)

    Phylo.write(tree, f"data/{clade}_{rev}_species.tree", "newick")


if __name__ == "__main__":
    import sys
    import glob
    suffix = sys.argv[1]
    for i in glob.glob(f"data/*_{suffix}.tree"):
        map_tree(i)
