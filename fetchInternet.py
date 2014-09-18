#Import Libraries
import urllib2

#Create Request URL
req = urllib2.Request('http://python.org/')

#Add request headers
req.add_header('User-Agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:5.0)')


#Get response
response = urllib2.urlopen(req)

#Read Response
the_page = response.read()


print the_page
print req.headers
