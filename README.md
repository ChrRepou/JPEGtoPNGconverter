# Simple JPEG to PNG Converter

This Python script is a simple command-line tool that converts all JPEG images from a source folder into PNG format and saves them in a specified destination folder.

---

### 🚀 Getting Started

#### Prerequisites

* **Python 3.x**
* The **Pillow** library. You can install it using `pip`:
    ```bash
    pip install Pillow
    ```

#### Usage

1.  Save the code as a Python file, for example, `JpegToPngConverter.py`.
2.  Run the script from your terminal (OR from your IDE), providing the source and destination folders as arguments:
    ```bash
    python3 JpegToPngConverter.py <source_folder> <dest_folder>
    ```

* `<source_folder>`: The path to the folder containing your JPEG images.
* `<dest_folder>`: The path where you want the converted PNG images to be saved. The script will automatically create this folder if it doesn't already exist.

---

### 🖼️ Example

Let's say you have a folder called `images` on your desktop with a file named `photo.jpeg`. You want to convert it to a PNG and save it in a new folder called `converted_images`.

```bash
# On macOS/Linux
python3 JpegToPngConverter.py ~/Desktop/images ~/Desktop/converted_images

# On Windows
python3 JpegToPngConverter.py C:\Users\YourUsername\Desktop\images C:\Users\YourUsername\Desktop\converted_images
