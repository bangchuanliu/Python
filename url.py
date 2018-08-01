import urllib2

res = urllib2.urlopen("https://www.google.com")
print res.info()
#print res.read()
