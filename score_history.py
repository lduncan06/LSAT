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

    # save current score for test mode to pause and resume later
    def save_test_progress(self, test_state):
        test_state['saved_at'] = datetime.now().isoformat()
        test_state['user'] = self.user_name

        # open progress file in writing mode
        with open(self.progress_file, 'w') as f:
            # save current state as json object attributed to the user
            json.dump(test_state, f)
        print(f"Progress saved! You can resume later.")

  
    def load_test_progress(self):
      # if the file path exists, open in reading mode and return the data
        if os.path.exists(self.progress_file):
            with open(self.progress_file, 'r') as f:
                progress = json.load(f)
            # auto deletes progress to make room for a new save
            os.remove(self.progress_file)
        return progress

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
