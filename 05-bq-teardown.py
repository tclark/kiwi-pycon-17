from google.cloud import bigquery

bq_client = bigquery.Client.from_service_account_json('your credentials file')
dataset_ref = bq_client.dataset('trump_tweets')
dataset = bigquery.Dataset(dataset_ref)
bq_client.delete_dataset(dataset)
