from PIL import Image
import glob

def main_zip():
    types = ['*.png', '*.jpg']
    files_grabl = []

    for files in types:
        files_grabl.extend(glob.glob(files))

    print(f"Найденно файлов {len(files_grabl)}")
    for i in files_grabl:
        img = Image.open(i)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(f"output/{i}")
