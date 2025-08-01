# 10974180_LAB_WORKS


# Computer Vision Lab Works

This repository contains solutions to lab tasks on **basic image processing using OpenCV and Matplotlib**.
All work is organized into separate task folders with clean commit history and descriptive messages.

---

## 📂 Repository Structure

```
Computer_Vision_LAB/
├── photo.jpg                      # Input image for processing
├── task1_image_grayscale/         # Task 1: Image Loading & Grayscale Conversion
│   └── grayscale_conversion.py
├── task2_color_histogram/         # Task 2: Color Space Conversion & Histogram
│   └── color_spaces_and_histogram.py
├── task3_thresholding/            # Task 3: Binary Thresholding Question
│   └── thresholding_question.txt
└── README.md                      # Project documentation
```

---

## 📝 Tasks

### 🔹 Task 1: Image Loading & Grayscale Conversion

* Loads an image (`photo.jpg`)
* Converts it to grayscale
* Displays both the original and grayscale images
* Saves the grayscale image as `photo_gray.jpg` 

📁 File: `task1_image_grayscale/grayscale_conversion.py`

---

### 🔹 Task 2: Color Space Conversion & Histogram

* Loads a color image (`photo.jpg`)
* Converts the image into:

  * **Grayscale**
  * **HSV**
  * **LAB**
* Saves each converted image (`photo_grayscale.jpg`, `photo_hsv.jpg`, `photo_lab.jpg`) 
* Displays the converted images
* Plots and displays a **histogram of the grayscale image**

📁 File: `task2_color_histogram/color_spaces_and_histogram.py`

---

### 🔹 Task 3: Binary Thresholding (Theory)

**Question:**
A pixel in a grayscale image has a value of `180`. If the threshold is set to `150`, what is the new pixel value after binary thresholding?

**Answer:**
Since `180 > 150`, the new pixel value is **255**.

📁 File: `task3_thresholding/thresholding_question.py`

---

## ⚙️ Installation

Make sure you have **Python 3.10 or 3.11** installed (Python 3.13 may cause compatibility issues).

Install required libraries:

```bash
pip install opencv-python matplotlib
```

If `cv2.imshow()` gives errors in some environments (e.g., servers, VSCode remote), install headless OpenCV:

```bash
pip install opencv-python-headless matplotlib
```

---

## ▶️ Running the Scripts

1. Place `photo.jpg` in the repository root (`Computer_Vision_LAB/`).
2. Click RUN

