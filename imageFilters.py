import cv2

path="Lion.jpg"
originalImage=cv2.imread(path)
# print(originalImage.size)
print(originalImage.shape)

resizeImage=cv2.resize(originalImage,(500,500))
print(resizeImage.shape)

# grayScaleImage
grayImage=cv2.cvtColor(resizeImage,cv2.COLOR_BGR2GRAY)

#oilPainting
oilPaintingImage=cv2.xphoto.oilPainting(resizeImage, size=7,dynRatio=1)

#invertedImage
invertedImage=255-grayImage

#blurImage
blurImage=cv2.GaussianBlur(invertedImage, (17,17),0)
pencilSketchImage=cv2.divide(grayImage, 255-blurImage, scale=256)

cv2.imshow("Lion",resizeImage)
cv2.imshow("GrayLion", grayImage)
cv2.imshow("LionOil", oilPaintingImage)
cv2.imshow("InvertedLion", invertedImage)
cv2.imshow("BlurredLion", blurImage)
cv2.imshow("sketchLion", pencilSketchImage)

cv2.imwrite("grayScaleLion.jpg", grayImage)
cv2.imwrite("LionOil.jpg", oilPaintingImage)
cv2.imwrite("sketchLion.jpg", pencilSketchImage)
cv2.waitKey(0)