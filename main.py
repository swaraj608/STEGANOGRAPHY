from hide_data import hide_text
from reveal_data import reveal_text

def main():
    print("\n🕵️‍♂️ Welcome to the Steganography Toolkit!")
    print("========================================")
    print("1️⃣  Hide a message inside an image")
    print("2️⃣  Reveal a message from an image")
    choice = input("\nChoose an option (1 or 2): ")

    if choice == "1":
        print("\n🔐 Hiding Mode Activated")
        image_path = input("📁 Enter input image filename (e.g., sample.png): ")
        output_path = input("💾 Name your output image (e.g., output.png): ")
        message = input("📝 Type your hidden message: ")
        password = input("🔑 Enter a password (leave empty for no encryption): ")
        hide_text(image_path, output_path, message, password)

    elif choice == "2":
        print("\n🔎 Reveal Mode Activated")
        image_path = input("📁 Enter image filename to decode (e.g., output.png): ")
        password = input("🔑 Enter the password used to encrypt (leave empty if none): ")
        try:
            result = reveal_text(image_path, password)
            print(result)
        except Exception as e:
            print(f"⚠️ Error: {e}")

    else:
        print("🚫 Invalid choice. Please run the program again and choose 1 or 2.")

if __name__ == "__main__":
    main()