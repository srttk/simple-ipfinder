#Trinko
#17/March/2012
#Sarath
#http://github.com/saratonite
#IP Finder Tool
import socket
import os
def trackme():
	try:
		url=raw_input("Enter wesite(/eg:google.com)/:");
		try:
			ip=socket.gethostbyname(url)
			print "Ip address of ",url,": ", ip
		except:
			print "SysError";
		raw_input("Press enter to exit")
		os.system(cmd)
	except:
		print "IP Track Tool Connection Error"
		print "Internet connection not available"
		print "www.sarathink.wordpress.com"
		raw_input("Press enter to exit")
		
trackme()
