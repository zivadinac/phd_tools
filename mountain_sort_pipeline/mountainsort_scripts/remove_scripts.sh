input_dir=${1:-/usr/input/}
scripts_dir=${2:-/usr/bin/mountainsort_scripts/}

for f in $(ls $scripts_dir); do
    rm $input_dir$(basename $f)
done
