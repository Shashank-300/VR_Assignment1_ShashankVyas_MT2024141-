import cv2
import numpy as np
import matplotlib.pyplot as plt

def detect_coins(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (7, 7), 0)
    edges = cv2.Canny(blurred, threshold1=50, threshold2=150)
    contours, _ = cv2.findContours(edges.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    detected_coins = image.copy()
    cv2.drawContours(detected_coins, contours, -1, (0, 255, 0), 2)

    return detected_coins, contours, edges

"""
Segmentation of Each Coin
Apply region-based segmentation to isolate individual coins
"""

def segment_coins(image, contours):

    segmented_coins = []
    coin_bound_box = image.copy()
    mask = np.zeros_like(cv2.cvtColor(image, cv2.COLOR_BGR2GRAY))

    # Thresholds for filtering
    min_area = 100
    max_area = 50000

    for idx, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        if min_area < area < max_area:
            cv2.drawContours(mask, [contour], -1, 255, thickness=cv2.FILLED)
            x, y, w, h = cv2.boundingRect(contour)

            coin_region = image[y:y+h, x:x+w]
            segmented_coins.append(coin_region)

            cv2.rectangle(coin_bound_box, (x, y), (x + w, y + h), (0, 255, 0), 2)

    return segmented_coins, coin_bound_box

"""
Count the Total Number of Coins (2 Marks)
Returns the total count of detected coins
"""

def count_coins(segmented_coins):

    return len(segmented_coins)

def result_image(original, detected, coin_bound_box, segmented_coins):
    plt.figure(figsize=(16, 6))

    plt.subplot(131)
    plt.imshow(cv2.cvtColor(original, cv2.COLOR_BGR2RGB))
    plt.title("Original Image")
    plt.axis("off")

    plt.subplot(132)
    plt.imshow(cv2.cvtColor(detected, cv2.COLOR_BGR2RGB))
    plt.title("Detected Coins")
    plt.axis("off")

    plt.subplot(133)
    plt.imshow(cv2.cvtColor(coin_bound_box, cv2.COLOR_BGR2RGB))
    plt.title("Segmented Coins")
    plt.axis("off")

    plt.show()

    for idx, coin in enumerate(segmented_coins):
        plt.figure()
        plt.imshow(cv2.cvtColor(coin, cv2.COLOR_BGR2RGB))
        plt.title(f"Segmented Coin {idx + 1}")
        plt.axis("off")
        plt.show()

        cv2.imwrite(f"segmented_coin_{idx+1}.png", coin)


if __name__ == "__main__":
    image_path = "coin3.jpeg"
    image = cv2.imread(image_path)
    if image is None:
        raise IOError(f"Could not read image: {image_path}")

    detected_image, contours, edges = detect_coins(image)

    segmented_coins, coin_bound_box = segment_coins(image, contours)

    total_coins = count_coins(segmented_coins)

    result_image(image, detected_image, coin_bound_box, segmented_coins)

    print(f"\n\nTotal number of coins detected: {total_coins}")
