from PIL import Image
image = Image.open('C:/Users/hsiaoyuh_wang/Desktop/temp/2018-09-06_143506.png')
cropArea=(0,0,20,20)
image = image.crop(cropArea)
print(image)
image.show()
image = image.resize((160,160),Image.ANTIALIAS)
print(image)
image.show()