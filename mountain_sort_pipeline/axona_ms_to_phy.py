from argparse import ArgumentParser
from os.path import join
from os import scandir
import json
import spikeinterface as si
from spikeinterface.extractors  import MdaRecordingExtractor, MdaSortingExtractor
from spikeinterface.exporters import export_to_phy
from spikeinterface.core.waveform_extractor import WaveformExtractor
import matplotlib.pyplot as plt
import spikeinterface.widgets as sw
from joblib import Parallel, delayed


def __write_params_json(path, **params):
    print(params)
    with open(path, "w") as pf:
        json.dump(params, pf)


def __process_tet(tet_dir, sampling_rate):
    print(f"Processing {tet_dir}")
    __write_params_json(join(tet_dir, "params.json"), samplerate=sampling_rate)
    recording = MdaRecordingExtractor(tet_dir, raw_fname="raw_filt.mda")
    recording.annotate(is_filtered=True)
    sorting = MdaSortingExtractor(join(tet_dir, "firings.mda"), sampling_rate)
    wfe = WaveformExtractor.create(recording, sorting, join(tet_dir, "wfe"))
    wfe.set_params()
    wfe.run_extract_waveforms()
    sw.plot_unit_waveforms(wfe)
    plt.savefig(join(tet_dir, "wfe", "waveforms.png"))
    export_to_phy(wfe, join(tet_dir, "phy_export"))
    print(f"Done with {tet_dir}!")


args = ArgumentParser()
args.add_argument("sorted_dir", type=str, help="Directory with sorted data. Has to contain a subdirectory for each tetrode (tet0, tet1...).")
args.add_argument("--sampling_rate", type=int, default=24000, help="Sampling rate of raw data in Hz (default is 24000)")
args.add_argument("--n_jobs", type=int, default=1, help="How many tetrodes to process in parallel (default is 1)")
args = args.parse_args()


tet_dirs = [tet for tet in scandir(args.sorted_dir)]
tet_dirs = list(filter(lambda tet: tet.is_dir() and tet.name.startswith("tet"), tet_dirs))

if args.n_jobs <= 1:
    [__process_tet(tet.path, args.sampling_rate) for tet in tet_dirs]
else:
    Parallel(n_jobs=args.n_jobs)(delayed(__process_tet, args.sampling_rate)(tet.path) for tet in tet_dirs)
