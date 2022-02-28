help()
{
    echo "Usage:"
    echo "      phy_clu_res SORTED_DIR"
    echo "Convert phy output in SORTED_DIR to '.clu'-'.res' format and merge result from all tetrodes."
    echo "SORTED_DIR should have a dir for each tetrode with a 'phy_export' subdir inside it ('tet0/phy_export/ etc.'):"
    printf "\n"
    echo "Options:"
    echo "      -h display help"
}

while getopts ":hj:" option; do
   case $option in
      h)
         help
         exit;;
   esac
done

if [ "$#" == 0 ]; then
    echo "Please provide directory with sorted data."
    help
    exit
fi 

conda activate si_phy

python phy_to_clu_res.py $1
python merge_tetrodes.py $1

conda deactivate
