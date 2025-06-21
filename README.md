# 🕵️‍♂️ Steganography Toolkit

A Python-based steganography tool to **hide and reveal secret messages in images** using **LSB (Least Significant Bit)** encoding with optional **XOR encryption**.

---

## 📌 Features

- 🔐 Hide secret messages inside images
- 🔓 Reveal hidden messages
- 🔑 Optional password-based XOR encryption
- 🧩 Simple command-line interface
- 🧪 Custom EOF marker to detect message boundaries

---

## 🖼️ Supported Image Formats

- ✅ **PNG** (recommended – lossless and ideal for steganography)
- ⚠️ **JPG/JPEG** (not recommended – lossy compression may corrupt hidden data)
- ✅ Other formats like **BMP**, **GIF** may work, but are **not officially tested**

> 🔍 **Tip:** Always use lossless formats like PNG to preserve hidden data integrity.

---

## 📁 Project Structure

stegano/
├── main.py
├── hide_data.py # Hide message into image
├── reveal_data.py # Reveal hidden message
├── utils.py # Encryption helper (SHA-256 + Fernet - currently unused)
├── flower.png # Sample input image
├── hidden.png # Image with hidden message (output)


---

## 🧠 How It Works

### Hiding a Message

1. Input an image (e.g., `flower.png`)
2. Provide a secret message and optional password
3. The message is XOR-encrypted (if password is set)
4. The message is converted to binary
5. Each bit is embedded into the LSB of RGB pixel values
6. A custom EOF marker (`10101010101010101111100011110000`) is appended
7. Result: A new image (e.g., `hidden.png`) with the secret message

### Revealing a Message

1. Input the image containing the hidden message
2. Extract binary data from the LSBs of pixel colors
3. Locate the EOF marker
4. Convert binary to text
5. If password is provided, XOR-decrypt the message

---

## 🚀 How to Run

### 🔧 Prerequisites

Install the required dependencies:

```bash
pip install pillow cryptography
▶️ Run the Tool
bash

python main.py
🧭 Menu Options
1️⃣ Hide a Message
Input image filename (e.g., flower.png)

Output image filename (e.g., hidden.png)

Secret message

Password (optional)

2️⃣ Reveal a Message
Input image with hidden message (e.g., hidden.png)

Password (if one was used during hiding)

🧪 Example
Hiding
bash

python main.py
Choose option 1

Image: flower.png

Output: hidden.png

Message: Top secret!

Password: mypassword

Revealing
bash

python main.py
Choose option 2

Image: hidden.png

Password: mypassword

Output:

scss

🔓 Hidden message: Top secret!
🛡️ Security Note
This toolkit uses XOR encryption, which is simple and not secure for serious use.

A stronger encryption option using Fernet (AES) exists in utils.py, but is not currently integrated into the main workflow.

👩‍💻 Author
Medha Swaraj
Cybersecurity Internship,2025
