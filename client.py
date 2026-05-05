import requests
import random
import time

SERVER_URL = "http://localhost:5000"

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

def practice_mode(question):
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
        
        ask_question(q)
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
