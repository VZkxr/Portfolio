import os
from PIL import Image

im_pack = 'Images'

list = []

for f in os.listdir(im_pack):
    name, extension = os.path.splitext(f)
    if extension in [".jpg", ".jpeg", ".png"]:
        image = Image.open(im_pack+"/"+f)
        image = image.convert('RGB')

        list.append(image)

image_1 = list[0]
list.pop(0)
image_1.save(r'PDFs/convert.pdf', save_all=True, append_images = list)