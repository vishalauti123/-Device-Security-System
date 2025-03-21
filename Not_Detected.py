
"""
 If face not detected..
 Caputre  the screenshot  save that img  in photo directory
 and send that img by mail to the owner and shutdown the system
"""

#-----------------------------------------------------------------------------------------------------

import random 
import cv2

from datetime import date
import pyautogui as p

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
		print("Available...")
		return True
	except:
		print("Not Available...")
		return False

#-----------------------------------------------------------------------------------------------------

def Mail(path):	
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
		MailSender(path)
		
#-----------------------------------------------------------------------------------------------------

def MailSender(path):
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
		Dhoke Saurabh              
		  """
		
	Subject = """ 😟️ Alert,Alert 😟️"""
		
	msg['Subject'] = Subject
	msg.attach(MIMEText(body,'plain'))
		
	"""------------ Attach image ----------------------"""
		
	#photo = ("Photo/pic.png")
		
	attachment = open(path,"rb")
		
	p = MIMEBase('application','octet-stream')
	p.set_payload((attachment).read())
		
	encoders.encode_base64(p)
	p.add_header('Content-Disposition',"attachment;filename =  %s"%path)
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
	
	folder_name = "Screenshot"
	if not os.path.exists(folder_name):
		try:
			os.mkdir(folder_name)
		except:
			pass
	
	today = date.today()
	log_path = os.path.join(folder_name,"pic_on %s.png"%(today))
		
	SS = p.screenshot()
	SS.save(r''+log_path)
	
	print("Screenshot captured...")
	time.sleep(2)
	Mail(log_path)

#-----------------------------------------------------------------------------------------------------

def Play_Sound():
	playsound("Audio.mp3")
	
#-----------------------------------------------------------------------------------------------------

def Warning_window():
	root = tkinter.Tk()
	root.withdraw()

	messagebox.showwarning("Warning ☠️","Face not Detected... So I'm turning off the machine ")

#-----------------------------------------------------------------------------------------------------
	
def ShutDown():
	print("Shut Down machine...")
	#os.system("poweroff")

#-----------------------------------------------------------------------------------------------------

def main():
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
			
	




