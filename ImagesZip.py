import zipfile
import os

def zip_directory(directory_path, zip_path):
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(directory_path):
            for file in files:
                file_path = os.path.join(root, file)
                zipf.write(file_path, os.path.relpath(file_path, directory_path))

directory_path = './'  # Replace with the actual directory path
zip_path = 'imagesall.zip'  # Replace with the desired zip file path

zip_directory(directory_path, zip_path)
