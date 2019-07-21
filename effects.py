'''Effects for images'''

#Importing libraries
import cv2
import argparse
from PIL import Image

#Importing external file libraries
from anagylph import effect
from sketch import effect_s

class Filter(object) : 
    
    def negative_img(self,img,fileName) :
        print(">>>Processing of the negative image\n")
        negative_img = cv2.bitwise_not(img)
        cv2.imwrite("Effects/Negative/"+fileName+".jpg" , negative_img)
        print("Press y to show you the preview of the filtered image")
        key = input()
        if key.lower() in ["y", "yes"]:
            image = Image.open("Effects/Negative/" + fileName + '.jpg')
            image.show()
        else :
            print("Your image is saved in the Effects/Negative folder\n")

    def convert_to_sketch(self,img,fileName) :
        effect_s.effect(self,img,fileName)
        return "done"

    def anagylph(self,img,fileName) :
        effect(self,img,fileName)
        return "done"


parser = argparse.ArgumentParser(description = "Adding effects  to your images ") #you iniatize as such
print(">>> Filters avaible")
print(">>> n for negative image\n>>> s for sketch of the image\n>>> a for 3D retro effect\n")
parser.add_argument("-f", required=True, help="enter fileName of your picture")
parser.add_argument("-filter", required=True, help="Filter(s) you want to apply to your image", nargs='+')

args = parser.parse_args()
file , filters = args.f , args.filter
image = cv2.imread("Image/"+file+".jpg")

filter = Filter()

if "n" in filters :
    filter.negative_img(image,file)

if "s" in filters :
    filter.convert_to_sketch(image,file)

if "a" in filters :
    filter.anagylph(image , file)

print("Program Ended , all your pictures are saved in the Effects folder")
