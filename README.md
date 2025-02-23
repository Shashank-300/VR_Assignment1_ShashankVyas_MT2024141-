# VR_Assignment1_ShashankVyas_MT2024141

This repository contains two Python projects as part of the VR Assignment 1:

1. **Coin Detection & Segmentation:**  
   Detects coins in an image, segments them individually, and counts the total number of coins.

2. **Panorama Creation:**  
   Creates a panorama by stitching multiple images together using keypoint detection and homography estimation.

Both projects are implemented in Python and use OpenCV, NumPy, and Matplotlib.

---

## Requirements

- **Python:**
- **OpenCV:**  
  - For coin detection and segmentation: `opencv-python`
  - For panorama creation (requires SIFT): `opencv-contrib-python`
- **NumPy**
- **Matplotlib**

You can install the required libraries using pip:

```bash
pip install opencv-python opencv-contrib-python numpy matplotlib
```
How to Run
    Coin Detection & Segmentation
python coin_detection.py

    Expects an image (defalut coinsun.jpeg) in the images/ folder (or update the path in the script).
    Outputs:
        Visual Display: Original image, detected coins, segmented coins.
        Saved Files: Segmented coin images (segmented_coin_1.png, segmented_coin_2.png, etc.).
        Console Output: Total coin count.

Panorama Creation
    python panorama.py

        Expects panroma1.jpeg, panroma2.jpeg, and panroma3.jpeg in the images/ folder (or update paths in the script).
        Outputs:
            Visual Display: Final stitched panorama.
            Saved File: stitched_result.jpg.

Methods Chosen
Coin Detection & Segmentation

    Gaussian Blurring to reduce noise.
    Canny Edge Detection to find contours.
    Contour Filtering based on area to identify coins.
    Segmentation by extracting bounding boxes for each coin.

Panorama Creation

    SIFT Keypoints & Descriptors for feature extraction.
    Brute-Force Matching to match features between images.
    Homography Estimation (RANSAC) to align and warp images.
    Image Stitching to create the final panorama.
Visual Outputs
1. Coin Detection & Segmentation

   **Original Image, Detected Coins, and Segmented Coins**
      ![image](https://github.com/user-attachments/assets/d4a99894-79d4-4403-b3a9-da6e15771308)

   **Segmented coins**
   ```
   ```
   ![image](https://github.com/user-attachments/assets/bcb4eef1-f09b-4e60-8f29-68c687c4a0bf)
      ![image](https://github.com/user-attachments/assets/9ca1b882-36f7-4577-a685-5510ae464129)
      ![image](https://github.com/user-attachments/assets/9c783508-5c59-4dd2-9e0b-647b0100e3fa)
      ![image](https://github.com/user-attachments/assets/a30bc5c5-8678-4ed0-af21-e3a1d149d8de)

3. Panorama

**Input images**

![panroma1](https://github.com/user-attachments/assets/a3558839-6f90-4ac1-9dd8-7cb0c39caa80)
![panroma2](https://github.com/user-attachments/assets/811dba34-b4b1-4638-a9c0-98f0b9fdea40)
![panroma3](https://github.com/user-attachments/assets/9c72c20f-d836-41fc-8127-6a48dbc16228)

**Stitched Image**
![image](https://github.com/user-attachments/assets/2508f2aa-5582-4ea0-ba18-f96848af7e89)

**Results & Observations**
   
   Coin Detection & Segmentation
        The code successfully detects and outlines each coin.
        Each coin is extracted as an individual image.
        The total coin count is printed in the console.
   
   Panorama Creation
        The script merges three overlapping images into a single panoramic image.
        Sufficient overlap and similar lighting conditions between the images lead to better results.
        Advanced blending techniques can be added to reduce visible seams.
