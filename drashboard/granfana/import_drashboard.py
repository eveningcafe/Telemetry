import requests
url='http://admin:admin@localhost:3000/api/dashboards/import'
data='''{
  "dashboard": {
    "annotations": {
          "list":[]
      },
    "editable": true,
    "gnetId": null,
    "graphTooltip": 0,
    "id": null,
    "iteration": 1529322539820,
    "links":[],
    "panels": [{}],
    "schemaVersion": 16,
    "style": "dark",
    "tags": [],
    "templating": {
        "list": []
    },
    "time": {},
    "timepicker": {},
    "timezone": "",
    "title": "name of the dashboard",
    "uid": "uid",
    "version": 1,
    "__inputs": [],
    "__requires": []
  },
  "inputs": [],
  "overwrite": false
}'''
headers={"Content-Type": 'application/json'}
response = requests.post(url, data=data,headers=headers)
print(response)
print(response.status_code)
print (response.text)
