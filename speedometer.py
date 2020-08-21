import subprocess
import ast
import time
import csv
from datetime import datetime

from pydrive2.auth import GoogleAuth
from pydrive2.drive import GoogleDrive

import json
import requests


headers = {"Authorization": "Bearer " + \
ya29.a0AfH6SMCbHx0gQVfDJWR-1Ldr



#import os

#gauth=GoogleAuth()
#gauth.LocalWebserverAuth()

print('Starting.')

time.sleep(1000)

#gauth = GoogleAuth()

#gauth.LoadCredentialsFile("mycreds.txt")
#if gauth.credentials is None:
#	gauth.LocalWebserverAuth()
#elif gauth.access_token_expired:
#	gauth.Refresh()
#else:
#	gauth.Authorize()

#gauth.SaveCredentialsFile("mycreds.txt")

#drive = GoogleDrive(gauth)

#auth_url = gauth.GetAuthUrl()
#g_login.LocalWebserverAuth()
#drive = GoogleDrive(g_login)

#print('Login part finished.')

locationList = []

def getLocation():
	location = subprocess.run("termux-location",
stdout=subprocess.PIPE)
	current_time = time.time()
	location=location.stdout.decode("utf-8")
	location=ast.literal_eval(location)
	#locationList.insert(0, {"latitude": location["latitude"],
#"longitude":location["longitude"],"time":current_time})
	locationList.append({"latitude":location["latitude"],"longitude":location["longitude"],"time":current_time})
	finish_time = time.time()
	print(datetime.fromtimestamp(current_time))
	#print(locationList)
	print(locationList[len(locationList)-1])


for i in range(180):
	start_time = datetime.fromtimestamp(time.time())
	for j in range(5):
		try:
			getLocation()
			print('RUnning again.')
			
		except:
			print('Trying again.')
			continue
	end_time = datetime.fromtimestamp(time.time())
	
	f = open('storage/dcim/Screenshots/locations_'+str(start_time)+'_'+str(end_time)+'.csv','w')
	print(f)
	#f = open('storage/emulated/0/DriveSyncFiles/locations_'+str(start_time)+'_'+str(end_time)+'.csv','w')	

	with f:
		writer = csv.writer(f)
		for j in range(len(locationList)):
			writer.writerows(locationList[j].items())

#f = open('storage/dcim/Screenshots/locations_'+str(start_time)+'_'+str(end_time)+'.csv','w')

#with f:
#	writer = csv.writer(f)
#	for i in range(len(locationList)):
#		writer.writerows(locationList[i].items())

print('Finished.')
