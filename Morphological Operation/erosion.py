import cv2
import numpy as np

# Read the image in grayscale
img = cv2.imread("image.jpg", cv2.IMREAD_GRAYSCALE)

# Check if image is loaded properly
if img is None:
    print("Error: Image not found!")
    exit()

# Create a kernel (structuring element)
kernel = np.ones((5, 5), np.uint8)

# Apply erosion
erosion = cv2.erode(img, kernel, iterations=1)

# Display results
cv2.imshow("Original Image", img)
cv2.imshow("Eroded Image", erosion)

# Wait for key press and close windows
cv2.waitKey(0)
cv2.destroyAllWindows()