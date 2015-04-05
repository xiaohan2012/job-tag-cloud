#! /bin/bash

if [ ! -z $1 ]; then
	keywords=$1 # url-encoded. Example: natural%20language%20processing
else
	echo 'Keywords should be set as 1st argument in url-encoded format'
	exit -1
fi


if [ ! -z $2 ]; then
	sample_size=$2 # Example: 100
else
	echo 'Job post sample size should be set as 2nd argument'
	exit -1
fi

if [ ! -z $3 ]; then
	output=$3 # Example: nlp_job.png
else
	echo 'Output image path should be set as 3rd argument'
	exit -1
fi

ID_PATH="ids.txt"
JOB_PATH="job_desc.txt"
JOB_CLEANED_PATH="job_desc_cleaned.txt"
JOB_KEYWORDS_PATH="job_keywords.txt"

touch_dir() {
	if [ ! -d $1 ]; then
		mkdir $1
	fi
}

touch_dir data
touch_dir jobs

#search word and gather ids
# ./search_jobs.sh $keywords $sample_size
# ./dump_field.sh data $ID_PATH id 1

# #download job posts
# ./download_jobs.sh $ID_PATH

# #extract job descriptions 
# ./dump_field.sh jobs $JOB_PATH description 0

# #remove HTML tags
# python clean_html.py $JOB_PATH $JOB_CLEANED_PATH

# #extract keywords
# python extract_keywords.py $JOB_CLEANED_PATH > $JOB_KEYWORDS_PATH

# #dump keywords
# python util.py

# #draw wordcloud
# echo "Tag cloud saved to $output"
python tagcloud.py $output
