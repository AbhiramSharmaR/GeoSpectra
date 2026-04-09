import cv2
import numpy as np
import matplotlib.pyplot as plt

# load NDVI images
before = cv2.imread("ndvi_before.png", cv2.IMREAD_GRAYSCALE)
after = cv2.imread("ndvi_after.png", cv2.IMREAD_GRAYSCALE)

# compute difference
diff = after.astype(float) - before.astype(float)

# threshold (detect vegetation loss)
change = diff < -20   # negative means vegetation loss

# convert to image
change_map = np.zeros_like(before)
change_map[change] = 255

# show result
plt.imshow(change_map, cmap='gray')
plt.title("Detected Vegetation Loss")
plt.axis("off")
plt.show()

cv2.imwrite("change_map.png", change_map)

print("Change detection complete")