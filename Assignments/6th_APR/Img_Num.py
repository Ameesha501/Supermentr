import cv2
import matplotlib.pyplot as plt

# Take image path from user
path = input("Enter image file path (example: sample.jpg): ")

# Load image
image = cv2.imread(path)

# Check if image exists
if image is None:
    print("❌ Image not found! Please check the path.")
else:
    print("\n✅ Image loaded successfully!\n")

    # Shape of image
    print("📌 Shape of image (Height, Width, Channels):")
    print(image.shape)

    # Pixel value at (0,0)
    print("\n📌 Pixel value at (0,0):")
    print(image[0, 0])

    # First 10 pixel values
    print("\n📌 First 10 pixel values:")
    print(image.flatten()[:10])

    # Split channels
    blue, green, red = cv2.split(image)

    print("\n📌 Channel Information:")
    print("Blue channel shape:", blue.shape)
    print("Green channel shape:", green.shape)
    print("Red channel shape:", red.shape)

    # Convert BGR → RGB for display
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Show image
    plt.imshow(image_rgb)
    plt.title("Input Image")
    plt.axis("off")
    plt.show()