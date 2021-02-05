#!/usr/bin/env python3
"""Maps genome nodes to species."""
import csv
from Bio import Phylo
from typing import Dict, Iterator, Callable


def crunch_tax(filename: str) -> Dict[str, str]:
    ret = {}
    with open(filename, "r") as f:
        for line in f:
            (genome_id, tax) = line.split("\t")
            # dpcofgs
            (_, _, _, _, _, _, species) = tax.split(";")
            # Map genus name
            # (s__[A-Z][-a-zA-Z0-9_]+?)_[A-Z] (.*)-> $1 $2
            ret[genome_id] = species
    return ret


def traverse_tree_depth(
    clade: Phylo.BaseTree.Clade, predicate=Callable[[Phylo.BaseTree.Clade], bool]
) -> Iterator[Phylo.BaseTree.Clade]:
    if predicate(clade):
        yield clade
    else:
        for c in clade:
            yield traverse_tree_depth(c)


def map_tree(clade, rev):
    tree = Phylo.read(f"data/{clade}{rev}.tree", "newick")
    tax = crunch_tax(f"data/{clade}_taxonomy_{rev}.tsv")

    # Map representative nodes to species
    for node in traverse_tree_depth(tree.clade, lambda c: c.is_terminal()):
        node.name = tax.get(node.name, node.name)

    Phylo.write(tree, "data/{clade}{rev}_species.tree", "newick")

if __name__ == '__main__':
    # TODO
    pass

