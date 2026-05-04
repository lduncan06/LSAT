import requests
import random

# The address of our Flask server (like a restaurant address)
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

def main():
    print("Welcome to the LSAT Practice App!")
    print("Connecting to question server...")
    
    # Get questions from the server
    all_questions = get_all_questions()
    
    if not all_questions:
        print("No questions available. Make sure the server is running!")
        return
    
    print(f"✅ Loaded {len(all_questions)} questions from server!")
    
    # Track stats
    total_attempted = 0
    total_correct = 0
    
    # Shuffle questions
    remaining_questions = all_questions.copy()
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
    
    print(f"\n🎉 Final score: {total_correct}/{total_attempted}")

if __name__ == "__main__":
    main()
