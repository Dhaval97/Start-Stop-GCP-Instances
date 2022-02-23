# Start-Stop-GCP-Instances
How to Start and Stop GCP (Google Cloud Platform) VM Instances and SQL Instances

### Description
* To use start.py and stop.py in GCP -> Create a **Cloud Function**
* To use Cloud Function -> Create a **Cloud Scheduler Task**

### Cloud Function Settings
* **Environment** - 1st gen
* **Function name** - Any name you want
* **Region** - Select region of your choice
* **Triger type** - HTTP
* **Authentication** - Require authentication
* Enable Require HTTPS
* Select **RUNTIME** -> Timeout - 180 seconds
* **Runtime service account** - Select service account of your choice (remember to give permission for supported tasks)
* Click Next
* Change Runtime -> Python 3.9
* Enter Entry point -> entry_point (defines where to start the python file)
* Enter the source code -> main.py
* Enter requirements -> requirements.txt
* Finally **Deploy**

### Cloud Scheduler Settings
* **Name** - Any name you want
* **Region** - Select region of your choice
* **Frequency** - Enter in cron jobs language (Help -> https://crontab.guru/)
* **Time zone** - Select Time zone as per needs
* Click Continue
* **Target Type** - HTTP
* **URL** - Copy url from Cloud Functio's **TRIGGER** Tab
* **HTTP method** - GET
* **Auth header** - Add OIDC token
* **Service Account** - Select same service account used for Cloud Function
* **Audience** - Paster the same as URL
* Click Create
