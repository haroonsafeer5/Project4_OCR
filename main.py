import cv2
import pytesseract

# 1. Tesseract Executable Path Set Karein
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# 2. Image Load Karein
image_path = 'sample.jpg'
image = cv2.imread(image_path)

if image is None:
    print(f"Error: Image '{image_path}' nahi mili! Check karein file folder mein majood hai.")
    exit()

# 3. Pre-Processing Pipeline (Grayscale -> Blur -> Thresholding)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (5, 5), 0)
_, processed_img = cv2.threshold(blurred, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# 4. OCR Text Extraction (Page Segmentation Mode 3)
custom_config = r'--oem 3 --psm 3'
extracted_text = pytesseract.image_to_string(processed_img, config=custom_config)

# 5. Output Result Print Karein
print("=" * 50)
print("EXTRACTED TEXT FROM IMAGE:")
print("=" * 50)
print(extracted_text if extracted_text.strip() else "[No text detected]")
print("=" * 50)

# Window par original aur processed image dikhane ke liye
cv2.imshow("Original Image", image)
cv2.imshow("Pre-Processed Image", processed_img)
cv2.waitKey(0)
cv2.destroyAllWindows()