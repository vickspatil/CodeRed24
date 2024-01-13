from PIL import Image
import piexif
picture="D:\CodeRed\img_1.jpg"
img=Image.open(picture)
exif=img._getexif()
print(exif)
