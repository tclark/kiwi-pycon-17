from google.cloud import bigquery

# set up client with credentials in a json file
bq_client = bigquery.Client.from_service_account_json('your credentials file')



query_string = 'SELECT AVG(replies/retweets) AS average FROM `twitter-ratio.trump_tweets.tweet_data` WHERE replies > 500 AND retweets > 500'
query_job = bq_client.query(query_string)
result = list(query_job.result())[0]
print(result.average)


years = [
         ('2009-01-01T00:00:00', '2010-01-01T00:00:00'),
         ('2010-01-01T00:00:00', '2011-01-01T00:00:00'),
         ('2011-01-01T00:00:00', '2012-01-01T00:00:00'),
         ('2012-01-01T00:00:00', '2013-01-01T00:00:00'),
         ('2013-01-01T00:00:00', '2014-01-01T00:00:00'),
         ('2014-01-01T00:00:00', '2015-01-01T00:00:00'),
         ('2015-01-01T00:00:00', '2016-01-01T00:00:00'),
         ('2016-01-01T00:00:00', '2017-01-01T00:00:00'),
         ('2017-01-01T00:00:00', '2017-10-01T00:00:00')
        ]
# this query will give us average ratios by year
#query_string = "SELECT AVG(replies/retweets) AS average FROM `twitter-ratio.trump_tweets.tweet_data` WHERE replies > 500 AND RETWEETS > 500 AND date > @start_lim AND date < @end_lim"
# this one gives number of tweets with ratio > 2
query_string = "SELECT COUNT(*) AS average FROM `twitter-ratio.trump_tweets.tweet_data` WHERE replies/retweets > 2 AND replies > 500 AND RETWEETS > 500 AND date > @start_lim AND date < @end_lim"

jobs = []
for  limits in years:
    print(limits[0], limits[1])
    start_param = bigquery.ScalarQueryParameter('start_lim', 'TIMESTAMP', limits[0])
    end_param = bigquery.ScalarQueryParameter('end_lim', 'TIMESTAMP', limits[1])
    job_config = bigquery.QueryJobConfig()
    job_config.query_parameters = [start_param, end_param]
    jobs.append(bq_client.query( query_string, job_config=job_config))


results = [list(job.result())[0] for job in jobs]
for r in results:
    print(r.average)
