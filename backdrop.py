#backdrop.py
#Description: This file can be used to add backdrops for generated TerminalTots.
#Author: Trevor Foresta
#Date Written: 8/30/2021
#Date Last Modified: 8/31/2021

import glob
from PIL import Image, ImageOps

#Set pathway and iterator for generated tots
tots = glob.glob ('Generated/*')
tots_iter = iter(tots)
COUNT = 0

#Blank template of larger size to use as backdrop
background_img = Image.open("BGTemplate.png")

# increment - counter used for naming convention
def increment():
    global COUNT
    COUNT = COUNT+1

# attach_bg - pastes generated tots onto background
def attach_bg():
    for tot in range(len(tots)):
        tot = Image.open(next(tots_iter))
        name = tot.filename
        background_img.paste(tot, (150,200), mask=0)
        increment()
        background_img.save("GeneratedBG/" + (str(COUNT).zfill(4))+ ".png", "PNG")

attach_bg()