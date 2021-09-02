# phd_tools
Some tools needed for daily work in JC lab. To use them just add [bin](./bin) folder to the PATH.

## List of tools

* **bin_to_dat**

    ******************************************************************************

    Convert all .bin files in each given directory to .dat files.

    ******************************************************************************

    ```
    Usage:

    bin_to_dat [OPTION]... DIR1 DIR2 DIR3...

    Options:

            -h display help

            -j MAX-JOBS    process at most MAX-JOBS .bin files in parallel
    ```
* **create_baselist**

    ******************************************************************************
    Create BASELIST file in each given directory.
    ******************************************************************************

    ```
    Usage:

    create_baselist DIR1 DIR2 DIR3...   

    Options:  

            -h display help
    ```

* **docker_helpers**

    Helper scripts for (un)installing docker on different flavours of Linux.
    
* **Axona2dat3_15_128**
    ******************************************************************************
    Axona2dat3_xx v 2.x: 08 March 2012 (PS). Based in original program by JRH.
    ******************************************************************************
    1. Create a .dat (Csicsvari raw data file) from an Axona .bin file
    2. Creates an .axtrak text file containing tracking
    3. Creates a binary .digbin file containing digital input channels and sync inputs.
       .digbin file contains four byes for every data packet. First two bytes are digital inputs.

    Valid arguments - defaults in []
      -outdat: output dat file? 0=no, 1=yes [1]
      -diindat: digital inputs in dat file? 0=no, 1=yes [0]

    Useage: Axona2dat3_xx.exe [axonafile] [OPTIONS]
    
 * **regaamc11**
    ******************************************************************************
    regaamc11 - LFP display written by JC.
    ******************************************************************************
    Usage:
    
    regaamc11 input_file.dat channel_num sampling_interval conf_file.conf 
    1. input_file.dat - binary input file
    2. channel_num - total number of channels in input file
    3. sampling_interval - in microseconds
    4. conf_file.conf - display configuration



    

 

