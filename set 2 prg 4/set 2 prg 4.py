# edge_detection.py

import cv2

# Read the image
img = cv2.imread("maths shapes.png")

if img is None:
    print("Image not found!")
    exit()

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply Gaussian blur before edge detection
blur = cv2.GaussianBlur(gray, (5, 5), 0)

# Perform Canny edge detection
edges = cv2.Canny(blur, 50, 150)

# Display images
cv2.imshow("Original", img)
cv2.imshow("Gray", gray)
cv2.imshow("Edges (Canny)", edges)

cv2.waitKey(0)
cv2.destroyAllWindows()