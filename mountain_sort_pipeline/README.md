# Spike sorting pipeline based on mountain sort and adapted to JC data formats

Pipeline was mainly written by [Igor Gridchyn](https://github.com/igridchyn) and packed by me into an easily usable docker container.

## Installation
    ```
        sudo make
    ```

## Usage
    ******************************************************************************

    Put TEMPLATE.par, TEMPLATE.par.tet and geom.csv into INPUT_DIR, then:

    Run mountain sort in a docker container.

    ******************************************************************************

    ```
    Usage:                                                                                                  
          run_docker_ms INPUT_DIR ANIMAL DAY DTHOLD NCHAN                                                
    ```

#### geom.csv
    Specifies tetrode geometry - the same in all cases and should just be copied from here.

#### TEMPLATE.par
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

#### TEMPLATE.par.tet
    ...

    
