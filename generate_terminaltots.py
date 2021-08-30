#generate_terminaltots.py
#Description: This file generates images of all possible feature combinations for TerminalTots. 
#Author: Trevor Foresta
#Date Written: 8/28/2021
#Date Last Modified: 8/29/2021

import glob
from PIL import Image
from itertools import cycle, islice

bodies = glob.glob ('Body/*')
faces = glob.glob ('Faces/*')

body_iter = iter(bodies)
COUNT = 0

def increment():
    global COUNT
    COUNT = COUNT+1

def repeatlist(it, count):
    return islice(cycle(it), count)

def paste_faces(body, face):
    face_iter = iter(faces)
    for n in range(len(faces)):
        face = Image.open(next(face_iter))
        body.paste(face, (53,79), mask=0)
        increment()
        body.save("Generated/" + str(COUNT), "PNG")
        #print("n:"+ str(n))
        #print("body_iter:"+ str(body_iter))
        repeatlist(faces, len(bodies))

def main():
    print("\n[Compucons Generator]\n\nAvailable Body Colors: ")
    print([b.strip('Body/*.png') for b in bodies])
    print("\nAvailable Faces: ")
    print([f.strip('Faces/*.png') for f in faces])
    print("\n")

    print("\n\n\n"+str(len(bodies)))

    for index in range(len(bodies)):
        for face in faces:
            body = Image.open(next(body_iter))
            paste_faces(body, face)
        
main()


