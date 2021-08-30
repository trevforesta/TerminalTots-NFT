#generate_terminaltots.py
#Description: This file generates images of all possible feature combinations for TerminalTots.
#Author: Trevor Foresta
#Date Written: 8/28/2021
#Date Last Modified: 8/29/2021

import glob
from PIL import Image
from itertools import cycle, islice

#Pathways for body and face assets
bodies = glob.glob ('Body/*')
faces = glob.glob ('Faces/*')

body_iter = iter(bodies)

# repeatlist() - resets faces iterator for next body
# note: may also use this function for future accessories
def repeatlist(it, count):
    return islice(cycle(it), count)

# paste_faces - for given body, paste every possible face
def paste_faces(body, face):
    face_iter = iter(faces)
    for n in range(len(faces)):
        face = Image.open(next(face_iter))
        body.paste(face, (53,79), mask=0)
        body.save("Generated/" + str(body) + str(body_iter) + str(n), "PNG")
        repeatlist(faces, len(bodies))

# main - shows available assets, generates Tots
def main():
    body = Image.open(next(body_iter))
    print("\n[Compucons Generator]\n\nAvailable Body Colors: ")
    print([b.strip('Body/*.png') for b in bodies])
    print("\nAvailable Faces: ")
    print([f.strip('Faces/*.png') for f in faces])
    print("\n")

    for index in range(len(bodies)):
        for face in faces:
            body = Image.open(next(body_iter))
            paste_faces(body, face)

# Execute main:
main()
