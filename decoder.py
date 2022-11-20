from base64 import b64encode as enc64
from base64 import b64decode as nc64
from io import BytesIO
from PIL import Image


def bynory_pict(pict: str) -> str:
    with open(pict, 'rb') as f:
        bynory = enc64(f.read())
    return bynory


def export(bynory):
    image = BytesIO(nc64(bynory))
    pillow = Image.open(image)
    x = pillow.show()
