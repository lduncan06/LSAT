This code is an LSAT study practice tool.

To get started:
1. Open terminal/command prompt
2. Run: pip install flask requests
3. Then run: python server.py
4. In another terminal: python client.py

It stores a question bank of LSAT-style question and poses them to the user in random order and without repetition. The questions are stored in a dictionary that provides question number, the type of question, the question, the answer options, the correct answer, and an explanation.
Each question is multiple-choice and the computer randomly shuffles the answers before presenting them. Tt asks the user the question and prompts for answer input. It checks the user's answer against the correct answer, then tallies how many answers the user has gotten correct out of the total number of questions attempted. It gives the user feedback as to whether their answer was correct and displays their total score. It asks if they would like to continue, and provides another question if they do.


Sources:
https://flask.palletsprojects.com/en/stable/
Provides an overview of the flask web API and how to use many of its functions.
https://docs.python.org/3/library/os.html
Outline of the os module.

For this project, I used generative AI. First, I asked it to source and produce a list of 50 practice questions. For the check-in submission, I ask it to provide me with feedback as to which improvements could be made. It suggested tallying answers by question category and not just by raw score, which I then implemented.
