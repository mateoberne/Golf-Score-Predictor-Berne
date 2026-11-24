from pathlib import Path
import joblib
import pandas as pd

FEATURES = ['driving_distance', 'fairways_hit', 'greens_in_regulation', 'total_putts', 'handicap']

class GolfPredictor:
    def __init__(self):
        self.model = joblib.load(Path(__file__).with_name('golf_model.joblib'))

    def predict(self, distance, fairways, greens, putts, handicap):
        if not (100 <= distance <= 350 and 0 <= fairways <= 14 and 0 <= greens <= 18 and 18 <= putts <= 60 and -5 <= handicap <= 54):
            raise ValueError('Statistics are outside the supported ranges.')
        data = pd.DataFrame([[distance, fairways, greens, putts, handicap]], columns=FEATURES)
        return round(float(self.model.predict(data)[0]))
