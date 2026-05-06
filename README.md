This code is an LSAT study practice tool.

To get started:
1. Open terminal/command prompt
2. Run: pip install flask requests
3. Then run: python server.py
4. In another terminal: python client.py

This LSAT practice application is a client-server system that simulates real LSAT testing conditions while tracking user performance over time. The server (server.py) uses Flask to create a REST API that stores 50 LSAT-style questions covering Logical Reasoning, Reading Comprehension, and Analytical Reasoning. When started, the server listens for HTTP requests on localhost:5000 and provides three endpoints: one to retrieve all questions (/api/questions), one to get a specific question by ID (/api/questions/<id>), and one to check answers (/api/check_answer). The server maintains a static list of questions, each containing the question text, answer options, correct answer, and an explanation. This separation of concerns allows the server to run independently and serve multiple clients simultaneously, making it scalable for classroom use.

The client (client.py) connects to this server and provides three main modes. Practice Mode shuffles all questions and allows users to answer at their own pace, receiving immediate feedback and explanations after each answer. Test Mode randomly selects 25 questions, enforces a 35-minute timer (matching a real LSAT section), and provides no feedback until the end, at which point it displays a comprehensive score report including raw score, scaled LSAT score (120-180), percentile rank, and a 90% confidence band. The scoring system uses an approximate LSAT scale where a perfect score of 25 correct converts to 180, with proportional scaling in between. Statistics Mode loads all previous test scores from JSON files and displays a detailed analytics dashboard showing overall statistics, progress trends with bar charts, time analysis, and linear regression projections that calculate improvement rate and predict future scores. A separate score_history module handles persistent data storage, saving each test's date, raw score, scaled score, and time used to user-specific JSON files. This allows users to track their improvement over multiple practice sessions and identify weak areas through flagged questions and performance breakdowns by question type. The entire system demonstrates practical applications of API communication, data persistence, statistical analysis, and timed testing conditions—all essential skills beyond basic Python programming.

Sources:
https://flask.palletsprojects.com/en/stable/
Provides an overview of the flask web API and how to use many of its functions.
https://docs.python.org/3/library/os.html
Outline of the os module.
https://www.geeksforgeeks.org/python/use-jsonify-instead-of-json-dumps-in-flask/
Explains the jsonify function in Flask
https://www.lsac.org/lsat/lsat-scoring
Information about LSAT scoring
https://www.princetonreview.com/law/lsat-sections
Information about LSAT structure

For this project, I used generative AI. First, I asked it to source and produce a list of 50 practice questions. For the check-in submission, I ask it to provide me with feedback as to which improvements could be made. It suggested tallying answers by question category and not just by raw score, which I then implemented. I also had it generate most of the "feedback text," such as the messages that tell the user, based on their scaled score, what their prospects for certain law schools might look like. I also had it help with trouble shooting and finding small errors in my code that I was struggling to find myself.
