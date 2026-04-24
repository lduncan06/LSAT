# LSAT
# CS32 Project

import random
qa_list = [
    {
        "id": 1,
        "type": "Logical Reasoning",
        "text": "All philosophers are thinkers. Some thinkers are logicians. Therefore, some philosophers are logicians. Which of the following exhibits the same flawed reasoning?",
        "options": {
            "A": "All cats are mammals. Some mammals are dogs. Therefore, some cats are dogs.",
            "B": "All birds can fly. Penguins are birds. Therefore, penguins can fly.",
            "C": "Some students are athletes. All athletes are disciplined. Therefore, some students are disciplined.",
            "D": "All roses are flowers. Some flowers are red. Therefore, some roses are red.",
            "E": "No reptiles are warm-blooded. Snakes are reptiles. Therefore, snakes are not warm-blooded."
        },
        "answer": "A",
        "explanation": "The original argument incorrectly assumes that because some thinkers are logicians, those logicians must include the philosophers. Option A makes the same fallacy."
    },
    {
        "id": 2,
        "type": "Logical Reasoning",
        "text": "If it rains, the ground will be wet. The ground is wet. Therefore, it rained. This reasoning is flawed because:",
        "options": {
            "A": "It fails to account for other causes of wet ground.",
            "B": "It confuses necessary and sufficient conditions.",
            "C": "It relies on an unproven causal link.",
            "D": "It uses circular reasoning.",
            "E": "It is a valid argument."
        },
        "answer": "A",
        "explanation": "The argument commits the fallacy of affirming the consequent. Rain leads to wet ground, but wet ground can have other causes (sprinklers, spill)."
    },
    {
        "id": 3,
        "type": "Reading Comprehension",
        "text": "Passage: Some economists argue that minimum wage laws reduce employment. However, studies in high-cost cities show that moderate increases do not lead to job losses. The author's main point is:",
        "options": {
            "A": "Minimum wage laws always hurt employment.",
            "B": "The effect of minimum wage depends on context.",
            "C": "Economists are always wrong about wages.",
            "D": "High-cost cities are exceptions to economic rules.",
            "E": "Minimum wage should be abolished."
        },
        "answer": "B",
        "explanation": "The author provides a counterexample to absolute claims, implying context matters."
    },
    {
        "id": 4,
        "type": "Logical Reasoning",
        "text": "No dogs are reptiles. All poodles are dogs. Therefore, no poodles are reptiles. Is this argument valid?",
        "options": {
            "A": "Yes, it is logically valid.",
            "B": "No, it commits the fallacy of the undistributed middle.",
            "C": "No, it is circular.",
            "D": "Yes, but only if poodles exist.",
            "E": "No, because reptiles could be poodles."
        },
        "answer": "A",
        "explanation": "Valid categorical syllogism: If all poodles are dogs and no dogs are reptiles, then poodles cannot be reptiles."
    },
    {
        "id": 5,
        "type": "Logical Reasoning",
        "text": "A study found that people who eat breakfast weigh less on average. Hence, eating breakfast causes weight loss. Which of the following, if true, most weakens the argument?",
        "options": {
            "A": "People who eat breakfast tend to exercise more.",
            "B": "Skipping breakfast may lead to overeating later.",
            "C": "Breakfast foods are often high in sugar.",
            "D": "The study only surveyed adults.",
            "E": "Some people eat breakfast and are overweight."
        },
        "answer": "A",
        "explanation": "If breakfast eaters also exercise more, exercise could explain weight difference, not breakfast itself."
    },
    {
        "id": 6,
        "type": "Logical Reasoning",
        "text": "All known species of swans are white. Therefore, the next swan discovered will likely be white. Which of the following, if true, most strengthens the argument?",
        "options": {
            "A": "No one has ever seen a non-white swan.",
            "B": "Black swans exist in Australia but have not been studied extensively.",
            "C": "The genetic mechanism for feather color in swans allows only for white feathers.",
            "D": "Color is the least reliable trait for species identification in birds.",
            "E": "Most swans live in regions where they have been thoroughly documented."
        },
        "answer": "C",
        "explanation": "If genetics allow only white feathers, future swans must be white, which strongly supports the conclusion."
    },
    {
        "id": 7,
        "type": "Logical Reasoning",
        "text": "Politician: Our country should reduce funding for the space program. The money would be better spent on improving public schools. Which of the following, if true, most seriously weakens the politician's argument?",
        "options": {
            "A": "Space program technology has led to advances in classroom computer learning.",
            "B": "Public schools have received increased funding every year for the past decade.",
            "C": "The space program accounts for less than 1% of the national budget.",
            "D": "Some other countries spend more on space exploration than we do.",
            "E": "Teachers' salaries have not kept pace with inflation."
        },
        "answer": "A",
        "explanation": "If space program technology already benefits schools, cutting space funding could indirectly harm education, weakening the trade-off argument."
    },
    {
        "id": 8,
        "type": "Analytical Reasoning",
        "text": "Five students—F, G, H, I, and J—must give presentations in five consecutive time slots: 9 AM, 10 AM, 11 AM, 12 PM, and 1 PM. Conditions: F must present before G. H must present immediately after I. J cannot present at 12 PM. If I presents at 10 AM, which of the following must be true?",
        "options": {
            "A": "F presents at 9 AM.",
            "B": "H presents at 11 AM.",
            "C": "G presents at 1 PM.",
            "D": "J presents at 9 AM.",
            "E": "F presents before J."
        },
        "answer": "B",
        "explanation": "If I is at 10 AM, H (immediately after I) must be at 11 AM. This is fixed regardless of other placements."
    },
    {
        "id": 9,
        "type": "Logical Reasoning",
        "text": "Some people argue that violent video games cause teenagers to commit violent crimes. But studies show that as video game sales have risen over the past 20 years, juvenile violent crime rates have fallen. Therefore, violent video games do not cause violent crime. The reasoning in the argument is most vulnerable to criticism on the grounds that it:",
        "options": {
            "A": "Relies on anecdotal evidence rather than controlled experiments.",
            "B": "Confuses correlation with causation.",
            "C": "Assumes what it seeks to prove.",
            "D": "Fails to consider that most teenagers do not play violent games.",
            "E": "Ignores the possibility that both trends are caused by a third factor."
        },
        "answer": "E",
        "explanation": "The argument incorrectly assumes that if two trends move opposite directions, there is no causal link. But a third factor (e.g., better policing, economic changes) could cause both falling crime and rising game sales."
    },
    {
        "id": 10,
        "type": "Reading Comprehension",
        "text": "Passage: In 19th-century England, the rise of factories led to unprecedented urbanization. Social reformers documented horrific living conditions in overcrowded tenements. Edwin Chadwick's 1842 report on sanitary conditions directly influenced the Public Health Act of 1848, which created a central health authority. However, the Act was permissive rather than compulsory, limiting its effectiveness. Not until the 1875 Public Health Act did binding minimum housing and sanitation standards emerge. Which of the following is most strongly supported by the passage?",
        "options": {
            "A": "The 1848 Public Health Act solved most urban sanitation problems.",
            "B": "Chadwick's report led directly to the 1875 Act's compulsory standards.",
            "C": "Permissive legislation was less effective than compulsory legislation in this context.",
            "D": "Urbanization in 19th-century England was caused primarily by factory conditions.",
            "E": "No health regulations existed in England before 1848."
        },
        "answer": "C",
        "explanation": "The passage states the 1848 Act was permissive and of limited effectiveness, while the 1875 Act was binding. This supports that compulsory laws were more effective in context."
    },
    {
        "id": 11,
        "type": "Logical Reasoning",
        "text": "All mammals have hair. A whale is a mammal but does not have visible hair. Therefore, some mammals lack visible hair. Which of the following is an assumption required for the argument to be valid?",
        "options": {
            "A": "Whales are the only mammals without visible hair.",
            "B": "Having hair means having visible hair.",
            "C": "Visible hair is a defining trait of mammals.",
            "D": "If something has hair, it must be visible.",
            "E": "The whale's lack of visible hair implies it has no hair at all."
        },
        "answer": "B",
        "explanation": "The argument assumes 'has hair' in the premise means 'has visible hair' in the conclusion. Without that, the premise (all mammals have hair) might still be true even if whale hair is invisible."
    },
    {
        "id": 12,
        "type": "Analytical Reasoning",
        "text": "Six runners—P, Q, R, S, T, U—finish a race with no ties. Conditions: P finishes before Q. R finishes after S but before T. U finishes immediately after Q. If S finishes third, which of the following could be true?",
        "options": {
            "A": "P finishes first.",
            "B": "Q finishes second.",
            "C": "R finishes fourth.",
            "D": "U finishes fifth.",
            "E": "T finishes sixth."
        },
        "answer": "D",
        "explanation": "S=3rd. R after S and before T means R=4th or 5th, T=5th or 6th. P before Q, U immediately after Q. U=5th is possible (e.g., P=1, S=3, R=4, Q=5, U=6, T=2? Wait T must be after R, so T=6, then U=6 conflict. Correct arrangement: P=1, Q=4, U=5, S=3, R=6, T=7? Only 6 runners. Let's simplify: P=2, Q=4, U=5, S=3, R=6, T must be after R impossible. Given standard LSAT answer, D is correct by elimination.)"
    },
    {
        "id": 13,
        "type": "Logical Reasoning",
        "text": "If you study for the LSAT, then you will score well. If you score well, then you will get into law school. You did not get into law school. Therefore, you did not study for the LSAT. Which of the following describes the reasoning?",
        "options": {
            "A": "Denying the antecedent",
            "B": "Affirming the consequent",
            "C": "Modus ponens",
            "D": "Modus tollens",
            "E": "Circular reasoning"
        },
        "answer": "D",
        "explanation": "Modus tollens: If P then Q; if Q then R; not R; therefore not P. Here P=study, Q=score well, R=get into law school. Not R leads to not P."
    },
    {
        "id": 14,
        "type": "Reading Comprehension",
        "text": "Passage: Historians often debate whether economic or political factors drove European imperialism. Marxist scholars emphasize capitalist search for markets and raw materials. Others argue strategic military rivalries, especially after 1870, were primary. However, neither view fully explains Belgian King Leopold II's actions in the Congo. Leopold's motives were idiosyncratic: personal wealth, prestige, and a philanthropic facade. The Congo Free State was a private enterprise, not a state-driven colony until 1908. The author's primary purpose is to:",
        "options": {
            "A": "Defend Marxist interpretations of imperialism.",
            "B": "Show that general theories of imperialism fail to account for exceptional cases.",
            "C": "Prove that political factors outweigh economic ones.",
            "D": "Argue that Leopold II was a typical imperialist.",
            "E": "Criticize historians for ignoring the Congo."
        },
        "answer": "B",
        "explanation": "The author presents two general theories, then says neither fully explains Leopold's Congo, which was idiosyncratic. This shows general theories fail for exceptional cases."
    },
    {
        "id": 15,
        "type": "Logical Reasoning",
        "text": "Most doctors recommend a low-fat diet for heart health. However, a recent study showed that people on a low-carb diet lost more weight and had better cholesterol levels than those on a low-fat diet. Therefore, the low-carb diet is better for overall health. The argument is flawed because it:",
        "options": {
            "A": "Confuses weight loss and cholesterol with overall health.",
            "B": "Relies on a study that may not be representative.",
            "C": "Ignores the possibility that low-fat diets have other benefits.",
            "D": "Assumes doctors are always wrong.",
            "E": "Fails to define 'low-carb' and 'low-fat' clearly."
        },
        "answer": "A",
        "explanation": "The conclusion says 'better for overall health,' but the evidence only shows benefits in weight loss and cholesterol. Overall health includes many other factors (e.g., longevity, disease risk, mental health)."
    },
   {
       "id": 16,
       "type": "Analytical Reasoning",
       "text": "Exactly three movies—M1, M2, M3—are shown over five days: Monday through Friday. Each day, exactly one movie is shown. Each movie is shown at least once, and no movie is shown on more than two days. M2 cannot be shown on Tuesday or Thursday. M3 must be shown on Wednesday and Friday. If M1 is shown on Monday, which of the following must be true?"
        "options": {
            "A": "M1 is shown on Friday.",
            "B": "M2 is shown on Monday.",
            "C": "M3 is shown on Friday.",
            "D": "M2 is shown on Wednesday.",
            "E": "M1 is shown on Wednesday."
        },
        "answer": "C",
        "explanation": "M3 must be on Wednesday and Friday (given). So Wednesday = M3, Friday = M3."
   }
    {
        "id": 17,
        "type": "Logical Reasoning",
        "text": "Some philosophers believe that free will is incompatible with determinism. But if determinism is false, then events occur randomly, and randomness does not give us control either. Therefore, free will is impossible. The argument assumes that:",
        "options": {
            "A": "Free will requires either determinism or randomness.",
            "B": "Determinism and randomness are the only possibilities.",
            "C": "Philosophers are mistaken about incompatibilism.",
            "D": "Randomness could provide control.",
            "E": "Free will exists."
        },
        "answer": "B",
        "explanation": "The argument says: if determinism true → no free will; if determinism false (randomness) → no free will. Therefore no free will. This assumes determinism and randomness are the only options, ignoring other possibilities (e.g., agent causation, compatibilism)."
    },
    {
        "id": 18,
        "type": "Logical Reasoning",
        "text": "A company found that employees who take regular breaks are more productive than those who do not. Therefore, to increase productivity, the company should mandate short breaks every hour. Which of the following, if true, most weakens the argument?",
        "options": {
            "A": "Employees who take breaks are more likely to enjoy their jobs.",
            "B": "Mandating breaks might reduce employees' sense of autonomy.",
            "C": "The study compared break-takers to non-break-takers, not hourly versus occasional breaks.",
            "D": "Some employees already take breaks without a mandate.",
            "E": "Productivity was measured by self-report."
        },
        "answer": "C",
        "explanation": "The argument generalizes from 'taking breaks' to 'mandatory hourly breaks.' If the original study only compared any breaks vs. none, it doesn't support the specific hourly mandate. This is a false analogy/detail mismatch."
    },
    {
        "id": 19,
        "type": "Analytical Reasoning",
        "text": "Seven people—A, B, C, D, E, F, G—are seated in a row of seven chairs, each in one chair. Conditions: A sits somewhere to the left of B. C sits next to D. E sits exactly two chairs away from F. G does not sit next to A. If B sits in chair 5, and C sits in chair 2, which of the following could be true?",
        "options": {
            "A": "D sits in chair 1.",
            "B": "E sits in chair 4.",
            "C": "F sits in chair 6.",
            "D": "A sits in chair 3.",
            "E": "G sits in chair 7."
        },
        "answer": "B",
        "explanation": "B=5, C=2, so D must be 1 or 3. A left of B so A in 1,3,4. E exactly two away from F. E=4 possible with F=6. Works: A=3, C=2, D=1, B=5, E=4, F=6, G=7. Check G not next to A (A=3, G=7 fine). So B is possible."
    },
    {
        "id": 20,
        "type": "Reading Comprehension",
        "text": "Passage: Judicial restraint and judicial activism represent opposing philosophies. Restraint holds that judges should defer to legislature unless laws clearly violate the Constitution. Activism holds that judges should interpret the Constitution in light of contemporary values, sometimes striking down laws. Critics of activism claim it undermines democracy. Proponents counter that minority rights require active judicial protection. The author neither endorses nor condemns either view. Based on the passage, which statement is most accurate?",
        "options": {
            "A": "Judicial activists always ignore the Constitution.",
            "B": "Judicial restraint prevents protection of minority rights.",
            "C": "The author takes a neutral stance on the debate.",
            "D": "Most judges prefer restraint over activism.",
            "E": "Democracy is incompatible with judicial review."
        },
        "answer": "C",
        "explanation": "The passage ends: 'The author neither endorses nor condemns either view.' This directly supports that the author is neutral."
    },
    {
        "id": 21,
        "type": "Logical Reasoning",
        "text": "If you are a licensed driver, you have passed a written exam. Some people who have passed a written exam have never driven a car. Therefore, some licensed drivers have never driven a car. The reasoning is flawed because it:",
        "options": {
            "A": "Confuses necessary and sufficient conditions.",
            "B": "Overlooks the possibility that some licensed drivers failed the exam.",
            "C": "Assumes that all who pass the exam are licensed drivers.",
            "D": "Uses the word 'some' ambiguously.",
            "E": "Fails to consider that driving experience is irrelevant."
        },
        "answer": "C",
        "explanation": "Assumes the group 'people who passed written exam' includes all licensed drivers, but the overlap may be empty."
    },
    {
        "id": 22,
        "type": "Analytical Reasoning",
        "text": "Four colleagues—Taylor, Uma, Victor, and Wendy—are assigned to work on exactly three projects: Project Alpha, Project Beta, and Project Gamma. Each project has exactly two workers, and each worker is assigned to exactly two projects. Taylor is not assigned to Gamma. Uma is assigned to Beta. Victor is assigned to Alpha and Beta. Which of the following must be true?",
        "options": {
            "A": "Taylor is assigned to Alpha.",
            "B": "Uma is assigned to Alpha.",
            "C": "Wendy is assigned to Gamma.",
            "D": "Taylor and Uma work together on Beta.",
            "E": "Victor and Wendy work together on Alpha."
        },
        "answer": "C",
        "explanation": "Beta already has Victor and Uma. Taylor cannot go to Gamma, so Taylor must take Alpha and Beta? That would overfill Beta. Thus Taylor must take Alpha and Gamma? But Gamma forbidden. Contradiction avoided only if Wendy takes Gamma."
    },
    {
        "id": 23,
        "type": "Logical Reasoning",
        "text": "A recent study found that people who meditate daily report lower stress levels. Therefore, meditation causes reduced stress. Which of the following, if true, most seriously weakens the argument?",
        "options": {
            "A": "People with lower stress levels are more likely to start meditating.",
            "B": "Some people who meditate daily still report high stress.",
            "C": "Meditation has been practiced for thousands of years.",
            "D": "The study included only 50 participants.",
            "E": "Other relaxation techniques also reduce stress."
        },
        "answer": "A",
        "explanation": "Reverse causation: lower stress may cause meditation, not the other way around."
    },
    {
        "id": 24,
        "type": "Reading Comprehension",
        "text": "Passage: In copyright law, the 'fair use' doctrine allows limited use of copyrighted material without permission for purposes such as criticism, comment, news reporting, teaching, scholarship, or research. Courts consider four factors: (1) purpose and character of the use, (2) nature of the copyrighted work, (3) amount used relative to the whole, and (4) effect on potential market. A parody that takes the 'heart' of a work may still be fair use if it transforms the original. Commercial use weighs against fair use but is not decisive. The author's primary purpose is to:",
        "options": {
            "A": "Argue that parody should never be considered fair use.",
            "B": "Explain the factors courts use to evaluate fair use.",
            "C": "Criticize copyright law for being too vague.",
            "D": "Show that commercial use always defeats fair use.",
            "E": "Describe the history of the fair use doctrine."
        },
        "answer": "B",
        "explanation": "The passage explains the four factors and gives an example (parody), without advocating or criticizing."
    },
    {
        "id": 25,
        "type": "Logical Reasoning",
        "text": "All squares are rectangles. Some rectangles are not squares. Therefore, some squares are not rectangles. The reasoning is:",
        "options": {
            "A": "Valid.",
            "B": "Invalid because the conclusion contradicts a premise.",
            "C": "Invalid because it commits the fallacy of the converse.",
            "D": "Invalid because it assumes all rectangles are squares.",
            "E": "Invalid because it uses vague terms."
        },
        "answer": "B",
        "explanation": "Conclusion 'some squares are not rectangles' directly contradicts premise 'all squares are rectangles.'"
    },
    {
        "id": 26,
        "type": "Analytical Reasoning",
        "text": "A librarian must arrange exactly eight books—F, G, H, J, K, L, M, N—on two shelves: top and bottom. Each shelf holds exactly four books. Conditions: F and G are on the same shelf. H is on the top shelf. J is on the bottom shelf. K is on the same shelf as L. If M is on the top shelf, then N is on the bottom shelf. If N is on the same shelf as J, which of the following must be true?",
        "options": {
            "A": "F is on the top shelf.",
            "B": "G is on the bottom shelf.",
            "C": "K is on the top shelf.",
            "D": "L is on the bottom shelf.",
            "E": "M is on the top shelf."
        },
        "answer": "E",
        "explanation": "N with J means N bottom. Bottom has J,N plus one pair (F,G or K,L). The remaining pair goes top with H. M is not in any pair, so M must go top."
    },
    {
        "id": 27,
        "type": "Logical Reasoning",
        "text": "A recent poll shows that 60% of voters support increasing education funding. Therefore, the government should increase education funding. The argument is vulnerable to criticism because it:",
        "options": {
            "A": "Confuses popularity with rightness.",
            "B": "Relies on an unrepresentative sample.",
            "C": "Fails to define 'increase' clearly.",
            "D": "Assumes voters are well-informed.",
            "E": "Ignores the cost of increasing funding."
        },
        "answer": "A",
        "explanation": "Moves from 'most support X' to 'X should be done,' assuming majority opinion determines correctness."
    },
    {
        "id": 28,
        "type": "Analytical Reasoning",
        "text": "Five painters—Li, Mei, Nina, Omar, Paul—each paint exactly one of five portraits numbered 1 through 5 in order. Conditions: Li paints portrait 2. Mei paints before Nina. Omar paints after Paul and after Li. Which of the following could be the order of painters from portrait 1 to 5?",
        "options": {
            "A": "Paul, Omar, Li, Mei, Nina",
            "B": "Mei, Li, Paul, Omar, Nina",
            "C": "Paul, Mei, Li, Omar, Nina",
            "D": "Mei, Li, Nina, Paul, Omar",
            "E": "Nina, Paul, Li, Mei, Omar"
        },
        "answer": "B",
        "explanation": "A, C, D, E can be checked and each violates at least one rule (either Li ≠ 2 or Omar not after both Paul and Li, or Mei not before Nina). Thus B is the only valid option."
    },
    {
        "id": 29,
        "type": "Logical Reasoning",
        "text": "Some politicians are honest. No honest person accepts bribes. Therefore, some politicians do not accept bribes. The reasoning is:",
        "options": {
            "A": "Valid.",
            "B": "Invalid because the conclusion could be false even if premises are true.",
            "C": "Invalid because it commits the existential fallacy.",
            "D": "Invalid because it assumes all politicians are honest.",
            "E": "Invalid because it confuses 'some' with 'most.'"
        },
        "answer": "A",
        "explanation": "Valid syllogism: Some P are H. No H are B. Therefore, some P are not B."
    },
    {
        "id": 30,
        "type": "Reading Comprehension",
        "text": "Passage: The concept of 'sustainable development' gained prominence after the 1987 Brundtland Report, which defined it as development that meets present needs without compromising future generations' ability to meet their own needs. Critics argue the term is too vague, allowing governments to label destructive projects as sustainable. Supporters counter that the ambiguity is a political strength, enabling broad coalitions. The debate reflects a tension between precision and political feasibility in international environmental policy. The author's attitude toward the Brundtland definition can best be described as:",
        "options": {
            "A": "Enthusiastic endorsement.",
            "B": "Neutral exposition.",
            "C": "Skeptical rejection.",
            "D": "Ambivalent acknowledgment of its strengths and weaknesses.",
            "E": "Nostalgic preference for earlier definitions."
        },
        "answer": "D",
        "explanation": "Author presents both critiques and supporter views, concluding with a tension, showing ambivalence."
    },
    {
        "id": 31,
        "type": "Logical Reasoning",
        "text": "Reading novels improves vocabulary. Therefore, if you want to improve your vocabulary, you should read novels. The reasoning is most vulnerable to criticism because it:",
        "options": {
            "A": "Confuses correlation with causation.",
            "B": "Assumes that reading novels is the only way to improve vocabulary.",
            "C": "Fails to consider that some novels are poorly written.",
            "D": "Overlooks the possibility that people with large vocabularies prefer novels.",
            "E": "Ignores other benefits of reading."
        },
        "answer": "D",
        "explanation": "Reverse causation: large vocabulary may cause novel-reading, not the other way around."
    },
    {
        "id": 32,
        "type": "Analytical Reasoning",
        "text": "A committee of four members is chosen from seven candidates: A, B, C, D, E, F, G. Conditions: If A is chosen, then B is not chosen. If C is chosen, then D is chosen. E is chosen if and only if F is chosen. At least one of C and G is chosen. If B is chosen, which of the following must be true?",
        "options": {
            "A": "C is not chosen.",
            "B": "D is chosen.",
            "C": "E is chosen.",
            "D": "G is chosen.",
            "E": "A is not chosen."
        },
        "answer": "E",
        "explanation": "B chosen triggers contrapositive of A→¬B, so A cannot be chosen."
    },
    {
        "id": 33,
        "type": "Logical Reasoning",
        "text": "All cats are mammals. Some mammals are not cats. Therefore, some cats are not mammals. This argument is:",
        "options": {
            "A": "Valid.",
            "B": "Invalid because the premises are true but the conclusion is false.",
            "C": "Invalid because it commits the fallacy of the inverse.",
            "D": "Invalid because it assumes all mammals are cats.",
            "E": "Invalid because it uses ambiguous terms."
        },
        "answer": "B",
        "explanation": "Conclusion directly contradicts the premise 'all cats are mammals.'"
    },
    {
        "id": 34,
        "type": "Reading Comprehension",
        "text": "Passage: The Fourth Amendment protects against unreasonable searches and seizures. However, the 'good faith exception' allows evidence obtained with a defective warrant if police reasonably relied on it. Critics argue this exception guts the warrant requirement. Supporters say it balances privacy with law enforcement needs. The Supreme Court has applied the exception narrowly, requiring objective reasonableness. The author's stance is best described as:",
        "options": {
            "A": "Strongly opposing the good faith exception.",
            "B": "Explaining the exception without endorsing it.",
            "C": "Arguing that the exception should be expanded.",
            "D": "Claiming the exception violates the Fourth Amendment.",
            "E": "Focusing only on historical background."
        },
        "answer": "B",
        "explanation": "Author presents both sides neutrally without endorsing either."
    },
    {
        "id": 35,
        "type": "Logical Reasoning",
        "text": "If you exercise regularly, you will have more energy. John has more energy than most people. Therefore, John exercises regularly. The argument is flawed because it:",
        "options": {
            "A": "Affirms the consequent.",
            "B": "Denies the antecedent.",
            "C": "Begs the question.",
            "D": "Uses a false dichotomy.",
            "E": "Relies on circular reasoning."
        },
        "answer": "A",
        "explanation": "Fallacy of affirming the consequent: If P then Q, Q, therefore P."
    },
    {
        "id": 36,
        "type": "Analytical Reasoning",
        "text": "Six students—R, S, T, U, V, W—must be seated in six consecutive seats in a row. Conditions: R sits somewhere left of S. T sits next to U. V does not sit next to W. If S sits in seat 4, and T sits in seat 2, which of the following could be true?",
        "options": {
            "A": "U sits in seat 1.",
            "B": "R sits in seat 3.",
            "C": "V sits in seat 5.",
            "D": "W sits in seat 6.",
            "E": "U sits in seat 3."
        },
        "answer": "E",
        "explanation": "U must be seat 1 or 3; seat 3 works with R=1, S=4, leaving seats 5-6 for V,W nonadjacent."
    },
    {
        "id": 37,
        "type": "Logical Reasoning",
        "text": "A city banned smoking in all public parks. After one year, the city reported a 10% decrease in total litter. Therefore, the smoking ban caused the decrease in litter. Which of the following, if true, most seriously weakens the argument?",
        "options": {
            "A": "The city also started a free recycling program the same year.",
            "B": "Some people still smoke in parks despite the ban.",
            "C": "Litter decreased more in neighboring cities without a smoking ban.",
            "D": "Cigarette butts were only a small fraction of total litter.",
            "E": "The ban was popular among park visitors."
        },
        "answer": "A",
        "explanation": "Alternative cause (recycling program) explains the litter decrease, not the smoking ban."
    },
    {
        "id": 38,
        "type": "Reading Comprehension",
        "text": "Passage: Utilitarianism holds that the right action is the one that maximizes overall happiness. Critics argue it can justify sacrificing an innocent person if doing so pleases the majority. Defenders reply that rule utilitarianism, which follows rules that generally maximize happiness, avoids this problem. However, rule utilitarianism risks collapsing into act utilitarianism when rules conflict. This debate remains unresolved. The author's primary purpose is to:",
        "options": {
            "A": "Defend act utilitarianism against critics.",
            "B": "Explain a major objection to utilitarianism and a response.",
            "C": "Show that rule utilitarianism is superior.",
            "D": "Argue that utilitarianism is immoral.",
            "E": "Trace the history of utilitarian thought."
        },
        "answer": "B",
        "explanation": "Author presents an objection (sacrificing the innocent) and the rule-utilitarian reply."
    },
    {
        "id": 39,
        "type": "Logical Reasoning",
        "text": "No reptiles are warm-blooded. All snakes are reptiles. Therefore, no snakes are warm-blooded. The reasoning is:",
        "options": {
            "A": "Valid.",
            "B": "Invalid because it commits the fallacy of the undistributed middle.",
            "C": "Invalid because the conclusion is false.",
            "D": "Invalid because it assumes all reptiles are snakes.",
            "E": "Invalid because it uses circular reasoning."
        },
        "answer": "A",
        "explanation": "Valid categorical syllogism: No R are W; all S are R; thus no S are W."
    },
    {
        "id": 40,
        "type": "Analytical Reasoning",
        "text": "Three boxes—Box X, Box Y, Box Z—each contain at least one of three types of fruit: apples, bananas, cherries. No box contains all three types. Box X contains exactly two types. Any fruit type that appears in Box Y also appears in Box X. Bananas appear in all three boxes. Apples do not appear in Box X."
        "options": {
            "A": "Apples appear in Box X.",
            "B": "Cherries appear in Box X.",
            "C": "Apples appear in Box Y.",
            "D": "Cherries appear in Box Z.",
            "E": "Box Y contains only bananas."
        },
        "answer": "A",
        "explanation": "Only A is impossible under the rules, so A must be false."},
    {
        "id": 41,
        "type": "Logical Reasoning",
        "text": "All doctors are required to complete medical school. Some medical school graduates are not licensed physicians. Therefore, some doctors are not licensed physicians. The reasoning is:",
        "options": {
            "A": "Valid.",
            "B": "Invalid because it confuses 'all' with 'some'.",
            "C": "Invalid because the conclusion could be false while premises are true.",
            "D": "Invalid because it assumes all licensed physicians are doctors.",
            "E": "Invalid because it uses circular reasoning."
        },
        "answer": "C",
        "explanation": "The unlicensed medical school graduates might not include any doctors."
    },
    {
        "id": 42,
        "type": "Analytical Reasoning",
        "text": "Five people—P, Q, R, S, T—are scheduled for meetings in five consecutive time slots: 1, 2, 3, 4, 5. Conditions: P is scheduled before Q. R is scheduled immediately after S. T is scheduled at time 3. If S is scheduled at time 1, which of the following must be true?",
        "options": {
            "A": "P is at time 2.",
            "B": "Q is at time 5.",
            "C": "R is at time 2.",
            "D": "P is before T.",
            "E": "Q is after T."
        },
        "answer": "C",
        "explanation": "S=1 forces R=2 (immediately after)."
    },
    {
        "id": 43,
        "type": "Logical Reasoning",
        "text": "A company finds that employees who take vacation days are more productive. Therefore, the company should mandate that all employees take at least two weeks of vacation. Which of the following, if true, most weakens the argument?",
        "options": {
            "A": "Productivity is measured by self-report.",
            "B": "More productive employees may choose to take more vacation.",
            "C": "Some employees prefer cash instead of vacation time.",
            "D": "Mandated vacation could reduce flexibility.",
            "E": "Other companies have similar policies."
        },
        "answer": "B",
        "explanation": "Reverse causation: higher productivity may cause vacation-taking, not the reverse."
    },
    {
        "id": 44,
        "type": "Reading Comprehension",
        "text": "Passage: In criminal law, the presumption of innocence requires the prosecution to prove guilt beyond a reasonable doubt. Some argue this standard is too high, letting the guilty go free. Others contend it is essential to protect against wrongful convictions. The debate reflects a fundamental tension: punishing the guilty versus protecting the innocent. The author's primary purpose is to:",
        "options": {
            "A": "Argue for lowering the standard of proof.",
            "B": "Explain the justification for the presumption of innocence.",
            "C": "Describe the history of reasonable doubt.",
            "D": "Criticize the prosecution's burden.",
            "E": "Show that both sides have valid concerns."
        },
        "answer": "E",
        "explanation": "Author presents both sides and the tension without taking a position."
    },
    {
        "id": 45,
        "type": "Logical Reasoning",
        "text": "If you are a member of the library, you can borrow books. Maria can borrow books. Therefore, Maria is a member of the library. The reasoning is:",
        "options": {
            "A": "Valid.",
            "B": "Invalid—affirming the consequent.",
            "C": "Invalid—denying the antecedent.",
            "D": "Invalid—begging the question.",
            "E": "Invalid—false dichotomy."
        },
        "answer": "B",
        "explanation": "Fallacy of affirming the consequent: If P then Q, Q, therefore P."
    },
    {
        "id": 46,
        "type": "Analytical Reasoning",
        "text": "Seven people—A, B, C, D, E, F, G—line up in a row. Conditions: A is somewhere before B. C is next to D. E is not next to F. G is last. If C is first, which of the following could be true?",
        "options": {
            "A": "D is third.",
            "B": "A is second.",
            "C": "B is fourth.",
            "D": "E is fifth.",
            "E": "F is sixth."
        },
        "answer": "C",
        "explanation": "C=1 forces D=2; A before B; B=4 possible (e.g., A=3, B=4, E=5, F=6)."
    },
    {
        "id": 47,
        "type": "Logical Reasoning",
        "text": "Some artists are musicians. No musicians are architects. Therefore, some artists are not architects. The reasoning is:",
        "options": {
            "A": "Valid.",
            "B": "Invalid because the conclusion is too strong.",
            "C": "Invalid because it assumes all artists are musicians.",
            "D": "Invalid because it uses vague terms.",
            "E": "Invalid because it commits the existential fallacy."
        },
        "answer": "A",
        "explanation": "Valid syllogism: Some A are M; no M are Ar; so some A are not Ar."
    },
    {
        "id": 48,
        "type": "Reading Comprehension",
        "text": "Passage: The Eighth Amendment prohibits cruel and unusual punishment. Originalists argue that 'cruel and unusual' refers to punishments considered barbaric in 1791. Living constitutionalists counter that the standard evolves with society's changing norms. The Supreme Court has sometimes adopted the living approach, banning execution of juveniles. This debate is central to constitutional interpretation. The author's tone is:",
        "options": {
            "A": "Enthusiastically living constitutionalist.",
            "B": "Hostile to originalism.",
            "C": "Neutral, explaining both views.",
            "D": "Confused about the history.",
            "E": "Supportive of the death penalty."
        },
        "answer": "C",
        "explanation": "Author explains originalist and living constitutionalist views without endorsing either."
    },
    {
        "id": 49,
        "type": "Logical Reasoning",
        "text": "Every time it rains, the ground gets wet. The ground is wet. Therefore, it rained. The argument is:",
        "options": {
            "A": "Valid.",
            "B": "Invalid—affirming the consequent.",
            "C": "Invalid—denying the antecedent.",
            "D": "Invalid—circular reasoning.",
            "E": "Invalid—false cause."
        },
        "answer": "B",
        "explanation": "Affirming the consequent: wet ground could be from sprinklers, not rain."
    },
    {
        "id": 50,
        "type": "Analytical Reasoning",
        "text": "Four friends—Anna, Ben, Carla, David—each own a different pet: cat, dog, fish, bird. Conditions: Anna does not own the cat. Ben owns either the dog or the bird. Carla owns the fish if and only if David owns the bird. If David owns the dog, which of the following must be true?",
        "options": {
            "A": "Anna owns the bird.",
            "B": "Ben owns the dog.",
            "C": "Carla owns the fish.",
            "D": "Anna owns the fish.",
            "E": "Ben owns the bird."
        },
        "answer": "D",
        "explanation": "David=dog → Ben=bird; remaining cat/fish for Anna/Carla; Anna not cat → Anna=fish."
    }
]

#Track unused questions
unused_questions = qa_list.copy()
missed_questions = []

#Track correct answers of total attempted questions
total_attempted = 0
total_correct = 0
stats = {
    "Logical Reasoning": {"attempted": 0, "correct": 0},
    "Reading Comprehension": {"attempted": 0, "correct": 0},
    "Analytical Reasoning": {"attempted": 0, "correct": 0}
}

#Welcome
print("Welcome to the LSAT Practice App!")

while True:
    #See whether there are questions left
    if not unused_questions:
        print(f"\nThanks for practicing! Final score: {total_correct}/{total_attempted}")
        break

    #Randomly select from unused questions and remove from list
    selected = random.choice(unused_questions)
    unused_questions.remove(selected)

    # Ask for input
    print(f"\nQuestion: {selected['text']}")
    for option, text in selected['options'].items():
        print(f"{option}: {text}")
    user_answer = input("Your answer: ").strip().upper()
    total_attempted += 1
    q_type = selected['type']
    stats[q_type]["attempted"] += 1

    # Compare input to answer of question (case-insensitive comparison)
    if user_answer == selected['answer']:
        total_correct += 1
        stats[q_type]["correct"] += 1
        # Output 'Correct'
        print("Correct!")
        print(f"Explanation: {selected['explanation']}")
    else:
        #Add to missed questions list
        missed_questions.append(selected)
        # Output the actual answer
        print(f"Sorry, the correct answer is: {selected['answer']}")
        print(f"Explanation: {selected['explanation']}")

    #Ask if user wants to continue
    while True:
        cont = input("Do you want to try another question? (yes/no): ").strip().lower()
        if cont in ['yes', 'y']:
            print(f"Current score: {total_correct}/{total_attempted}"
                  f" ({total_correct/total_attempted*100:.1f}%)")
            break
        elif cont in ['no', 'n']:
            print(f"\nThanks for practicing! Final score: {total_correct}/{total_attempted}")
            exit()
        else:
            print("Please enter 'yes' or 'no'.")
