try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract

def ocr_core(filename):
    """
    This function will handle the core OCR processing of images.
    """
    load_freq_dawg = False
    load_system_dawg = False
    img = Image.open(filename)
    new_size = tuple(2*x for x in img.size)
    img = img.resize(new_size, Image.ANTIALIAS)
    text = pytesseract.image_to_string(img)  # We'll use Pillow's Image class to open the image and pytesseract to detect the string in the image
    return text


