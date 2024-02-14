import cv2
import imutils
import easyocr
from collections import Counter
import utils.utils as utils
import sys

def recognize_license_plate(image_path:str = None):
    args = sys.argv
    if len(args)>1:
        image_path=args[1]
        # cv2.imread() uses forward slashes, so we replace backslashes with forward slashes in the file path
        image_path = image_path.replace("\\", "/")

    elif not image_path:
        # No path specified, so we manually select the image
        image_path=utils.open_file_dialog()

    img = cv2.imread(image_path)

    if img is None:
        print ("Error: Unable to load the image.")
        return

    # Grayscale the image
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply bilateral filter and edge detection
    bfilter = cv2.bilateralFilter(gray, 11, 17, 17)
    edge = cv2.Canny(bfilter, 30, 200)

    # Find contours
    contours = cv2.findContours(edge.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours = imutils.grab_contours(contours)
    contours = sorted(contours, key=cv2.contourArea, reverse=True)[:10]

    results = []
    reader = easyocr.Reader(['en'])

    for contour in contours:
        # Approximate the contours
        epsilon_values = [10,20]
        for epsilon in epsilon_values:
            approx = cv2.approxPolyDP(contour, epsilon, True)
            if len(approx) < 3 or len(approx) > 10:
                continue

            # Get coordinates for the license plate on the original image
            (x, y, w, h) = cv2.boundingRect(contour)
            cropped_image = gray[y:y + h, x:x + w]

            # Read text using EasyOCR
            result = reader.readtext(cropped_image)
            if len(result) != 0:
                plate = result[0][1].replace(" ", "")
                if len(plate) > 3:
                    results.append(plate)
                

    # Count occurrences of plates and find the most common one
    results_count = Counter(results)
    if len(results_count) == 0:
        return None
    plate = results_count.most_common(1)[0][0]
    return plate


def main():
    plate = recognize_license_plate()
    if plate:
        print("License Plate Number: ", plate)
    else:
        print("No license plate recognized.")

if __name__ == "__main__":
    main()