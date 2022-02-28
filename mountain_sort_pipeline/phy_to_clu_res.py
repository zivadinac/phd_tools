from os import listdir
from os.path import join
from argparse import ArgumentParser
import numpy as np
import pandas as pd

args = ArgumentParser()
args.add_argument("input_dir", help="Input directory with phy-processed data.")
args = args.parse_args()
# args.input_dir = "/hdr/data/predrag/recordings_raw/jc269/051221/sorted_right/"

for tet in listdir(args.input_dir):
    phy_dir = join(args.input_dir, tet, "phy_export")

    cluster_groups = pd.read_csv(join(phy_dir, "cluster_group.tsv"), sep="\t")

    spike_times = np.load(join(phy_dir, "spike_times.npy"))
    spike_clusters = np.load(join(phy_dir, "spike_clusters.npy"))

    # remove spikes from unsorted clusters
    unsorted_clusters = cluster_groups[cluster_groups["group"] == "unsorted"]["cluster_id"].tolist()
    for usc in unsorted_clusters:
        inds = spike_clusters == usc
        spike_clusters[inds] = -1
        spike_times[inds] = -1
    spike_clusters = spike_clusters[spike_clusters != -1]
    spike_times = spike_times[spike_times != -1]
    assert len(spike_clusters) == len(spike_times)
    clu = spike_clusters.copy()

    # mark all noise spikes with 0
    noise_clusters = cluster_groups[cluster_groups["group"] == "noise"]["cluster_id"].tolist()
    for c in noise_clusters:
        clu[spike_clusters == c] = 0

    # mark all mua spikes with 1
    mua_clusters = cluster_groups[cluster_groups["group"] == "mua"]["cluster_id"].tolist()
    for c in mua_clusters:
        clu[spike_clusters == c] = 1

    # good clusters are from 2 onwards
    good_clusters = cluster_groups[cluster_groups["group"] == "good"]["cluster_id"].tolist()
    for i,c in enumerate(good_clusters):
        clu[spike_clusters == c] = i + 2

    np.savetxt(join(phy_dir, f"{tet}.res"), spike_times, fmt="%i")
    np.savetxt(join(phy_dir, f"{tet}.clu"), clu, fmt="%i")
    print(f"Finished converting {tet} with {len(np.unique(clu))} clusters.")
