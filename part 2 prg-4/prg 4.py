import cv2

# Take inputs
path = input("Enter image path: ")
angle = float(input("Enter rotation angle (e.g. 45, 90, 180): "))

# Read image
img = cv2.imread(path)

if img is None:
    print("Error: Image not found!")
else:
    # Get image dimensions
    (h, w) = img.shape[:2]
    center = (w // 2, h // 2)

    # Create rotation matrix
    matrix = cv2.getRotationMatrix2D(center, angle, 1.0)

    # Perform rotation
    rotated = cv2.warpAffine(img, matrix, (w, h))

    # Display images
    cv2.imshow("Original Image", img)
    cv2.imshow("Rotated Image", rotated)
    cv2.waitKey(0)
    cv2.destroyAllWindows()