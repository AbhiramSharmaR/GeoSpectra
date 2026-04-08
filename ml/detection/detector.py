import cv2
import numpy as np

def detect_changes(img1_gray, img2_gray, threshold=50):
    # Absolute difference between the two grayscale images
    diff = cv2.absdiff(img1_gray, img2_gray)
    
    # Thresholding
    _, mask = cv2.threshold(diff, threshold, 255, cv2.THRESH_BINARY)
    
    # Denosing mask (optional but good for robustness)
    kernel = np.ones((5,5), np.uint8)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    
    change_ratio = np.count_nonzero(mask) / mask.size
    
    return mask, change_ratio

def create_output_image(original_img, mask):
    # Create red overlay where mask is 255
    output_img = original_img.copy()
    red_overlay = np.zeros_like(original_img)
    red_overlay[:, :] = [0, 0, 255] # Red in BGR
    
    # Where mask is true, mix the original image with red
    mask_bool = mask > 0
    output_img[mask_bool] = cv2.addWeighted(original_img[mask_bool], 0.5, red_overlay[mask_bool], 0.5, 0)
    
    return output_img
