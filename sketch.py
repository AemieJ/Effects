'''Convert image to sketch'''

#Importing libraries
import cv2
from PIL import Image

class effect_s(object) :
    def effect(self,img , fileName) :
        print(">>>Processing of the sketch\n")

        img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        img_blur = cv2.GaussianBlur(img_gray, (5, 5), 0, 0, cv2.BORDER_DEFAULT)
        img_blur = cv2.GaussianBlur(img_blur, (5, 5), 0, 0, cv2.BORDER_DEFAULT)
        img_blur = cv2.GaussianBlur(img_blur, (21, 21), 0, 0, cv2.BORDER_DEFAULT)
        img_blend = cv2.divide(img_gray, img_blur, scale=256)

        thresh = cv2.adaptiveThreshold(img_blend, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 9,13)
        cv2.imwrite("Effects/Sketch/"+fileName+".jpg", thresh)

        print("Press y to show you the preview of the filtered image")
        key = input()
        if key.lower() in ["y", "yes"]:
            image = Image.open("Effects/Sketch/" + fileName + '.jpg')
            image.show()
        else :
            print("Your image is saved in the Effects/Sketch folder\n")