import PIL
import os
import os.path
from PIL import Image

f = r'/home/tauhid/jayed/sg2/data/RaFD/'
for file in os.listdir(f):
    f_img = f+"/"+file
    img = Image.open(f_png)
    img = img.resize((256,256))
    img.save(f_png)
