import cv2

# Load the original image
image = cv2.imread('../photo.jpg')  # Adjust path if needed
cv2.imshow("Original Image", image)

# Convert to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Grayscale Image", gray_image)

# Save grayscale image

cv2.imwrite('photo_gray.jpg', gray_image)

# Wait and close windows
cv2.waitKey(0)
cv2.destroyAllWindows()
