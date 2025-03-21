
"""
 If not face verified..
 Caputre  photo save that img  in photo directory
 and send that img by mail to the owner and shutdown the system
"""

#-----------------------------------------------------------------------------------------------------

import random 
import cv2
import datetime
import time
import os 

from playsound import playsound
import threading

import tkinter
from tkinter import messagebox

from sys import *


from urllib.request import urlopen
import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

#-----------------------------------------------------------------------------------------------------

def is_connected():
	try:
		urlopen('https://www.google.com/')
		print("Network Available...")
		return True
	except:
		print("Network Not Available...")
		return False

#-----------------------------------------------------------------------------------------------------

def Mail():	
	print("Checking network connection...")
	connected = is_connected()
	cnt = 0
	
	if connected == False :
		while cnt < 6:	
			#print(cnt)
			cnt = cnt + 1
			time.sleep(10)	
			connected = is_connected()
	
	if connected == True:		
		MailSender()
		
#-----------------------------------------------------------------------------------------------------

def MailSender():
	from_address = "Sender-mail-id"
	to_address   = "Reciver-mail-id"
		
	msg = MIMEMultipart()
	msg['From'] = from_address
	msg['To'] = to_address

	body = """
	Hello Sir...
		 Your Laptop was open by someone, i was captured that person image and sending you by attaching mail...check image imigiataly
		
	This is automatically generated mail please do not reply to this mail.
		Thanks & Regards,
		Device Security System              
		  """
		
	Subject = """ 😟️ Alert,Alert 😟️"""
		
	msg['Subject'] = Subject
	msg.attach(MIMEText(body,'plain'))
		
	"""------------ Attach image ----------------------"""
		
	photo = ("Photo/pic.png")
		
	attachment = open(photo,"rb")
		
	p = MIMEBase('application','octet-stream')
	p.set_payload((attachment).read())
		
	encoders.encode_base64(p)
	p.add_header('Content-Disposition',"attachment;filename =  %s"%photo)
	msg.attach(p)
		
	"""--------------------------------------------------"""
		
	s = smtplib.SMTP('smtp.gmail.com',587)
	s.starttls()
	s.login(from_address,"password")
		
	text = msg.as_string()
	s.sendmail(from_address,to_address,text)
	s.quit()
	print("Mail send...")
#-----------------------------------------------------------------------------------------------------

def Capture_image():
	StartTime = time.time()
	cam_port = 0
	cam = cv2.VideoCapture(cam_port)
	
	result, image = cam.read()
	cv2.imwrite("Photo/pic.png", image)
	cv2.destroyAllWindows()
	
	print("image captured...")
	time.sleep(2)
	Mail()

#-----------------------------------------------------------------------------------------------------

def Play_Sound():
	playsound("Audio.mp3")

#-----------------------------------------------------------------------------------------------------

def Warning_window():
	root = tkinter.Tk()
	root.withdraw()

	messagebox.showwarning("Warning ☠️","You are not owner... So I'm turning off the machine ")

#-----------------------------------------------------------------------------------------------------
	
def ShutDown():
	print("Shut Down machine...")
	os.system("poweroff")

#-----------------------------------------------------------------------------------------------------

def main():
	#print("\n-------------- Shiv Shambho : Photo Capture Script ------------------")
	#print("Application Name : "+argv[0])
	
	if (len(argv) == 2):
		if ((argv[1] == "-h") or (argv[1] == "-H")):	
			print("This script is used to take photo of user when he will start the laptop and send that image by mail to the owner of the laptop automatically ")
			exit()
			
		if ((argv[1] == "-u") or (argv[1] == "-U")):	
			print("Usage : Application_Name")
			exit()
	
	# call to the capture image function		
	Capture_image()	
	
	# Creating the threads	
	t1 = threading.Thread(target=Play_Sound, args=())
	t2 = threading.Thread(target=Warning_window, args=())
	t3 = threading.Thread(target=ShutDown, args=())
	
	# Starting the threads 
	t1.start()
	time.sleep(6)
	
	t2.start()
	time.sleep(20)
	
	t3.start()
	
	
#------------------------------------------------------------------------------------------------------------------------------------------------

if __name__ == "__main__":
	main()

"""------------------------------------------------------------------------------------------------------------------------------------"""			
			
	




