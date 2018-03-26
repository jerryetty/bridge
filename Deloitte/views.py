from django.shortcuts import render
from django.http import HttpResponse

# from firebase import firebase
# # Import database module.
# from firebase_admin import db

# # Get a database reference to our posts
# ref = db.reference('server/saving-data/fireblog/posts')

# Read the data at the posts reference (this is a blocking operation)
# print ref.get()





import pyrebase
config = {
  "apiKey": "AIzaSyCclOmtad6FtvQ3x08ww4Z6xML5Vs1bMI0",
  "authDomain": "bridge-a08e9.firebaseapp.com",
  "databaseURL": "https://bridge-a08e9.firebaseio.com/",
  "storageBucket": "gs://bridge-a08e9.appspot.com/",
  # "serviceAccount": "D:\Web\Bridge\venv\Bridge\Deloitte\Bridge-e4e239f0cf57.json"
}
firebase = pyrebase.initialize_app(config)

# Create your views here.
def index(request):
	return render(request, 'pages/dashboard.html', {})
def income(request):
	# income = db.bridge-a08e9(income)
	return render(request, 'pages/income.html', {})
def assets(request):
	return render(request, 'pages/assets.html', {})
def liability(request):
	return render(request, 'pages/liability.html', {})
def expenditure(request):
	return render(request, 'pages/expenditure.html', {})
def equity(request):
	return render(request, 'pages/equity.html', {})	
def business_details(request):
	return render(request, 'pages/business_details.html', {})	