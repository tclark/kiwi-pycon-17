from google.cloud import bigquery

bq_client = bigquery.Client.from_service_account_json('your credentials file')

dataset_ref = bq_client.dataset('trump_tweets')
dataset = bigquery.Dataset(dataset_ref)
dataset = bq_client.create_dataset(dataset)


# create table from json
table_ref = dataset.table('tweet_data')
table = bigquery.Table(table_ref)

# I'm not going to specify the schema, but included for reference.
#table.schema = [
  #  bigquery.SchemaField('id', 'STRING', mode='REQUIRED'),
  #  bigquery.SchemaField('text', 'STRING', mode='REQUIRED'),
  #  bigquery.SchemaField('date', 'TIMESTAMP', mode='REQUIRED'),
  #  bigquery.SchemaField('retweets', 'INTEGER', mode='REQUIRED'),
  #  bigquery.SchemaField('replies', 'INTEGER', mode='REQUIRED')
  #      ]
#bq_client.create_table(table)

job_config = bigquery.LoadJobConfig()
job_config.source_format = 'NEWLINE_DELIMITED_JSON'
job_config.autodetect = True
with open('twitter_data_set.json', mode='rb') as datafile:
    job = bq_client.load_table_from_file(datafile, table_ref,
            job_config=job_config)
job.result()    



