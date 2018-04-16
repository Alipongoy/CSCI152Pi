import urllib2, urllib
mydata = [("lot","lotQ"),("genID","1-1"),("space",3),("isOpen",1)]
mydata=urllib.urlencode(mydata)
path = 'http://ab-kc.tk/parking/push.php'
req=urllib2.Request(path, mydata)
req.add_header("Content-type", "application/x-www-form-urlencoded")
page=urllib2.urlopen(req).read()
print page
