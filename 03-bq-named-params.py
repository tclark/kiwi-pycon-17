from google.cloud import bigquery

def print_tweet(tweet):
    print('=======================')
    print('Date: {}.'.format(tweet.date))
    print(tweet.text)
    print('Replies: {}  Retweets: {}.'.format(tweet.replies, tweet.retweets))
    print('Ratio: {}.'.format(tweet.ratio))
    print('ID: {}.'.format(tweet.id))
    print('=======================')


# set up client with credentials in a json file
bq_client = bigquery.Client.from_service_account_json('your credentials file')
# note named parameter @threshold in string
query_string = 'SELECT id, replies,retweets, replies/retweets AS ratio, date,text FROM `twitter-ratio.trump_tweets.tweet_data` WHERE replies > @threshold AND retweets > @threshold ORDER BY ratio DESC LIMIT 1'

jobs = []
for t in (5, 10, 50, 100, 500, 1000):
    param = bigquery.ScalarQueryParameter('threshold', 'INTEGER', t)
    job_config = bigquery.QueryJobConfig()
    job_config.query_parameters = [param]
    jobs.append(bq_client.query( query_string, job_config=job_config))

results = [list(job.result()) for job in jobs]

for r in results:
    print_tweet(r[0])
