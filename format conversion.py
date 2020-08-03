import cv2

#lets try to directly read a grayscale image

img=cv2.imread('apple.jpg') #second method
img=cv2.resize(img,(300,300))

#conversion of image from BGR to grayscale
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#lets convert BGR to RGB

rgb=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
#lets convert BGR to HSV
hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

#first show this image using imshow method

cv2.imshow("original image",img) #this will show the original image
cv2.imshow("grayscale image",gray) #this will show a grayscale image
cv2.imshow("rgb format image",rgb) #this will show the rgb format image
cv2.imshow("hsv format image",hsv) #this will show the hsv format
cv2.waitKey(0)
cv2.destroyAllWindows()
