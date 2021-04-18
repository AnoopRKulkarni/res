#!/bin/bash
for i in `ls pandas*.png`
do
base=$(basename $i '.png')
#echo $base'_tr.png'
convert -negate $i $base'_tr.png'
done
