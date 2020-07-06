import argparse
from PIL import Image

parser=argparse.ArgumentParser(description="convert a picture into a ascii char text")
parser.add_argument("file",help="the name of the file")
parser.add_argument("--width",type=int,default=100,help="set width, default=100 pixels")
parser.add_argument("--height",type=int,default=50,help="set height, default=50 pixels")
parser.add_argument("--OutputName",default="asciiresult",help="the output txt name")

args=parser.parse_args()
IMG=args.file

im=Image.open(IMG)

WIDTH=args.width
HEIGHT=args.height

im = im.resize((WIDTH, HEIGHT))

grey=im.convert(mode="L")

def getChar(greyV,CharList):
    x=int(greyV/256*len(CharList))
    return CharList[x]

ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")


text=""
for y in range(HEIGHT):
    for x in range(WIDTH):
        char=getChar(grey.getpixel((x,y)),ascii_char)
        text+=char
    text+="\n"

Outname=args.OutputName

with open("{}.txt".format(Outname),"w") as f:
    f.write(text)


