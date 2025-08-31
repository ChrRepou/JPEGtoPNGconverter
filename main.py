from PIL import Image
import sys
from pathlib import Path

def jpeg_to_png():
    try:
        source_folder = sys.argv[1]
        dest_folder = sys.argv[2]
        try:
            source_path = Path(source_folder)
            for imageFile in source_path.iterdir():
                if imageFile.is_dir():
                    continue
                img = Image.open(imageFile)
                try:
                    dest_path = Path(dest_folder)
                    if not dest_path.exists():
                        dest_path.mkdir(parents=True, exist_ok=True)
                    if dest_path.is_dir():
                        img.save(dest_path / imageFile.with_suffix('.png').name)
                except FileExistsError as err:
                    print(err)
                    break
        except FileNotFoundError as err:
            print(err)
    except IndexError:
        print('Usage: python3 JpegToPngConverter.py source_folder dest_folder')
    except Exception as err:
        print(err)

if __name__ == '__main__':
    jpeg_to_png()