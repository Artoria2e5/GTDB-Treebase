VERSION=r95

all: data/${VERSION}_final.tree

data/data_fetched:
	./get-data.sh

data/species_mapped:
	./map-genome.py "${VERSION}"

data/prefix_trimmed:
	./trim-prefix.sh "${VERSION}_species"

data/final.tree:
	# Aight, idk
