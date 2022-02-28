from os.path import join
from os import listdir
from argparse import ArgumentParser
import numpy as np
import pandas as pd


def __make_path(tet, args, ext):
    if args.phy_export:
        return join(args.input_dir, tet, "phy_export", f"{tet}.{ext}")
    else:
        return join(args.input_dir, tet, f"{tet}.{ext}")


args = ArgumentParser()
args.add_argument("input_dir", help="Input directory with 'tet' subdirectories.")
#args.add_argument("output_dir", help="Output directory with phy-processed data.")
args.add_argument("--phy_export", type=bool, default=True, help="If true (default) take data from 'phy_export' dir for each tetrode.")
args = args.parse_args()
#args.input_dir = "/hdr/data/predrag/recordings_raw/jc269/051221/sorted_right/" #tet2/phy_export"
#args.output_dir = "."

tets = listdir(args.input_dir)
srted_tets = sorted(zip([int(tet[3:]) for tet in tets], tets))
tet_nums, tets = zip(*srted_tets)

clus = {tet: np.loadtxt(__make_path(tet, args, "clu"), dtype=int) for tet in tets}
ress = {tet: np.loadtxt(__make_path(tet, args, "res"), dtype=int) for tet in tets}

num_clusters = {tet: max(clu)-1 if len(clu)>0 else 0 for tet, clu in clus.items()}
clu_shifts = dict(zip(num_clusters.keys(), [0, *np.cumsum(list(num_clusters.values())[:-1]).tolist()]))

tet_to_clus = {} # track which clusters come from which tet
clu_merged = []
res_merged = []

for tet, cs in clu_shifts.items():
    res_merged.extend(ress[tet])
    clu = clus[tet].copy()
    clu[clu > 1] += cs # 0-noise, 1-mua so we keep them the same from every tet
    clu_merged.extend(clu)
    tet_to_clus[tet] = np.unique(clu)

srted = sorted(zip(res_merged, clu_merged))
res_merged, clu_merged = zip(*srted)

np.savetxt(join(args.input_dir, "merged.clu"), clu_merged, fmt='%d')
np.savetxt(join(args.input_dir, "merged.res"), res_merged, fmt='%d')

with open(join(args.input_dir, "clu_origin.txt"), "w") as f:
    for tet, clus in tet_to_clus.items():
        clus = map(str, clus)
        f.write(f"{tet} {' '.join(clus)}\n")
