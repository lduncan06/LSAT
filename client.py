import requests
import random
import time
from datetime import datetime
from score_history import LSATScoreHistory

# defines where the flask server runs
SERVER_URL = "http://localhost:5000"

#initialise global variable
score_history = None

# LSAT Scoring Scale (approximate based on typical LSAT with 25 questions)
# Real LSAT has ~100 questions, scaled 120-180
# This scale adjusts for 25 questions to a 120-180 scale
LSAT_SCALE = {
    25: 180, 24: 177, 23: 174, 22: 171, 21: 169,
    20: 167, 19: 165, 18: 163, 17: 161, 16: 159,
    15: 157, 14: 155, 13: 153, 12: 151, 11: 149,
    10: 147, 9: 145, 8: 143, 7: 141, 6: 139,
    5: 137, 4: 135, 3: 133, 2: 130, 1: 125, 0: 120
}

# Percentile equivalents (approximate for this scaled score range)
PERCENTILES = {
    180: 99.9, 177: 99.5, 174: 99.0, 171: 97.5, 169: 95.0,
    167: 90.0, 165: 85.0, 163: 80.0, 161: 75.0, 159: 70.0,
    157: 65.0, 155: 60.0, 153: 55.0, 151: 50.0, 149: 45.0,
    147: 40.0, 145: 35.0, 143: 30.0, 141: 25.0, 139: 20.0,
    137: 15.0, 135: 10.0, 133: 8.0, 130: 5.0, 125: 2.0, 120: 1.0
}

def calculate_lsat_score(raw_score):
    # get scaled score from LSAT scale or default to 120 if not found
    scaled_score = LSAT_SCALE.get(raw_score, 120)
    # get percentile from scale score or default to 1.0
    percentile = PERCENTILES.get(scaled_score, 1.0)
    return scaled_score, percentile

def display_score_rubric(raw_score, total_questions, scaled_score, percentile, time_used):
    print("\n" + "LSAT SCORE REPORT")
    # disclaimer that certain comparative data/exact scaled scoring may not be accurat
    print(" NOTE: This scoring system is an approximation")
    print("   for practice purposes. Official LSAT scoring")
    print("   varies by test administration and includes")
    print("   equating adjustments not reflected here.")
    # provides raw score information
    print(f"\n RAW SCORE")
    print(f"   Correct Answers: {raw_score}")
    print(f"   Total Questions: {total_questions}")
    # calculates raw score as a fraction and percent and prints
    print(f"   Raw Score: {raw_score}/{total_questions} ({raw_score/total_questions*100:.1f}%)")
    
    # provides scaled information
    print(f"\nSCALED SCORE (120-180 scale)")
    print(f"   Your LSAT Score: {scaled_score}")
    
    # creates a score bar that displays user's scaled score
    # estimates how the scale score compares to national average
    bar_length = 50
    # calculates where the score should be places
    score_position = int((scaled_score - 120) / 60 * bar_length)
    # fills bars below the score position dark and those above in white
    score_bar = "█" * score_position + "░" * (bar_length - score_position)
    print(f"   [{score_bar}]")
    print(f"   120{' ' * 20}{scaled_score}{' ' * 20}180")
    
    # approximates based on the scaled score percentile how they compare to other users
    # in reality LSAT scores are not linearily distributed
    print(f"\n PERCENTILE RANK")
    print(f"   You scored higher than {percentile:.1f}% of test takers")
    
    # calculates minutes used as an integer
    minutes_used = int(time_used // 60)
    # calculates additional seconds beyond the integer minute
    seconds_used = int(time_used % 60)
    # prints amount of time used out of toal available
    print(f"\n TIME")
    print(f"   Time used: {minutes_used}:{seconds_used:02d}")
    print(f"   Time limit: 35:00")
    
    # creates a 90% confidence interval score board
    # real LSAT scores use margin of error
    score_band_low = scaled_score - 3
    score_band_high = scaled_score + 3
    print(f"\n SCORE BAND (90% confidence)")
    print(f"   Your true score range: {score_band_low}-{score_band_high}")
    
    # provides score interpretation
    print(f"\n  LAW SCHOOL ADMISSION GUIDANCE")
    if scaled_score >= 170:
        print("   ★ Excellent! Competitive for Top 10 law schools (Harvard, Yale, Stanford)")
    elif scaled_score >= 165:
        print("   ★ Very Good! Competitive for Top 20 law schools")
    elif scaled_score >= 160:
        print("   ★ Good! Competitive for Top 50 law schools")
    elif scaled_score >= 155:
        print("   ★ Solid! Competitive for many accredited law schools")
    elif scaled_score >= 150:
        print("   ★ Acceptable! May need strong GPA and recommendations")
    else:
        print("   ★ Room for improvement. Consider LSAT prep courses")
    
    # gives next study/prep tips
    print(f"\n RECOMMENDED NEXT STEPS")
    if scaled_score >= 165:
        print("   • Focus on application essays and recommendations")
        print("   • Research reach, target, and safety schools")
    elif scaled_score >= 155:
        print("   • Consider retaking to improve by 5-10 points")
        print("   • Focus on weak areas identified in review")
    else:
        print("   • Strongly consider LSAT prep course (Kaplan, Princeton Review)")
        print("   • Plan to retake in 2-3 months after intensive study")
    
    # room for improvement analysis
    print(f"\n SCORE IMPROVEMENT POTENTIAL")
    if raw_score < total_questions:
        potential_max = LSAT_SCALE.get(total_questions, 180)
        points_to_gain = potential_max - scaled_score
        print(f"   • Maximum possible score: {potential_max}")
        print(f"   • Potential gain: +{points_to_gain} points")
        print(f"   • Each additional correct answer ≈ +{(points_to_gain/(total_questions-raw_score)):.1f} scaled points")
    

def get_all_questions():
    # send get request to the server url
    try:
        response = requests.get(f"{SERVER_URL}/api/questions")
        if response.status_code == 200:
            return response.json()
        else:
            print("Could not get questions from server")
            return []
    except requests.exceptions.ConnectionError:
        print("❌ Cannot connect to the server!")
        print("Make sure you're running question_server.py in another terminal")
        return []

def check_answer_with_server(question_id, user_answer):
    # send post request to server
    try:
        response = requests.post(
            f"{SERVER_URL}/api/check_answer",
            json={"question_id": question_id, "answer": user_answer}
        )
        if response.status_code == 200:
            return response.json()
        else:
            return None
    except:
        print("Error connecting to server")
        return None

def get_user_answer():
    while True:
        ans = input("Your answer: ").strip().upper()
        if ans in ['A', 'B', 'C', 'D', 'E']:
            return ans
        print("Please enter A, B, C, D, or E.")

# display analytics over time
def display_statistics_dashboard(all_questions):
    global score_history
    scores = score_history.load_all_scores()
    
    if not scores:
        print("\n Not enough scores yet. Take some tests first!")
        return
    
    print("LSAT PERFORMANCE DASHBOARD")
    
    # overall statistics
    total_tests = len(scores)
    avg_raw = sum(s['raw_score'] for s in scores) / total_tests
    avg_scaled = sum(s['scaled_score'] for s in scores) / total_tests
    best_score = max(s['scaled_score'] for s in scores)
    
    print(f"\n OVERALL STATISTICS")
    print(f"   Tests taken: {total_tests}")
    print(f"   Average score: {avg_scaled:.0f} (LSAT)")
    print(f"   Best score: {best_score} (LSAT)")
    print(f"   Average raw: {avg_raw:.1f}/25 ({avg_raw/25*100:.1f}%)")
    
    # Trend analysis (last 5 tests)
    if total_tests >= 3:
        print(f"\n PROGRESS TREND (Last 5 tests)")
        recent = scores[-5:]

        # create a bar chart showing scaled scores from last 5 tests
        for i, score in enumerate(recent, 1):
            bar = "█" * int(score['scaled_score'] / 180 * 40)
            print(f"   Test {i}: {score['scaled_score']:3d} {bar}")
        
        # calculate improvement over last 5 tests
        first_avg = sum(s['scaled_score'] for s in recent[:2]) / 2
        last_avg = sum(s['scaled_score'] for s in recent[-2:]) / 2
        improvement = last_avg - first_avg
        
        if improvement > 0:
            print(f"\n   📈 Trending UP: +{improvement:.1f} points!")
        elif improvement < 0:
            print(f"\n   📉 Trending DOWN: {improvement:.1f} points")
        else:
            print(f"\n   ➡️ Consistent performance")
    
    # time analysis
    print(f"\n TIME STATISTICS")
    avg_time = sum(s.get('time_used', 0) for s in scores) / total_tests
    avg_minutes = avg_time / 60
    print(f"   Average time: {avg_minutes:.1f} minutes")

    #provide feedback
    if avg_minutes < 30:
        print("   Fast pace - be careful not to rush!")
    elif avg_minutes > 33:
        print("   Working slowly - practice timing!")
    else:
        print("   Good pace for LSAT timing!")
    
    # projected score based on linear regression of previous scores
    if total_tests >= 3:
        n = len(score_values)
        x = list(range(1, n + 1))  # Test numbers: 1, 2, 3...
        y = score_values
        
        # calculate means
        x_mean = sum(x) / n
        y_mean = sum(y) / n
        
        # calculate slope  using linear regression
        numerator = sum((x[i] - x_mean) * (y[i] - y_mean) for i in range(n))
        denominator = sum((x[i] - x_mean) ** 2 for i in range(n))
        
        slope = numerator / denominator if denominator != 0 else 0
        
        # calculate y-intercept
        intercept = y_mean - slope * x_mean
        
        # project next test score
        next_test_num = n + 1
        next_projection = slope * next_test_num + intercept
        
        print(f"\n LINEAR REGRESSION TREND ANALYSIS")
        print(f"   Improvement rate: {slope:+.2f} points per test")
        print(f"   Trend line: Score = {slope:+.2f} × Test# + {intercept:.1f}")
        print(f"   R-squared (fit quality): {r_squared:.3f}")
        
        next_projection = recent_avg + improvement_rate
        print(f"   Next test projection: {next_projection:.0f}")
        
        if next_projection >= 170:
            print("   🌟 On track for Top 10 law schools!")
        elif next_projection >= 160:
            print("   🌟 On track for Top 50 law schools!")

# practice mode allows users to answer as many questions as they want with unlimited time 
# and get immediate feedback after each answer
def practice_mode(questions):
    print("PRACTICE MODE")
    print("You'll get feedback after each question, and you can decide when to stop.\n")
    
    # track stats
    total_attempted = 0
    total_correct = 0
    
    # shuffle questions
    remaining_questions = questions.copy()
    random.shuffle(remaining_questions)
    
    while remaining_questions:
        q = remaining_questions.pop()
        
        # ask the question
        print(f"\nQuestion {q['id']} ({q['type']}): {q['text']}")
        for option, text in q['options'].items():
            print(f"{option}: {text}")
        user_answer = get_user_answer()
        total_attempted += 1
        
        # send post request to server to check answer
        result = check_answer_with_server(q['id'], user_answer)

        # give result and feedback
        if result and result['correct']:
            total_correct += 1
            print("✅ Correct!")
        elif result:
            print(f"❌ Sorry, the correct answer is: {result['correct_answer']}")
            print(f"Explanation: {result['explanation']}")
        else:
            print("Could not verify answer with server")
        
        # ask if they want to continue
        cont = input("\nAnother question? (yes/no): ").strip().lower()
        if cont not in ['yes', 'y']:
            break
    
    print(f"\n Final score: {total_correct}/{total_attempted} ({total_correct/total_attempted*100:.1f}%)")

# test mode simulates LSAT sections
# the real LSAT consists of four 35-minute sections each with 25 multiple choice questions
# this simulates a single section
def test_mode(questions):
    global score_history
    """Test mode: 25 random questions, 35 minute time limit, no feedback until the end"""
    print("\n" + "TEST MODE")
    print("You'll have 35 minutes to answer all 25 questions.")
    print("No feedback will be given until you complete all questions.")
    print("Good luck!\n")

    # pick 25 questions and shuffle them
    test_questions = random.sample(questions, 25)
    random.shuffle(test_questions)
    
    # create list to store answers
    user_answers = []
    
    # start the timer
    start_time = time.time()
    time_limit = 35 * 60  # 35 minutes in seconds since time requires seconds
    
    # ask all questions
    # give each question a number starting with 1
    for i, q in enumerate(test_questions, 1):
        # check if time is up
        elapsed = time.time() - start_time
        if elapsed > time_limit:
            print(f"\n TIME'S UP! You've exceeded the 35-minute limit.")
            print(f"You completed {i-1} out of {len(test_questions)} questions.")
            break

        # calculate remaining time
        remaining_time = time_limit - elapsed
        minutes_remaining = int(remaining_time // 60)
        seconds_remaining = int(remaining_time % 60)
        
        print(f"Question {i} of {len(test_questions)}")
        print(f"Time remaining: {minutes_remaining}:{seconds_remaining:02d}")

        # ask question
        print(f"\n{i}. {q['text']}") 
        for option, text in q['options'].items():
            print(f"   {option}: {text}")
        user_answer = get_user_answer()

        user_answers.append({
            'question': q,
            'user_answer': user_answer,
            'question_number': i,  # Store the test question number (1-25)
            'original_id': q['id']  # Keep original ID for reference
         })
    
    # calculate results
    print(" TEST RESULTS")
    total_correct = 0
    results = []
    
    for item in user_answers:
        q = item['question']
        user_answer = item['user_answer']
        
        # check answer with server
        result = check_answer_with_server(q['id'], user_answer)
        is_correct = result['correct'] if result else False
        
        if is_correct:
            total_correct += 1
        
        results.append({
            'id': q['id'],
            'question_number': item['question_number'],
            'type': q['type'],
            'user_answer': user_answer,
            'correct_answer': q['answer'] if result else "Unknown",
            'is_correct': is_correct,
            'explanation': result['explanation'] if result else "No explanation available"
        })
    
    # display summary
    total_questions = len(user_answers)
    percentage = (total_correct / 25 * 100)
    
    # provide raw score
    print(f"\n Raw Score: {total_correct}/{total_questions} ({percentage:.1f}%)")

    # provide time used
    elapsed_time = time.time() - start_time
    minutes_used = int(elapsed_time // 60)
    seconds_used = int(elapsed_time % 60)
    print(f"  Time used: {minutes_used}:{seconds_used:02d}")

    
    # give answer and feedback for each question
    print("DETAILED RESULTS")
    
    for result in results:
        status = "✅" if result['is_correct'] else "❌"
        print(f"\n{status} Q{result['question_number']} (ID: {result['id']}) - {result['type']}")
        print(f"   Your answer: {result['user_answer']}")
        if not result['is_correct']:
            print(f"   Correct answer: {result['correct_answer']}")
            print(f"   Explanation: {result['explanation']}")
    total_questions = len(user_answers)
    scaled_score, percentile = calculate_lsat_score(total_correct)

    # display LSAT scoring rubric
    display_score_rubric(total_correct, 25, scaled_score, percentile, elapsed_time)

    # save score to history for analytics tracking
    score_data = {
            'date': datetime.now().isoformat(),
            'raw_score': total_correct,
            'scaled_score': scaled_score,
            'time_used': elapsed_time,
            'mode': 'test'
        }
    score_history.save_score_record(score_data)
    print("\n Score saved to history!")
    
# lets user choose between modes
def choose_mode():
    print("LSAT PRACTICE APP")
    print("\nPlease select a mode:")
    print("1. Practice Mode - Get feedback after each question, stop anytime")
    print("2. Test Mode - 25 questions, 35 minute time limit, see results at end")
    print("3. Statistics Analysis - Review your score history and next step")
    
    while True:
        choice = input("\nEnter a number from 1 to 3: ").strip()
        if choice == '1':
            return 'practice'
        elif choice == '2':
            return 'test'
        elif choice == '3':
            return 'statistics'
        else:
            print("Invalid choice. Please enter a number from 1 to 3.")
            
def main():
    global score_history
    print("Welcome to the LSAT Practice App!")
    print("Connecting to question server...")

    #get username for score tracking
    user_name = input("\nEnter your username: ").strip()
    if not user_name:
        user_name = "default_user"

    #initialize score tracking variable
    score_history = LSATScoreHistory(user_name)
    
    # get questions from the server
    all_questions = get_all_questions()
    
    if not all_questions:
        print("No questions available. Make sure the server is running!")
        return
        
    while True:
        mode = choose_mode()
    
        # run the selected mode
        if mode == 'practice':
            practice_mode(all_questions)
        elif mode == 'test':
            test_mode(all_questions)
        elif mode == 'statistics':
            display_statistics_dashboard(all_questions)

        # ask if user wants to continue
        cont = input("\n Return to main menu? (yes/no): ").strip().lower()
        if cont not in ['yes', 'y']:
            break

    print("Thanks for practicing!")

if __name__ == "__main__":
    main()
