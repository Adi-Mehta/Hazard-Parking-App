from flask import Flask, render_template, request, jsonify
import uuid
from google.cloud import storage
from google.cloud.storage import Blob
import cloudstorage as gcs
import os


app = Flask(__name__)

storage_client = storage.Client()
buck_name = "hazbucket"
bucket = storage_client.create_bucket(buck_name)
GOOGLE_APPLICATION_CREDENTIALS="C:/Users/Aditya Mehta/Documents/Final Project/Corrected/Templates/Hazard-b5dfbc34951c.json"

def upload_blob(bucket_name, file, name, lat, lon, destination_blob_name):
	storage_client = storage.Client()
	bucket = storage_client.get_bucket(bucket_name)
	blob = bucket.blob(destination_blob_name)

@app.route("/")
def index():
	return render_template("index.html")

@app.route("/upload", methods=["POST"])
def upload():
	original = request.files.get('image', None)
	image=images.Image(original.read())
	name=request.form.get('name')
	lat=request.form.get('latt')
	lon=request.form.get('long')
	lat=str(lat)
	lon=str(lon)
	upload_blob(buck_name, image,lat, lon, "hazard")

	
	# f = gcs.open(bucket_name+'haz-{}'.format(uuid.uuid4()),'w', content_type ='image/jpg')
	# f.write(image)
	# f.close()
	return render_template("complete.html")
