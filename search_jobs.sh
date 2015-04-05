source credentials.sh


if [ -z $2 ]; then
	echo '1st argument missing. What job keywords do you use?'
	exit -1
else
	keywords=$1
fi

if [ -z $2 ]; then
	echo '2nd argument missing. How many job posts to sample?'
	exit -1
else
	sample_size=$2
fi

BASE_URL="https://api.linkedin.com/v1/job-search?oauth2_access_token=$LINKEDIN_TOKEN&keywords=$keywords&sort=R&count=20"

for i in $(seq 0 20 $sample_size); do 
	wget "${BASE_URL}&start=$i" -O data/$i.json
done


