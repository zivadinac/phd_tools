bash dat_to_mdab.sh $ANIMAL_$DAY $TET $NDAT $NCHAN $OUT_DIR		# todo - simultaneously for all tetrodes
TET_DIR=$OUT_DIR/tet$TET
[ -f $TET_DIR/firings.mda ] && echo "WARNING: $TET_DIR/firings.mda exists, omit mountainsort pipeline" || bash mount_sortb.sh $TET $DTHOLD $TET_DIR                 # (5 default, 3,4 try - see cell and ); 4 - less good cells but better rates;
python mountain_to_sgclustb.py $TET $TET_DIR
#python sgclust_to_lfpo.py . $TET 	# replace . with directory containing tet#/ if different from working directory
python sgclust_to_lfpo.py $OUT_DIR $TET 	# replace . with directory containing tet#/ if different from working directory
cp $ANIMAL_$DAY.whl $TET_DIR/tet${TET}.whl
cp  session_shifts.txt $TET_DIR/
if [ $TET == 0 ] && [ ! -f tet0/tet0.spk.0.ORIG ]; then cp $TET_DIR/tet0.spk.0 $TET_DIR/tet0.spk.0.ORIG ; fi
[ ! -f $TET_DIR/tet${TET}.spk.${TET} ] && echo "spk FILE doesn't exist, don't run interpolation" || echo "call ws_interpolate" && ./ws_interpolate `cat nchan.tmp` $TET_DIR/tet${TET}.spk.${TET}; mv test.out $TET_DIR/tet${TET}.spk.0
echo 0 > $TET_DIR/tet${TET}.cluster_shifts
