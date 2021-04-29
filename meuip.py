import urllib
url = 'http://myexternalip.com/raw'
myip = urllib.urlopen(url).read()

print myip
