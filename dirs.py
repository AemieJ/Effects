'''Making all the directories for storing the filtered images'''

#Importing libraries
import os

os.makedirs("Effects")

filters = ["Anagylph" , "Negative" , "Sketch"]

for filter in filters :
    os.makedirs("Effects/"+filter)