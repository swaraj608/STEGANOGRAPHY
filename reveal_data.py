from PIL import Image

def binary_to_text(binary):
    chars = [chr(int(binary[i:i+8], 2)) for i in range(0, len(binary), 8)]
    return ''.join(chars)

def xor_decrypt(text, password):
    return ''.join(chr(ord(c) ^ ord(password[i % len(password)])) for i, c in enumerate(text))

def reveal_text(image_path, password=None):
    img = Image.open(image_path)
    binary_data = ""

    pixels = list(img.getdata())
    for pixel in pixels:
        for color in pixel[:3]:  # RGB
            binary_data += str(color & 1)
    
    # Match the updated EOF marker used in hide_text.py
    eof_marker = '10101010101010101111100011110000'
    eof_index = binary_data.find(eof_marker)

    if eof_index == -1:
        raise ValueError("🚫 No hidden message found or incorrect EOF marker.")

    binary_data = binary_data[:eof_index]
    text = binary_to_text(binary_data)

    if password:
        try:
            text = xor_decrypt(text, password)
        except Exception as e:
            return f"⚠️ Decryption error: {str(e)}"
    
    return f"🔓 Hidden message: {text}"