# Spike sorting pipeline based on mountain sort and adapted to JC data formats

This pipeline includes mountainsort4 for automatic spike sorting (adapted from [Igor Gridchyn's](https://github.com/igridchyn) version) and spikeinterface + phy for manual curation of the results.

## Installation

    Install [Anaconda](https://www.anaconda.com/products/individual).

    Create conda virtual environment for mountainsort4:

    ```
    conda create --name ms_clust --file ms_clust_conda_req.txt
    ```

    Create conda virtual environment for spike interface and phy:

    ```
    conda create --name si_phy --file si_phy_conda_req.txt
    ```

## Usage
    To run the mountainsort4 you should use provided script [run_ms_local](mountainsort_scripts/run_ms_local).
    But before running it you should prepare a few files and put them into directory with your data:

##### geom.csv
    Specifies tetrode geometry - usually the same in all cases (for tetrode recording) and should just be copied from here.

##### TEMPLATE.par
    Text file in the following format:
    ```
    channel_nu  num_bits (per datum, 16 for ushort in JC data)
    sampling_interval (im microseconds) egg_sampling_interval (in microseconds)
    num_of_working_tetrodes reference_channel
    for working tetrode:
    num_working_channels channels... i.e:
    4 0 1 2 3 # fist tetrode with all working channels
    2 5 7 # second tetrode with two working channels (5 and 7)
    ```
    See TEMPLATE.par in this folder as an example.

##### BASELIST
    Put names without extension (.dat) of all input files that you wish to be processed.
    You can use (`create_baselist`)[../bin/create_baselist] script if you wish all your files to be processed together.
    
### Running mountainsort4
    Now you should be able to start mountainsort4:

    ```
    conda activate ms_clust
    ./mountainsort_scripts/run_ms_local INPUT_DIR ANIMAL DAY THRESHOLD NUM_CHANNEL
    ```

    Your sorted data will be in `INPUT_DIR/sorted/` directory.
    This directory has results for each tetrode in a separate subdirectory (tet0, tet1...)

### Using phy for manual curation
    To manually curate results you should run phy:

    ```
    conda activate si_phy
    python axona_ms_to_phy.py --sampling_rate SAMPLING_RATE INPUT_DIR/sorted/
    ```

    After this each tetrode will have a phy_export directory in it.
    You should run phy from there, e.g:
    
    ```
    cd INPUT_DIR/sorted/tet0/phy_export
    phy template-gui params.py
    ```

