import requests
import random
import time

SERVER_URL = "http://localhost:5000"

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

def calculate_lsat_score(raw_score, total_questions):
    """Calculate scaled LSAT score and percentile"""
    # Get scaled score from our scale (clamp to available keys)
    scaled_score = LSAT_SCALE.get(raw_score, 120)
    
    # Get percentile
    percentile = PERCENTILES.get(scaled_score, 1.0)
    
    return scaled_score, percentile

def display_score_rubric(raw_score, total_questions, scaled_score, percentile, time_used):
    """Display professional LSAT-style score report"""
    print("\n" + "="*60)
    print("🎓 LSAT SCORE REPORT")
    print("="*60)
    
    # Raw score section
    print(f"\n📊 RAW SCORE")
    print(f"   Correct Answers: {raw_score}")
    print(f"   Total Questions: {total_questions}")
    print(f"   Raw Score: {raw_score}/{total_questions} ({raw_score/total_questions*100:.1f}%)")
    
    # Scaled score section (the one that matters for law school)
    print(f"\n🎯 SCALED SCORE (120-180 scale)")
    print(f"   ⭐ Your LSAT Score: {scaled_score}")
    
    # Visual score bar
    bar_length = 50
    score_position = int((scaled_score - 120) / 60 * bar_length)
    score_bar = "█" * score_position + "░" * (bar_length - score_position)
    print(f"   [{score_bar}]")
    print(f"   120{' ' * 20}{scaled_score}{' ' * 20}180")
    
    # Percentile rank
    print(f"\n📈 PERCENTILE RANK")
    print(f"   You scored higher than {percentile:.1f}% of test takers")
    
    # Time information
    minutes_used = int(time_used // 60)
    seconds_used = int(time_used % 60)
    print(f"\n⏱️  TIME")
    print(f"   Time used: {minutes_used}:{seconds_used:02d}")
    print(f"   Time limit: 35:00")
    
    # Score band (LSAT scores have a margin of error)
    score_band_low = scaled_score - 3
    score_band_high = scaled_score + 3
    print(f"\n🎲 SCORE BAND (90% confidence)")
    print(f"   Your true score range: {score_band_low}-{score_band_high}")
    
    # Law school admission guidance
    print(f"\n🏛️  LAW SCHOOL ADMISSION GUIDANCE")
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
    
    # Next steps based on score
    print(f"\n📚 RECOMMENDED NEXT STEPS")
    if scaled_score >= 165:
        print("   • Focus on application essays and recommendations")
        print("   • Research reach, target, and safety schools")
    elif scaled_score >= 155:
        print("   • Consider retaking to improve by 5-10 points")
        print("   • Focus on weak areas identified in review")
    else:
        print("   • Strongly consider LSAT prep course (Kaplan, Princeton Review)")
        print("   • Plan to retake in 2-3 months after intensive study")
    
    # Score improvement analysis
    print(f"\n💡 SCORE IMPROVEMENT POTENTIAL")
    if raw_score < total_questions:
        potential_max = LSAT_SCALE.get(total_questions, 180)
        points_to_gain = potential_max - scaled_score
        print(f"   • Maximum possible score: {potential_max}")
        print(f"   • Potential gain: +{points_to_gain} points")
        print(f"   • Each additional correct answer ≈ +{(points_to_gain/(total_questions-raw_score)):.1f} scaled points")
    
    print("\n" + "="*60)

def get_all_questions():
    """Ask the server for all questions"""
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
    """Ask the server if our answer is correct"""
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

def ask_question(q):
    print(f"\nQuestion {q['id']} ({q['type']}): {q['text']}")
    for option, text in q['options'].items():
        print(f"{option}: {text}")

def get_user_answer():
    while True:
        ans = input("Your answer: ").strip().upper()
        if ans in ['A', 'B', 'C', 'D', 'E']:
            return ans
        print("Please enter A, B, C, D, or E.")

def practice_mode(questions):
    print("\n" + "="*50)
    print("🎯 PRACTICE MODE")
    print("="*50)
    print("You'll get feedback after each question, and you can decide when to stop.\n")
    
    # Track stats
    total_attempted = 0
    total_correct = 0
    
    # Shuffle questions
    remaining_questions = questions.copy()
    random.shuffle(remaining_questions)
    
    while remaining_questions:
        q = remaining_questions.pop()
        
        # Ask the question
        ask_question(q)
        user_answer = get_user_answer()
        total_attempted += 1
        
        # Check with server
        result = check_answer_with_server(q['id'], user_answer)
        
        if result and result['correct']:
            total_correct += 1
            print("✅ Correct!")
        elif result:
            print(f"❌ Sorry, the correct answer is: {result['correct_answer']}")
            print(f"Explanation: {result['explanation']}")
        else:
            print("Could not verify answer with server")
        
        # Ask if they want to continue
        cont = input("\nAnother question? (yes/no): ").strip().lower()
        if cont not in ['yes', 'y']:
            break
    
    print(f"\n🎉 Final score: {total_correct}/{total_attempted} ({total_correct/total_attempted*100:.1f}%)")

def test_mode(questions):
    """Test mode: 25 random questions, 35 minute time limit, no feedback until the end"""
    print("\n" + "="*50)
    print("📝 TEST MODE")
    print("="*50)
    print("You'll have 35 minutes to answer all 25 questions.")
    print("No feedback will be given until you complete all questions.")
    print("Good luck!\n")
    
    # Select 25 random questions
    if len(questions) < 25:
        print(f"Warning: Only {len(questions)} questions available. Using all of them.")
        test_questions = questions.copy()
    else:
        test_questions = random.sample(questions, 25)
    
    # Shuffle the selected questions
    random.shuffle(test_questions)
    
    # Store user answers
    user_answers = []
    
    # Start timer
    start_time = time.time()
    time_limit = 35 * 60  # 35 minutes in seconds
    
    # Ask all questions
    for i, q in enumerate(test_questions, 1):
        # Check if time is up
        elapsed = time.time() - start_time
        if elapsed > time_limit:
            print(f"\n⏰ TIME'S UP! You've exceeded the 35-minute limit.")
            print(f"You completed {i-1} out of {len(test_questions)} questions.")
            break
        
        remaining_time = time_limit - elapsed
        minutes_remaining = int(remaining_time // 60)
        seconds_remaining = int(remaining_time % 60)
        
        print(f"\n{'='*50}")
        print(f"Question {i} of {len(test_questions)}")
        print(f"Time remaining: {minutes_remaining}:{seconds_remaining:02d}")
        print(f"{'='*50}")
        
        print(f"\n{i}. {q['text']}")  # Just shows "1. [question text]" instead of original ID
        for option, text in q['options'].items():
            print(f"   {option}: {text}")
        user_answer = get_user_answer()
        
        user_answers.append({
            'question': q,
            'user_answer': user_answer,
            'question_number': i
        })
    
    # Calculate results
    print("\n" + "="*50)
    print("📊 TEST RESULTS")
    print("="*50)
    
    total_correct = 0
    results = []
    
    for item in user_answers:
        q = item['question']
        user_answer = item['user_answer']
        
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
    
    # Display summary
    total_questions = len(user_answers)
    percentage = (total_correct / total_questions * 100) if total_questions > 0 else 0
    
    print(f"\n✅ You answered {total_questions} questions")
    print(f"🎯 Score: {total_correct}/{total_questions} ({percentage:.1f}%)")
    
    elapsed_time = time.time() - start_time
    minutes_used = int(elapsed_time // 60)
    seconds_used = int(elapsed_time % 60)
    print(f"⏱️  Time used: {minutes_used}:{seconds_used:02d}")
    
    # Display detailed results
    print("\n" + "="*50)
    print("DETAILED RESULTS")
    print("="*50)
    
    for result in results:
        status = "✅" if result['is_correct'] else "❌"
        print(f"\n{status} Q{result['question_number']} (ID: {result['id']}) - {result['type']}")
        print(f"   Your answer: {result['user_answer']}")
        if not result['is_correct']:
            print(f"   Correct answer: {result['correct_answer']}")
            print(f"   Explanation: {result['explanation']}")
    total_questions = len(user_answers)
    scaled_score, percentile = calculate_lsat_score(total_correct, total_questions)
    
    # Calculate time used
    elapsed_time = time.time() - start_time
    
    # Display LSAT scoring rubric
    display_score_rubric(total_correct, total_questions, scaled_score, percentile, elapsed_time)
    
    # Ask if they want to review wrong answers in more detail
    wrong_answers = [r for r in results if not r['is_correct']]
    if wrong_answers:
        review = input("\nWould you like to review all wrong answers? (yes/no): ").strip().lower()
        if review in ['yes', 'y']:
            print("\n" + "="*50)
            print("WRONG ANSWER REVIEW")
            print("="*50)
            for result in wrong_answers:
                print(f"\n❌ Question {result['question_number']} (ID: {result['id']}) - {result['type']}")
                # Need to fetch the full question text
                original_q = next((q for q in questions if q['id'] == result['id']), None)
                if original_q:
                    print(f"Text: {original_q['text']}")
                    for opt, txt in original_q['options'].items():
                        print(f"   {opt}: {txt}")
                print(f"Your answer: {result['user_answer']}")
                print(f"Correct answer: {result['correct_answer']}")
                print(f"Why: {result['explanation']}")
                print("-" * 40)

def choose_mode():
    """Ask user which mode they want to play"""
    print("\n" + "="*50)
    print("🎓 LSAT PRACTICE APP")
    print("="*50)
    print("\nPlease select a mode:")
    print("1. Practice Mode - Get feedback after each question, stop anytime")
    print("2. Test Mode - 25 questions, 35 minute time limit, see results at end")
    
    while True:
        choice = input("\nEnter 1 or 2: ").strip()
        if choice == '1':
            return 'practice'
        elif choice == '2':
            return 'test'
        else:
            print("Invalid choice. Please enter 1 or 2.")
            
def main():
    print("Welcome to the LSAT Practice App!")
    print("Connecting to question server...")
    
    # Get questions from the server
    all_questions = get_all_questions()
    
    if not all_questions:
        print("No questions available. Make sure the server is running!")
        return
    
    print(f"✅ Loaded {len(all_questions)} questions from server!")

    mode = choose_mode()
    
    # Run the selected mode
    if mode == 'practice':
        practice_mode(all_questions)
    else:
        test_mode(all_questions)
        
    print("\n" + "="*50)
    print("Thanks for practicing! 👋")
    print("="*50)

if __name__ == "__main__":
    main()
