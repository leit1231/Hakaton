import cv2
import pytesseract
from decoder import export
from decoder import bynory_pict
from zip_images import main_zip
from anti_shum import shum
from zip_text import zip

def runner():
    pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

    pict = input('Напиши название фотки:')
    shum(pict)

    export(bynory_pict(pict))
    img = cv2.imread(pict)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    config = r"--oem 3 --psm 6 "

    text = pytesseract.image_to_string(img, lang='rus+eng', config=config)
    print(text.strip())


    # cv2.imshow('Result', img)
    # cv2.waitKey(0)
    f = open('text_from_image.txt', 'w+')
    f.seek(0)
    f.close()
    with open('text_from_image.txt', 'a', encoding="utf-8") as f:
        f.write(text.strip()+"\n")

    main_zip()
    zip()

runner()