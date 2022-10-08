import unicodedata
import urllib

url = 'http://ubaid.tk/sms/sms.aspx?uid=&pwd=&phone=%s&msg=%s&provider=way2sms'

def sendSMS(number, message):
	number = unicodedata.normalize('NFKD', unicode(number)).encode('ASCII', 'ignore')
	message = unicodedata.normalize('NFKD', unicode(message)).encode('ASCII', 'ignore')
	req = urllib.urlopen(url % (number, message))
	return req.read()
