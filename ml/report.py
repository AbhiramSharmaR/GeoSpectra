def generate_report(region: str, result: dict) -> str:
    change_ratio = result.get("change_ratio", 0.0)
    classification = result.get("classification", "low")
    
    if classification == "high":
        reason = f"Significant vegetation or structural changes detected via change mask (change ratio: {change_ratio:.2%})."
        recommendation = "Immediate investigation and field validation recommended."
    elif classification == "medium":
        reason = f"Moderate changes observed in the change mask (change ratio: {change_ratio:.2%})."
        recommendation = "Monitor area closely and schedule future assessments."
    else:
        reason = f"Minimal or no changes detected (change ratio: {change_ratio:.2%})."
        recommendation = "No immediate action required."

    report = f"""Region name: {region}
Change level: {change_ratio:.2%}
Risk level: {classification.upper()}
Reason: {reason}
Recommendation: {recommendation}"""
    
    return report
