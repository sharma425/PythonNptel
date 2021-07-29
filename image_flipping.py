# -*- coding: utf-8 -*-
"""
Created on Tue Apr 13 16:05:24 2021

@author: Keshav
"""

from PIL import Image
img = Image.open("flipped_newspaper.png")

#transposing
transposed_img = img.transpose(Image.FLIP_LEFT_RIGHT)

#compiled in human understandable format
transposed_img.save("corrected.png")

print("done flipping")