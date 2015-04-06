# LinkedIn Job Tag Cloud Generator

A small keyword cloud generator for job search result


## What is it?

Python-written Command line tool that:

1. Extract keywords from [LinkedIn job post](https://developer.linkedin.com/docs/rest-api) via [AlchemyAPI](http://www.alchemyapi.com/)
2. Generates tag cloud graphics using [Python word cloud](https://github.com/amueller/word_cloud)

## Demo

The tag cloud for `natural language processing`:

![nlp jobs](http://www.cs.helsinki.fi/u/hxiao/nlp_jobs.png)

The tag cloud for `machine learning`:

![nlp jobs](http://www.cs.helsinki.fi/u/hxiao/ml.png)


## Usage

You need to get OAuth authorization tokens from both *LinkedIn* and *AlchemyAPI* in order to get the job post and extract keywords respectively.


### OAuth for LinkedIn and AlchemyAPI

**LinkedIn:**

Go to [LinkedIn REST console](https://apigee.com/console/linkedin), click the `Authetication` dropdown menu and choose `OAuth 2`. Then make some request and you will see the token string in the request parameter.

Last, set the token variable in `credential.sh`.

**AlchemyAPI:**

Register for an [API key ](http://www.alchemyapi.com/api/register.html) if you don't have one. And follow the [Alchemy Python SDK setup](http://www.alchemyapi.com/developers/getting-started-guide/using-alchemyapi-with-python) to set the OAuth token

### Run the program

```
./pipeline.sh {job_query_words} {job_post_sample_size} {output}
```

1. `job_query_words`: url-encoded job search query, such as `natural%20language%20processing`
2. `job_post_sample_size`: how many job posts do you want to sample
3. `output`: the output path for the tag cloud


## Note:
1. For free Alchemy API account, there is a daily transaction limit
2. For LinkedIn user, when crawling the job posts, requests might be forbidden. When this happens, it might work to update the OAuth token as it can expire.


## Contributor:

@xiaohan2012
