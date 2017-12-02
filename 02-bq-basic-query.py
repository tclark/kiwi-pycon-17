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


# run a query
query_string = 'SELECT id, replies,retweets, replies/retweets AS ratio, date, text FROM `twitter-ratio.trump_tweets.tweet_data` ORDER BY ratio DESC LIMIT 1'

query_job = bq_client.query(query_string)
print(query_job.state) # should be 'RUNNING'
results = list(query_job.result())
print_tweet(results[0])
