#!/bin/bash
for i in `ls viz_[5-8]*.png`
do
base=$(basename $i '.png')
#echo $base'_tr.png'
convert -negate $i $base'_tr.png'
done
