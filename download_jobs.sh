#! /bin/bash
source credentials.sh

if [ ! -z $1 ]; then
	input=$1
	if [ ! -f $input ]; then
		echo 'file `$input` not exist'
		exit -1
	fi
else
	echo 'Input should be set as 1st argument'
	exit -1
fi

ids=$(<$input)

for id in $ids; do
	echo "Processing $id"
	wget "https://api.linkedin.com/v1/jobs/$id:(description)?oauth2_access_token=$LINKEDIN_TOKEN" -O jobs/$id.json
done
