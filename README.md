# Simple JPEG to PNG Converter

This Python script is a simple command-line tool that **recursively** converts all JPEG images from a source folder and its subfolders into PNG format and saves them in a specified destination folder, maintaining the folder structure.

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
2.  Run the script from your terminal, providing the source and destination folders as arguments:
    ```bash
    python3 JpegToPngConverter.py <source_folder> <dest_folder>
    ```

* `<source_folder>`: The path to the folder containing your JPEG images. The script will process this folder and any subfolders it finds.
* `<dest_folder>`: The path where you want the converted PNG images to be saved. The script will automatically create this folder and the necessary subfolders if they do not already exist.

---

### 🖼️ Example

Let's say you have a folder structure like this:
```
my_photos/
├── vacation_pics/
│   ├── beach.jpeg
│   └── sunset.jpeg
└── portraits.jpeg
 ```
You can convert all these images and preserve the folder structure with a single command:
```bash
# On macOS/Linux
python3 JpegToPngConverter.py ~/Desktop/my_photos ~/Desktop/converted_images

# On Windows
python3 JpegToPngConverter.py C:\Users\YourUsername\Desktop\my_photos C:\Users\YourUsername\Desktop\converted_images
 ```

After running this command, you will have a new folder structure like this on your desktop:
 ```
converted_images/
├── vacation_pics/
│   ├── beach.png
│   └── sunset.png
└── portraits.png
 ```
