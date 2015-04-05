#! /bin/bash

if [ ! -z $1 ]; then
	input_dir=$1
else
	echo 'input_dir path required as 1st argument'
	exit -1
fi


if [ ! -z $2 ]; then
	output=$2
	if [ -f $output ]; then
		rm $output
	fi
else
	echo 'output path required as 2nd argument'
	exit -1
fi

if [ ! -z $3 ]; then
	field=$3
else
	echo 'field should be set as 3rd argument'
	exit -1
fi

if [ ! -z $4 ]; then
	multiple=$4
else
	echo 'multiple job flag should be set as 4th argument(0 or 1)'
	exit -1
fi

for path in $(ls $input_dir/*.json); do
	echo $path
	python extract_content.py $path $field $multiple >> $output
done
