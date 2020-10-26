from firebase import firebase
from google.cloud import storage
import os

os.environ["GOOGLE_APPLICATION_CREDENTIALS"]=""

client = storage.Client()
bucket = client.get_bucket('iotfundamentals.appspot.com')
imageBlob = bucket.blob("/")
imagePath = "/home/capeie/iotprojekt/photo.jpg"
imageBlob = bucket.blob("photo.jpg") 
imageBlob.upload_from_filename(imagePath)