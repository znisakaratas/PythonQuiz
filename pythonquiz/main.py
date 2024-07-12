import cv2 as cv
from matplotlib import pyplot as plt
#taking file name as first command line argument
img = cv.imread("cityimageinp.jpg",cv.IMREAD_GRAYSCALE)
assert img is not None, "file could not be read, check with os.path.exists()"

#Blurring the image for preventing noises
image = cv.GaussianBlur(img, (3, 3), 0)

#Specifying edges with using canny
edges = cv.Canny(image,100,200)

#Showing the pictures side by side
plt.subplot(121), plt.imshow(image, cmap='gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(edges, cmap='gray')
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
plt.show()

