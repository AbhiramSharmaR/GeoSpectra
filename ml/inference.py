import os
from pathlib import Path
import cv2
from ml.config import DATA_DIR
from ml.preprocessing.preprocess import load_and_preprocess
from ml.detection.detector import detect_changes, create_output_image
from ml.classification.classifier import MLModel

def run_inference(region_name: str):
    region_dir = DATA_DIR / region_name
    before_path = region_dir / "before.jpg"
    after_path = region_dir / "after.jpg"
    
    if not before_path.exists() or not after_path.exists():
        raise FileNotFoundError(f"Missing imagery for region '{region_name}'. Ensure before.jpg and after.jpg exist in {region_dir}")
    
    # Preprocessing
    before_img, before_gray = load_and_preprocess(before_path)
    after_img, after_gray = load_and_preprocess(after_path)
    
    # Detection
    mask, change_ratio = detect_changes(before_gray, after_gray)
    
    # Classification
    model = MLModel()
    classification = model.predict(change_ratio)
    
    # Visualization
    output_img = create_output_image(after_img, mask)
    
    # Save output
    output_dir = region_dir / "outputs"
    output_dir.mkdir(parents=True, exist_ok=True)
    output_path = output_dir / "result.jpg"
    cv2.imwrite(str(output_path), output_img)
    
    return {
        "change_ratio": float(change_ratio),
        "classification": classification,
        "output_image_path": str(output_path)
    }
