![TerminalTots Logo](https://uploads-ssl.webflow.com/61116be30fa72a710da13ebe/612ced8bc60b405fcd8dc7f2_title.jpg)
# TerminalTots NFT Project

TerminalTots is an NFT (Non-Fungible Token) project on the Polygon Blockchain. This repo contains a random icon generator written in Python. With designs inspired by the retro terminals of early computing, each TerminalTot is unique in its appearance.

Visit the [TerminalTots Collection](https://opensea.io/collection/terminaltots) on OpenSea.

## Getting Started

### Dependencies (Python)
* Glob
* Pillow
* Itertools

### Executing program
To create a series of TerminalTots, simply run the following files in order:
```
python3 generate_tots.py
python3 backdrop.py
python3 add_hats.py
```
![TerminalTots preview](https://uploads-ssl.webflow.com/61116be30fa72a710da13ebe/612ceda6ffb069e853d81add_tots_preview.jpg)
The program generate_tots will create image files (PNG) of every possible combination of body and face assets, then backdrop will add random backgrounds to each tot. Finally, add_hats will create every combination of Tots with their wearable hats.  

## Authors & Acknowledgments
* Project created by Trevor Foresta - [@trevforesta](https://github.com/trevforesta)
* TerminalTots logo created with [Textcraft](https://textcraft.net/)
* README written with [StackEdit](https://stackedit.io/).
