
import cv2
import numpy as np
import os
import time 
import face_recognition
import subprocess

#-------------------------------------------------------------------------------------------------------------------------------------------
def Compare_face():
	video_capture = cv2.VideoCapture(0)

	# Load a sample picture and learn how to recognize it.
	Owner_image = face_recognition.load_image_file("xyz.jpg")
	owner_face_encoding = face_recognition.face_encodings(Owner_image)[0]


	# Create arrays of known face encodings and their names
	known_face_encodings = [owner_face_encoding]
	known_face_names = ["saurabh"]

	# Initialize some variables
	face_locations = []
	face_encodings = []
	face_names = []
	process_this_frame = True

	count = 0
	cnt_1 = 0
	cnt_0 = 0
	List = []
	cnt_face_not = 0

			
	while count < 100 :
		""" Grab a single frame of video"""
		ret, frame = video_capture.read()
		
		""" Only process every other frame of video to save time """
		if process_this_frame:
			""" Resize frame of video to 1/4 size for faster face recognition processing """
			small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

			""" Convert the image from BGR color (which face_recognition uses) """
			rgb_small_frame = small_frame[:, :, ::-1]
		    
			""" Find all the faces and face encodings in the current frame of video """
			face_locations = face_recognition.face_locations(rgb_small_frame)
			face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)
			
			""" if face not detected in camera it will shut down the system"""
			if(len(face_locations) == 0):
				cnt_face_not = cnt_face_not + 1;	
			
			if(cnt_face_not == 420):
				# call face not detected program
				subprocess.check_call("python3 Not_Detected.py",shell = True)

				
			face_names = []
			for face_encoding in face_encodings:
				
				""" See if the face is a match for the known face(s) """
				matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
				name = "Unknown"
				
				face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
				best_match_index = np.argmin(face_distances)
				if matches[best_match_index]:
					name = known_face_names[best_match_index]

				face_names.append(name)
				
				"""------------------------------------------------------"""
				if(name == "saurabh"):
					List.append(1)
					cnt_1 = cnt_1 + 1
				else:
					List.append(0)
					cnt_0 = cnt_0 + 1
				count = count + 1			
				"""------------------------------------------------------"""
		process_this_frame = not process_this_frame

					
	"""check how much percentage face is match"""
	if(cnt_1 > 85):
		print("True")
		print(cnt_1,"%")
		subprocess.check_call("python3 Verified.py",shell = True)
	
	else:			
		""" Release handle to the webcam """
		video_capture.release()
		cv2.destroyAllWindows()

		print("False")
		print(cnt_0,"%")
		subprocess.check_call("python3 Not_Verified.py",shell = True)
	
#-------------------------------------------------------------------------------------------------------------------------------------------

def main():
	Compare_face()
	
#-------------------------------------------------------------------------------------------------------------------------------------------

if __name__ == "__main__":
	main()
	
#-------------------------------------------------------------------------------------------------------------------------------------------



