"""
The main GUI and class of the program
Saul Meredith
14/06/2024
V1: Shows the code and can use questions
"""

from tkinter import *
import json
with open("questions.json") as f:
    data = json.load(f)


FONT = ("Arial", "20")

count = 1

class MainSystem:
    def __init__(self):
        
        self.QOLframe = Frame(padx= 10, pady= 10)
        self.QOLframe.grid()

    # Heading
        self.heading = Label(self.QOLframe,
                             text= "Quiz Of Legends",
                             font= ("Arial", "36", "bold"))
        self.heading.grid(row= 0, columnspan= 2)

        questions = []
        choices = []
        self.answer = []

        


        for key, value in data.items():
            self.answered = False
            questions.append(value["question"])
            self.answer.append(value["answer"])
            choices.append(value["choice"])

        self.count = 0






        self.question = Label(self.QOLframe,
                              text= questions[self.count],
                              font= FONT)
        self.question.grid(row= 1, columnspan= 2)

        for x in choices:
            self.answers1 = Button(self.QOLframe,
                                text= choices[self.count][0],
                                font= FONT,
                                command= self.check_correct)
            self.answers1.grid(row= 2, column= 0)

            self.answers2 = Button(self.QOLframe,
                                text= choices[self.count][1],
                                font= FONT,
                                command= self.check_correct)
            self.answers2.grid(row= 2, column= 1)

            self.answers3 = Button(self.QOLframe,
                                text= choices[self.count][2],
                                font= FONT,
                                command= self.check_correct)
            self.answers3.grid(row= 3, column= 0)
            
            self.answers4 = Button(self.QOLframe,
                                text= choices[self.count][3],
                                font= FONT,
                                command= self.check_correct)
            self.answers4.grid(row= 3, column= 1)


            self.correct = Correct()

    
    def check_correct(self):
        self.QOLframe.grid_forget()
        self.correct.page_open()
        self.next_question



    def next_question(self):
        self.QOLframe = Frame()
        self.count += 1
        

class Correct:
    def __init__(self):

        self.correct_frame = Frame(padx= 10, pady= 10)

        self.w = Label(self.correct_frame,
                  text= "Idk whats going on",
                  font= FONT)
        self.w.grid(row= 0, columnspan= 2)

        self.new_question = Button(self.correct_frame,
                              text= "next question",
                              font= FONT,
                              command= self.return_to_question)
        self.new_question.grid(row= 1, columnspan= 2)
        
        
        

    def page_open(self):
        self.correct_frame.grid(padx= 10, pady= 10)

    def return_to_question(self):
        self.correct_frame.grid_forget()
        MainSystem().next_question

        





    
            


if __name__ == "__main__":
    root = Tk() 
    root.title("Quiz Of Legends")
    MainSystem()
    root.mainloop()