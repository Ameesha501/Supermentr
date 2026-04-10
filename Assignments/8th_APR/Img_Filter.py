import cv2
import matplotlib.pyplot as plt

# Take image path from user
path = input("Enter image path (example: sample.jpg): ")

# Load image
image = cv2.imread(path)

if image is None:
    print("❌ Image not found! Check the path.")
else:
    print("✅ Image loaded successfully!\n")

    # Convert BGR to RGB (for display)
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # 1. Grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # 2. Blur
    blur = cv2.GaussianBlur(image, (7, 7), 0)

    # 3. Edge Detection
    edges = cv2.Canny(image, 100, 200)

    # Show all images
    plt.figure(figsize=(10,8))

    plt.subplot(2,2,1)
    plt.imshow(image_rgb)
    plt.title("Original Image")
    plt.axis("off")

    plt.subplot(2,2,2)
    plt.imshow(gray, cmap='gray')
    plt.title("Grayscale")
    plt.axis("off")

    plt.subplot(2,2,3)
    plt.imshow(cv2.cvtColor(blur, cv2.COLOR_BGR2RGB))
    plt.title("Blur Image")
    plt.axis("off")

    plt.subplot(2,2,4)
    plt.imshow(edges, cmap='gray')
    plt.title("Edge Detection")
    plt.axis("off")

    plt.tight_layout()
    plt.show()