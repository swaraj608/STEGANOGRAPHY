from PIL import Image
import os

def text_to_binary(text):
    return ''.join(format(ord(c), '08b') for c in text)

def xor_encrypt(text, password):
    return ''.join(chr(ord(c) ^ ord(password[i % len(password)])) for i, c in enumerate(text))

def hide_text(image_path, output_path, secret_text, password=None):
    img = Image.open(image_path)
    if img.mode != 'RGB':
        img = img.convert('RGB')
    
    pixels = list(img.getdata())
    max_capacity = len(pixels) * 3  # Each pixel has 3 color components

    # Encrypt the message if a password is provided
    if password:
        secret_text = xor_encrypt(secret_text, password)
        print("🔑 Encryption: XOR applied")
    else:
        print("🔓 No encryption applied")
    
    # Convert to binary and add a custom EOF marker
    eof_marker = '10101010101010101111100011110000'
    binary_secret = text_to_binary(secret_text) + eof_marker

    if len(binary_secret) > max_capacity:
        raise ValueError("🚫 Message is too long for this image. Try a larger image.")

    binary_index = 0
    new_pixels = []

    for pixel in pixels:
        r, g, b = pixel
        if binary_index < len(binary_secret):
            r = (r & ~1) | int(binary_secret[binary_index])
            binary_index += 1
        if binary_index < len(binary_secret):
            g = (g & ~1) | int(binary_secret[binary_index])
            binary_index += 1
        if binary_index < len(binary_secret):
            b = (b & ~1) | int(binary_secret[binary_index])
            binary_index += 1
        new_pixels.append((r, g, b))

    img.putdata(new_pixels)
    img.save(output_path)

    print(f"✅ Secret text hidden and saved to '{output_path}'.")
    print(f"📊 Hidden {len(secret_text)} characters using {binary_index} bits.")