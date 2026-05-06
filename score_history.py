import json
import os
from datetime import datetime

class LSATScoreHistory:
    # initialise the data history director for a sertain user
    def __init__(self, user_name="default_user"):
        self.user_name = user_name
        self.data_dir = "lsat_data"
        
        # create data directory if it doesn't exist
        if not os.path.exists(self.data_dir):
            os.makedirs(self.data_dir)
        
        self.progress_file = f"{self.data_dir}/{user_name}_progress.json"
        self.scores_file = f"{self.data_dir}/{user_name}_scores.json"

    # adds the score to the record for later analytics
    def save_score_record(self, score_data):
        scores = self.load_all_scores()
        scores.append(score_data)
        with open(self.scores_file, 'w') as f:
            json.dump(scores, f)

    # load all past scores
    def load_all_scores(self):
        if os.path.exists(self.scores_file):
            with open(self.scores_file, 'r') as f:
                return json.load(f)
        return []
