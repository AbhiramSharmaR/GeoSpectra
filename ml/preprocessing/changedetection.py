import cv2
import numpy as np
import matplotlib.pyplot as plt

# load NDVI images
before = cv2.imread("ndvi_before.png", cv2.IMREAD_GRAYSCALE)
after = cv2.imread("ndvi_after.png", cv2.IMREAD_GRAYSCALE)

# compute difference
diff = after.astype(float) - before.astype(float)

# detect vegetation loss
change = diff < -20

# create map
change_map = np.zeros_like(before)
change_map[change] = 255

cv2.imwrite("change_map.png", change_map)

print("Saved as change_map.png")

# force display using cv2
cv2.imshow("Change Map", change_map)
cv2.waitKey(0)
cv2.destroyAllWindows()