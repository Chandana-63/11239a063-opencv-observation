# histogram_analysis.py

import cv2
import matplotlib.pyplot as plt

# Read image
img = cv2.imread("maths shapes.png")

if img is None:
    print("Image not found!")
    exit()

# -------------------- Grayscale Histogram --------------------
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

hist = cv2.calcHist([gray], [0], None, [256], [0, 256])

plt.title("Grayscale Histogram")
plt.xlabel("Pixel Intensity (0-255)")
plt.ylabel("Number of Pixels")
plt.plot(hist)
plt.xlim([0, 256])
plt.show()


# -------------------- Color Histogram --------------------
colors = ('b', 'g', 'r')
plt.title("Color Histogram")
plt.xlabel("Pixel Intensity")
plt.ylabel("Number of Pixels")

for i, col in enumerate(colors):
    hist = cv2.calcHist([img], [i], None, [256], [0, 256])
    plt.plot(hist, color=col)
    plt.xlim([0, 256])

plt.show()