from fastapi import File, UploadFile
from PIL import Image, ImageOps
import io


def invert_picture(file: UploadFile = File(...)):
    file_content = file.file.read()
    image = Image.open(io.BytesIO(file_content))
    inverted_image = ImageOps.invert(image)
    buff = io.BytesIO()
    inverted_image.save(buff, format='JPEG')
    buff.seek(0)
    return buff
