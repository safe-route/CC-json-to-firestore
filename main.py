from google.cloud import storage
import json
import firebase_admin
import os
from firebase_admin import credentials, firestore

def get_json(filename, bucket):
    '''
    this function will get the json object from
    google cloud storage bucket
    '''
    # get the blob
    blob = bucket.get_blob(filename)
    # load blob using json
    file_data = json.loads(blob.download_as_string())
    return file_data

def main(event, context):
    #connection and service account
    storage_client = storage.Client()

    bucket_name = 'safe-route-clustering-to-firestore'
    bucket = storage_client.get_bucket(bucket_name)
    filename = 'clustering.json'

    firebase_admin.initialize_app()
    db = firestore.client()

    json_data = get_json(filename, bucket)
    get_col = list(json_data.keys())
    collection = str(get_col)[2:-2]
    convertion = str(json_data['centroids-test'])
    string = convertion.replace("'", "\"")
    res = json.loads(string)
    docs = res

    for doc in docs:
      id = doc['id']
      db.collection(collection).document(str(id)).set(doc, merge=True)
      print(str(id) + " Success")

if __name__ == "__main__":
  main(event, context)
