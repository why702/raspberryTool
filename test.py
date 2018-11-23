from PIL import Image
image = Image.open('C:/Users/hsiaoyuh_wang/Desktop/temp/2018-09-06_143506.png')
cropArea=(100,0,200,200)
image = image.crop(cropArea)
print(image)
image.show()
image = image.resize((160,160),Image.ANTIALIAS)
print(image)
image.show()