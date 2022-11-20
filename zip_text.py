import lzma

def zip():
    with open("text_from_image.txt", 'rb') as file:
        text = file.read()

    data = text

    with lzma.open("file.xz", "w") as f:
        f.write(data)
zip()