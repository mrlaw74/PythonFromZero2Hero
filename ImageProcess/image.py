from PIL import Image, ImageFilter
img = Image.open("./image/image.jpg")
img.show()
# print(im)
filterImg = img.filter(ImageFilter.BLUR)
# filterImg.save("blur.png", 'png')
filterImg.show()