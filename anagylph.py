'''Anagylph''' 

#Importing libraries 
import cv2  
import numpy as np
import time
from PIL import Image
from tqdm import tqdm 

#Initialising global variable
start_lst  = []


def superimpose(blank,color,start,name) :
        global start_lst
        start_lst.append(start)
        selected_cols = []
    
        hb , wb , _ = blank.shape
        hc , wc , _ = color.shape
    
        for count in range(start,start+wc) :
            selected_cols.append(count)
    
        print("\n>>> Creating the overlay filter of "+ name)
        for row in tqdm(range(hb)) :
            for col in range(wc) :
                add = blank[row][selected_cols[col]] + color[row][selected_cols[col]-start]
            
                for i in add :
                    if i> 255 :
                        i=255
                    if i<0 :
                        i=0
                blank[row][selected_cols[col]] = add
    
        return blank

def effect(self,img,fileName) :
        global start_lst
        print(">>>Processing of the 3D retro effect\n")
        actual_h , actual_w , _  = img.shape

        print("Add amount of cyan and red filter overlay on image")
        c ,r = list(map(int,input().split()))

        red = img.copy()
        red[:,:,0] = 0
        red[:,:,1] = 0
    
        cyan = img.copy()
        cyan[:,:,2] = 0
    
        blank_img = np.zeros(shape=[actual_h,actual_w+200, 3], dtype=np.uint8)
        final_img = np.zeros(shape=[actual_h,actual_w,3],dtype=np.uint8)
    
        blank = superimpose(blank_img , cyan , start = c , name="cyan")
        blank = superimpose(blank_img , red , start = r , name="red")
        col_start = max(start_lst)
        col_end = actual_w - min(start_lst)
    
        print("\n>>> Processing the final image")
        for row in tqdm(range(actual_h)) :
             for col in range(actual_w) :
                 final_img[row][col] = blank[row][col+col_start]
        
        final_img = final_img[0:actual_h,0:0+col_end]
        cv2.imwrite("Effects/Anagylph/"+fileName+".jpg",final_img)

        print("Press y to show you the preview of the filtered image")
        key = input()
        if key.lower() in ["y", "yes"] :
            image = Image.open("Effects/Anagylph/"+fileName+'.jpg')
            image.show()

        else :
            print("Your image is saved in the Effects/Sketch folder\n")

