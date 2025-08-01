import cv2
import matplotlib.pyplot as plt

# Load color image
image = cv2.imread('../photo.jpg')  # Adjust path if needed
if image is None:
    print("Error: Could not load image '../photo.jpg'")
    exit()

# Convert to Grayscale, HSV, LAB
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
lab = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)

# Save each image
cv2.imwrite("photo_gray.jpg", gray)
cv2.imwrite("photo_hsv.jpg", hsv)
cv2.imwrite("photo_lab.jpg", lab)

# Display converted images
cv2.imshow("Grayscale", gray)
cv2.imshow("HSV", hsv)
cv2.imshow("LAB", lab)

# Plot grayscale histogram and save it
plt.figure()
plt.title("Grayscale Histogram")
plt.xlabel("Pixel value")
plt.ylabel("Frequency")
plt.hist(gray.ravel(), bins=256, range=[0,256], color='gray')
plt.grid(True)

# Save the histogram plot as an image file (you can use .jpg, .png, etc.)
plt.savefig("grayscale_histogram.png")

# Now display it
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()
