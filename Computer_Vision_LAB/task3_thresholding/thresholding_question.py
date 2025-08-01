# A pixel value = 180  
# Threshold = 150  
# Binary thresholding rule:
# - If pixel > threshold → 255
# - Else → 0

# Since 180 > 150 → New pixel value = 255

pixel_value = 180
threshold = 150

# Apply binary thresholding
new_value = 255 if pixel_value > threshold else 0
print("New pixel value:", new_value)



# Example of Thresholding
import cv2

# Load grayscale image
image = cv2.imread('../photo', 0)  # 0 = grayscale mode

# Check if image loaded
if image is None:
    print("Error loading image")
    exit()

# Apply binary thresholding
threshold_value = 150
_, binary_image = cv2.threshold(image, threshold_value, 255, cv2.THRESH_BINARY)

# Save and display the result
cv2.imwrite("binary_threshold.jpg", binary_image)
cv2.imshow("Binary Threshold", binary_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
