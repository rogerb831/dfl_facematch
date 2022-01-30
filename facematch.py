import face_recognition
from shutil import move
import os
from os import path
import sys
from pathlib import Path, PureWindowsPath

# Set up commmand line args
file_to_recognize = sys.argv[1]
target_dir = sys.argv[2]

#Validate source file
if not path.isfile(file_to_recognize):
   print("ERROR: File " + str(file_to_recognize) + " isn't valid")
   exit()

#Validate target directory
if not path.isdir(target_dir):
   print("ERROR: Path " + str(target_dir) + " isn't a valid directory")
   exit()

#Count how many files in the directory
#file_count = len(os.listdir(target_dir))
dirhash = next(os.walk(target_dir))[2]
file_count = len(next(os.walk(target_dir))[2])

#Show some stats
#print("Using " + str(file_to_recognize) + " as source")
print("Checking " + str(file_count) + " files")

#Setup the output directory for matching faces
match_path = os.path.join(target_dir, 'match')

#Make sure the path exists and if not, create it.
if not path.isdir(match_path):
   try:
       os.mkdir(match_path)
   except OSError:
       print("Creation of the directory %s failed" % match_path)
   else:
       print("Successfully created the directory %s " % match_path)


# Create an encoding of my facial features that can be compared to other faces
picture_of_me = face_recognition.load_image_file(file_to_recognize)
my_face_encoding = face_recognition.face_encodings(picture_of_me)[0]

iterator=1

# Iterate through all pictures
for thisFile in dirhash:
   
   file_name = os.path.join(target_dir, thisFile)
   print("Working on " + str(iterator) + " of " + str(file_count) + ": " + str(file_name))

   iterator += 1

   # Load this picture
   new_picture = face_recognition.load_image_file(file_name)
   
   # Iterate through every face detected in the new picture
   for face_encoding in face_recognition.face_encodings(new_picture):

       # Run the algorithm of face comaprison for the detected face, with 0.5 tolerance
       results = face_recognition.compare_faces(
           [my_face_encoding], face_encoding, 0.5)

       # Save the image to a seperate folder if there is a match
       if results[0] == True:
           match_file = os.path.join(match_path, thisFile)
           print (thisFile + " is a match, copying to " + match_file)
           move(
               file_name, match_file)