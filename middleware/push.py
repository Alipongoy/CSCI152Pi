import urllib2, urllib
import json
import pdb

path = 'http://ab-kc.tk/parking/push.php'
with open('../backend/data.json') as json_data:
    mydata = json.load(json_data)

req = urllib2.Request(path)
req.add_header('Content-Type', 'application/json')
response = urllib2.urlopen(req, json.dumps(mydata))
print response.read().decode("iso-8859-1")
