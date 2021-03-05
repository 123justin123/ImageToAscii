# -*- coding: utf-8 -*-
from PIL import Image
import math, cv2

chars = ["B","S","#","&","@","$","%","*","!",":","."][::-1]
def resize(img):
    width, height = img.size
    ratio = height / width / 1.65
    new_width = 200
    new_height = ratio * new_width
    return img.resize((new_width, int(new_height)))


def image_to_ascii(path):
    img = Image.open(path)
    img = resize(img)
    width, height = img.size
    img = img.convert("L")
    pixels = img.getdata()
    characters = "".join([chars[pix*len(chars)//256] for pix in pixels])
    lg = len(characters)
    ascii_image = "\n".join([characters[i:i+width] for i in range(0, lg, width)])
    with open("result.txt", "w") as f:
        f.write(ascii_image)
    return ascii_image
            
def frame_to_ascii(img):
    img = resize(img)
    width, height = img.size
    grey_img = img.convert("L")
    pixels = grey_img.getdata()
    characters = "".join([chars[pix * len(chars) // 256] for pix in pixels])
    lg = len(characters)
    ascii_image = "\n".join([characters[i:i+width] for i in range(0, lg, width)])
    print(ascii_image)
    

   
def video_ascii(video = 0):   
    cap = cv2.VideoCapture(video)
    while True:  
        ret, frame = cap.read()
        if ret:
            frame_to_ascii(Image.fromarray(frame))
            cv2.waitKey(10)
        else:
            break



test = [[1,2,3],[4,5,6]]
print(test[1])