#!/bin/bash
for i in data/*"$1.tree"; do
    basename=${i#.tree}
    sed -e 's/[dpcofgs]__//g' < "$i" > "${basename}_norank.tree"
done
