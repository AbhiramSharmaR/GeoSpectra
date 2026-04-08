import os
from datetime import datetime
from ml.inference import run_inference
from ml.report import generate_report

class AnalysisService:
    @staticmethod
    def get_available_regions():
        data_dir = "ml/data"
        if not os.path.exists(data_dir):
            return []
        
        regions = []
        for d in os.listdir(data_dir):
            if os.path.isdir(os.path.join(data_dir, d)):
                regions.append(d)
        return regions

    @staticmethod
    def perform_analysis(region: str) -> dict:
        # Run ML inference
        inference_result = run_inference(region)
        
        # Generate the structured report
        report = generate_report(region, inference_result)
        
        # Compile result object for the DB
        return {
            "region": region,
            "change_ratio": inference_result["change_ratio"],
            "classification": inference_result["classification"],
            "report": report,
            "output_image_path": inference_result["output_image_path"],
            "timestamp": datetime.utcnow()
        }
