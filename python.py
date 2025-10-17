# backlink_analysis_features.py

class BacklinkAnalysisFeatures:
    def __init__(self):
        self.features = {
            "Backlink Strength Score": "Rate backlinks based on factors like DA, PA, and traffic.",
            "Domain Analysis": "Analyzes the domain's trustworthiness and authority.",
            "Relevance Scoring": "Measures the relevance of a backlink to your niche.",
            "Spam Detection": "Identifies backlinks from spammy or toxic sites.",
            "Competitor Comparison": "Compare your backlinks to competitors' for insights.",
            "Report Generation": "Generates detailed reports for each backlink analyzed."
        }

    def display_features(self):
        print("Backlink Analysis Features:")
        for feature, description in self.features.items():
            print(f"{feature}: {description}")

    def get_feature(self, feature_name):
        return self.features.get(feature_name, "Feature not found.")

# Example usage:
if __name__ == "__main__":
    ba_features = BacklinkAnalysisFeatures()
    ba_features.display_features()
    # To get details for a specific feature:
    print(ba_features.get_feature("Competitor Comparison"))
