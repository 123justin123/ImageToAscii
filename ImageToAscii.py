# -*- coding: utf-8 -*-
from PIL import Image
import math
import cv2
import argparse

chars = ["B", "S", "#", "&", "@", "$", "%", "*", "!", ":", "."][::-1]


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
    ascii_image = "\n".join([characters[i:i+width]
                            for i in range(0, lg, width)])
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
    ascii_image = "\n".join([characters[i:i+width]
                            for i in range(0, lg, width)])
    print(ascii_image)


def video_ascii(video=0):
    cap = cv2.VideoCapture(video)
    while True:
        ret, frame = cap.read()
        if ret:
            frame_to_ascii(Image.fromarray(frame))
            cv2.waitKey(10)
        else:
            break

def test():
    print("test")

parser = argparse.ArgumentParser()
parser.add_argument('-i', '--input', help="Chemin de l'image")
parser.add_argument('-c', action='store_true', help="Convertir l'image de la caméra")
args = parser.parse_args()

if(args.input):
    image_to_ascii(args.input)

if(args.c):
    video_ascii()