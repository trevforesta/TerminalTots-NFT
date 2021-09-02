#backdrop.py
#Description: This file can be used to add backdrops for generated TerminalTots.
#Author: Trevor Foresta
#Date Written: 8/30/2021
#Date Last Modified: 8/31/2021

import glob
from PIL import Image, ImageOps
import random 

#Set pathways and iterator for generated tots
tots = glob.glob ('Generated/*')
tots_iter = iter(tots)
backdrops = glob.glob ('Backdrops/*')
COUNT = 0

# increment - counter used for naming convention
def increment():
    global COUNT
    COUNT = COUNT+1

# attach_bg - pastes generated tots onto background
def attach_bg():
    for tot in range(len(tots)):
        background_img = Image.open(random.choice(backdrops))
        tot = Image.open(next(tots_iter))
        name = tot.filename
        tot_copy = tot.copy()
        background_img.paste(tot_copy, (150,200), mask=tot)
        increment()
        background_img.save("GeneratedBG/" + (str(COUNT).zfill(4))+ ".png", "PNG")

attach_bg()