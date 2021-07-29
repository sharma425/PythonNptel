import cv2

img = cv2.imread('bullet_unclear.png')

#prepare for CLAHE(histrogram equilization technique)

clahe = cv2.createCLAHE()

#Convert to greyscale

gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)


#APPLY INHANCEMENT PROCESS
enh_image = clahe.apply(gray_img)

#save it to a file
cv2.imwrite('enhanced_img.png',enh_image)

print("Done enhancing")