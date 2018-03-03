if [ "$#" -ne 1 ]; then
	echo "Need name of shape"
	exit;
fi

echo "Removing contents of slices folder"
rm -rf slices; mkdir slices
python3 src/stl-to-voxel/stltovoxel.py inputs/"$1".stl slices/slice.png
python3 src/sum_slices.py "$1"
