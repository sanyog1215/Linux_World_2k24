import cv2
import numpy as np

def apply_filters(image_path):
    # Load the image
    image = cv2.imread(image_path)
    if image is None:
        print("Image not found.")
        return

    # Convert the image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply different filters

    # 1. Gaussian Blur
    gaussian_blur = cv2.GaussianBlur(image, (15, 15), 0)

    # 2. Median Blur
    median_blur = cv2.medianBlur(image, 15)

    # 3. Bilateral Filter
    bilateral_filter = cv2.bilateralFilter(image, 15, 75, 75)

    # 4. Edge Detection (Canny)
    edges = cv2.Canny(gray_image, 100, 200)

    # 5. Sharpening Filter
    kernel = np.array([[0, -1, 0], 
                       [-1, 5,-1], 
                       [0, -1, 0]])
    sharpened = cv2.filter2D(image, -1, kernel)

    # Display the results
    cv2.imshow("Original Image", image)
    cv2.imshow("Gaussian Blur", gaussian_blur)
    cv2.imshow("Median Blur", median_blur)
    cv2.imshow("Bilateral Filter", bilateral_filter)
    cv2.imshow("Canny Edges", edges)
    cv2.imshow("Sharpened Image", sharpened)

    # Wait for a key press and close the windows
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Example usage
image_path = 'Machine Learning\AWS_Image.png'
apply_filters(image_path)
