import base64
import googleapiclient.discovery
from oauth2client.client import GoogleCredentials

project_id = "YOUR_PROJECT_ID"
zone_name = 'INSTANCE_ZONE_NAME'

def start_vm():
  instance_action = "start"
  credentials = GoogleCredentials.get_application_default()
  compute = googleapiclient.discovery.build('compute', 'v1', credentials=credentials)
  
  instances_result = compute.instances().list(project=project_id, zone=zone_name).execute()
  if 'items' in instances_result:
    for instance_row in instances_result["items"]:
      instance_name = ""
      instance_zone = ""
      instance_name = instance_row["name"]
      instance_zone = zone_name
      action_api_call = "compute.instances()."+instance_action+"(project=project_id, zone=zone_name, instance=instance_name)"
      action_result = eval(action_api_call).execute()

def start_sql():
  credentials = GoogleCredentials.get_application_default()
  service = googleapiclient.discovery.build('sqladmin', 'v1', credentials=credentials)
  
  sql_instance = 'SQL_INSTANCE_NAME'
  
  request = service.instances().get(project=project_id, instance=sql_instance)
  response = request.execute()
  
  j = response["settings"]
  settingsVersion = int(j["settingsVersion"])
  
  dbinstancebody = {
    "settings": {
      "settingsVersion": settingsVersion,
      "tier": "db-n1-standard-1",
      "activationPolicy": "Always"
    }
  }
  
  request = service.instances().update(project=project_id, instance=sql_instance, body=dbinstancebody)
  response = request.execute()

def entry_point(request):
  start_vm()
  start_sql()
  return f'Success'