import base64
import numpy as np
from PIL import Image
import io

def convert_to_grayscale_base64(image_path: str) -> str:
    with Image.open(image_path).convert("RGB") as img:
        np_img = np.array(img)
        gray = np.mean(np_img, axis=2).astype(np.uint8)
        gray_img = Image.fromarray(gray)
        buffered = io.BytesIO()
        gray_img.save(buffered, format="PNG")
        return base64.b64encode(buffered.getvalue()).decode("utf-8")

def apply_invert_effect_base64(image_path: str) -> str:
    with Image.open(image_path).convert("RGB") as img:
        np_img = np.array(img)
        inverted = 255 - np_img
        inverted_img = Image.fromarray(inverted)
        buffered = io.BytesIO()
        inverted_img.save(buffered, format="PNG")
        return base64.b64encode(buffered.getvalue()).decode("utf-8")
