# LicensePlateReader

LicensePlateReader is a Python project designed to recognize license plates using computer vision techniques and the EasyOCR library to accurately detect and extract license plate numbers from images of vehicles.

## Features

- Utilizes computer vision techniques and the EasyOCR library for license plate recognition.
- Command-line interface for specifying image files or manually selecting them using a graphical file dialog.
- Detects and extracts license plate numbers from images.
- Supports various image formats, including JPEG, PNG, and others.

## Clone the repository

git clone https://github.com/TudorCalinCS/LicensePlateReader.git

## Install the required dependencies

OpenCV:
pip install opencv-python

imutils:
pip install imutils

EasyOCR:
pip install easyocr

## Usage

Command-line Interface:

Run the recognize_license_plate.py script with the desired image file as an argument:
python recognize_license_plate.py path/to/image.jpg

You can also use the recognize_license_plate() function directly in your Python code.

## Usage tips

For best results and improved accuracy when using LicensePlateReader, consider the following:

- Use high-quality images with clear and well-lit license plates.
- Capture license plates at close distances and avoid capturing them at extreme angles.
- Ensure that the license plate is centered within the image frame.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
If no image file is provided, the script will prompt you to manually select an image using a graphical file dialog.
