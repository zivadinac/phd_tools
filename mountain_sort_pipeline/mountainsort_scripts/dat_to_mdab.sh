#!/bin/bash

echo "================================ dat_to_mdab.sh $2 ===================================================="
TET_DIR=$5/tet$2
[ ! -d "$TET_DIR" ] && mkdir $TET_DIR

# create tetrode par
NUM=$2
sed "$((NUM+4))q;d" $1.par | awk '{print 64, $1, 50}' >  $TET_DIR/tet${2}.par.$2
sed "$((NUM+4))q;d" $1.par | awk '{$1=""; print $0}' >>  $TET_DIR/tet${2}.par.$2
cat TEMPLATE.par.tet >> $TET_DIR/tet${2}.par.$2

NCHAN=`sed "$((NUM+4))q;d" $ANIMAL_$DAY.par | awk '{print $1}'`
echo $NCHAN > nchan.tmp

cp $1.par $TET_DIR/tet${2}.par

#cp $1.par.$2 $TET_DIR/tet${2}.par.$2

head -$NCHAN geom.csv > $TET_DIR/geom.csv

[ -f "$TET_DIR/tet$2raw.mda" ] && echo "WARNING: raw.mda exists, skip conversion" || python Dat_to_Mda.py $1 $2 $3 $4 $TET_DIR
#python3 Dat_to_Mda.py $1 $2 $3
