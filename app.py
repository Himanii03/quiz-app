#dictionary-json
#make a quiz app.. it displays questions
# user chooses option
# increments score if it correct 
# 3/5
# streamlit or flask 
import json

class QuizApp:

    def __init__(self,questions_file):
        self.questions_file=questions_file #stores the file name
        self.questions=self.load_questions() # stores all the questions
        self.score=0 

    def load_questions(self):
        ''' It loads questions from our JSON file'''
        #load our json file and questions
        try:
            with open(self.questions_file,"r") as file:
                return json.load(file) # it converts json to dictionary 
                #json.dump() -dictionary to json
        except Exception as e:
            print(e)
            return []

    def ask_questions(self,question):
        '''Ask a single question
        User's output
     What is the capital of france?
     1. Paris
     2. Berlin
     3. Rome
     4. Madrid
     Enter your choice (1/2/3/4)
     berlin==paris wrong '''
    #     question= {
    #     "question": "What is the capital of France?",
    #     "options": ["Paris", "Berlin", "Rome", "Madrid"],[0,1,2,3]
    #     "answer": "Paris"
    # },
    # User's output
    # what is the capital of france?

        print(f"\n{question['question']}")
        for i,option in enumerate(question["options"],1):
            print(f"{i}. {option}")
        choice=int(input( "Enter your choice (1/2/3/4)"))
        return question['options'][choice-1]== question['answer'] 
                #question['options'][4-1] questions['options'][3]=Madrid
                # question['answer']=Paris
                #return Madrid==Paris False 

    def start_quiz(self):
        ''' Start the quiz'''
        
        if not self.questions: 
            print("No questions are available")
            return
        
        print("\nWelcome to the quiz")
        for question in self.questions:
            if self.ask_questions(question): 
                print("Correct! ")
                self.score+=1
            else:
                print(f"Wrong! The correct answer is {question['answer']}")
        
        print(f"\n Quiz over! Your score is {self.score}/{len(self.questions)}")


if __name__=="__main__":
    quiz=QuizApp("data.json")
    quiz.start_quiz()