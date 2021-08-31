#add_hats.py
#Description: This file can be used to add hats to generated TerminalTots that have backdrops.
#Author: Trevor Foresta
#Date Written: 8/30/2021
#Date Last Modified: 8/31/2021

import glob
from PIL import Image
from itertools import cycle, islice

#Pathways for backdrop tots and hat assets
BGtots = glob.glob ('GeneratedBG/*')
hats = glob.glob ('Hats/*')

BGtot_iter = iter(BGtots)
COUNT = 0

# increment - counter used for naming convention
def increment():
    global COUNT
    COUNT = COUNT+1

# add_hats - for given BGtot, paste every possible hat
def add_hats(BGtot, hat):
    hat_iter = iter(hats)
    for hat in range(len(hats)):
        hat = Image.open(next(hat_iter))
        BGtot.paste(hat, (80,15), hat)
        increment()
        BGtot.save("GeneratedFinal/" + (str(COUNT).zfill(4)) + ".png", "PNG")

# main - shows available assets, generates Tots
def main():
    for index in range(len(BGtots)):
            BGtot = Image.open(next(BGtot_iter))
            hat = None
            add_hats(BGtot, hat)
        
main()


