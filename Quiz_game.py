questions = (" How many elements are in the periodic table?: ",
             " Which animal lays the largest eggs?: " ,
             " what is the most abundant gas in Earth`s atmosphere?: ",
             " How many bones are in the human body: ",
             " which planet in the solar system is the hottest?: "
             )

options = (("A: 116", "B: 117", "C: 118", "D: 119"),
           ("A: Whale", "B: Crocodile", "C: Elephant", "D: Ostrich"),
           ("A: Nitrogen", "B: Oxygen", "C: Carbon-dioxide", "D: Hydrogen"),
           ("A: 206", "B: 207", "C: 208", "D: 209"),
           ("A: Mercury", "B: Venus", "C: Earth", "d: mars"),
           )

answer = ("C","D","A","A","B")
guesses = []
score = 0 
question_num = 0
for question in questions:
    print("---------------------------------------------")
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input("Select your answer:").upper()
    guesses.append(guess)
    if guess == answer[question_num]:
        print("--correct--")
        score +=1
    else:
        print("--incorrct--")
        print(f"{answer[question_num]} is the correct answer")

    question_num += 1

print(f"Total score is {score}")