"""
 If face verified Successfully
"""
#-----------------------------------------------------------------------------------------------------
import tkinter
from tkinter import messagebox

from playsound import playsound
import threading

#-----------------------------------------------------------------------------------------------------

def Play_Sound():
	playsound("welcome.mp3")

#-----------------------------------------------------------------------------------------------------

def Warning_window():
	root = tkinter.Tk()
	root.withdraw()
	messagebox.showwarning("Warning ","Face Verified... Welcome Sir ")

#-----------------------------------------------------------------------------------------------------

def main():	
	# Creating the threads	
	t1 = threading.Thread(target=Play_Sound, args=())
	t2 = threading.Thread(target=Warning_window, args=())
	
	# Starting the threads 
	t1.start()
	t2.start()
	
	# wait to complete there tasks
	t2.join()
	t1.join()
	
#------------------------------------------------------------------------------------------------------------------------------------------------

if __name__ == "__main__":
	main()

"""------------------------------------------------------------------------------------------------------------------------------------"""			

