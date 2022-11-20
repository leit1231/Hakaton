from PIL import Image
from PIL import ImageFilter

def shum(pict):
    src = Image.open(pict)
    src = src.convert("L")
    dst = src.filter(ImageFilter.Kernel((3, 3), (0, 1, 0, 1, -4, 1, 0, 1, 0), 1, 1))

