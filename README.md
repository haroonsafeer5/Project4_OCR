# Project 4: Image Text Recognition (OCR)

This project implements an Image Text Recognition pipeline using OpenCV and Tesseract OCR in Python.

## Features & Pre-processing Pipeline
1. **Image Loading**: Loads raw input image (`sample.jpg`).
2. **Grayscale Conversion**: Converts BGR image to 1D intensity matrix to eliminate color noise.
3. **Noise Reduction**: Applies Gaussian Blur to remove micro-imperfections.
4. **Otsu Binarization**: Creates a high-contrast black and white image for optimal OCR text detection.
5. **OCR Extraction**: Uses `pytesseract` with Page Segmentation Mode 3 (`--psm 3`) to extract text.

## Project Structure
* `main.py` - Main execution script containing image pre-processing and OCR logic.
* `sample.jpg` - Input image containing text.
* `1.JPG` & `2.JPG` - Visual output screenshots of pre-processed images and terminal results.

## Setup & Execution
1. Install Tesseract OCR Engine on Windows.
2. Install required dependencies:
   ```bash
   pip install opencv-python pytesseract numpy
