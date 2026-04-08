from ml.config import HIGH_RISK_THRESHOLD, MEDIUM_RISK_THRESHOLD

class MLModel:
    """
    Placeholder for future deep learning capabilities.
    Currently used to wrap rule-based logic to maintain structure.
    """
    def __init__(self):
        self.model = None

    def load_model(self, model_path):
        pass

    def predict(self, change_ratio):
        # Fallback to rule-based logic
        return classify_risk(change_ratio)

def classify_risk(change_ratio: float) -> str:
    if change_ratio > HIGH_RISK_THRESHOLD:
        return "high"
    elif change_ratio > MEDIUM_RISK_THRESHOLD:
        return "medium"
    return "low"
