from tkinter import *
from tkinter import *
import json
with open("questions.json") as f:
    data = json.load(f)

main_font = ("Candara", "20")
heading = ("Goudy Stout", "25", "bold")
points = []
question_amount = []

class Introduction:
    def __init__(self):

        self.intro_frame = Frame()
        self.intro_frame.grid(padx= 10, pady= 10)

        self.heading = Label(self.intro_frame,
                             text= "Quiz of Legends",
                             font= ("Goudy Stout", "30", "bold")).grid(row= 0, columnspan = 2)

        instructions = ("For millenia people have tried their knowledge and failed this very quiz.\n"
                        "Many individuals falter under the sheer right to be called a legend.\n"
                        "Do you have what it takes to be granted this title?\n"
                        "Or will you falter like the latter?")

        self.message = Label(self.intro_frame,
                             text= instructions,
                             font= main_font).grid(row= 1, columnspan= 2)

        self.start_button = Button(self.intro_frame,
                            text= "Run the gauntlet",
                            font= main_font,
                            width= 15,
                            command= self.start).grid(row= 2, column= 0)


        self.falter = Button(self.intro_frame,
                             text= "Falter like the rest",
                             font= main_font,
                             width= 15,
                             command= root.destroy).grid(row= 2, column= 1)
        self.mainmenu = MainMenu()

    def start(self):
        self.intro_frame.grid_forget()
        self.mainmenu.open_page()

class MainMenu:
    def __init__(self):
        self.mainframe = Frame()
        
        self.heading = Label(self.mainframe,
                             text= "Choose your future",
                             font= heading)
        self.heading.grid(row=0, columnspan= 2)

        instructions = "Enter the amount of questions and answer\nthem to see if you've got what it takes"

        self.information = Label(self.mainframe,
                                 text= instructions,
                                 font= ("Candara", "20", "bold"))
        self.information.grid(row= 1, columnspan= 2)

        stats = ("30 Questions: The gauntlet \n"
                "20-15 Questions: The trial \n"
                "14-10 Questions: The test \n"
                "9-5 Questions: Yowaimo")

        self.status = Label(self.mainframe,
                            text= stats,
                            font= main_font,
                            justify= "left").grid(rowspan= 2, row= 2, column= 0)

        self.number_of_questions = IntVar()
    
        self.entry = Entry(self.mainframe,
                           textvariable= self.number_of_questions,
                           font= main_font,
                           width= 12,
                           justify= "center").grid(row= 2, column= 1)

        self.start_button = Button(self.mainframe,
                            text= "BEGIN",
                            font= main_font,
                            command= self.check_number)
        self.start_button.grid(row= 3, column= 1)

    def check_number(self):
        self.value = self.number_of_questions.get()

        if self.value > 30 or self.value < 5:
            error = Label(self.mainframe,
                          text= "ERROR: Use a number between 5 and 30",
                          font= main_font,
                          fg= "red").grid(row= 4, columnspan= 2)
            
        else:
            question_amount.append(self.value)
            self.begin()
            
    def open_page(self):
        self.mainframe.grid(padx= 10, pady= 10)
    
    def begin(self):
        self.mainframe.grid_forget()
        MainSystem()


class MainSystem:
    def __init__(self):
        self.QOLframe = Frame(padx= 10, pady= 10)
        self.QOLframe.grid()
    # Heading
        self.heading = Label(self.QOLframe,
                             text= "Quiz Of Legends",
                             font= heading)
        self.heading.grid(row= 0, columnspan= 2)

        questions = []
        choices = []
        self.answer = []
        for key, value in data.items():
            self.answered = False
            questions.append(value["question"])
            self.answer.append(value["answer"])
            choices.append(value["choice"])


        if (question_amount[0] - 1) >= len(points):

            self.question = Label(self.QOLframe,
                              text= questions[len(points)],
                              font= main_font)
            self.question.grid(row= 1, columnspan= 2)

            for x in choices:

                self.answers1 = Button(self.QOLframe,
                                    text= choices[len(points)][0],
                                    font= main_font,
                                    command= lambda 
                                    m= choices[len(points)][0] : 
                                    self.check_correct(m)).grid(row= 2, column= 0)

                self.answers2 = Button(self.QOLframe,
                                    text= choices[len(points)][1],
                                    font= main_font,
                                    command= lambda 
                                    m= choices[len(points)][1] : 
                                    self.check_correct(m)).grid(row= 2, column= 1)

                self.answers3 = Button(self.QOLframe,
                                    text= choices[len(points)][2],
                                    font= main_font,
                                    command= lambda 
                                    m= choices[len(points)][2] : 
                                    self.check_correct(m)).grid(row= 3, column= 0)
                
                self.answers4 = Button(self.QOLframe,
                                    text= choices[len(points)][3],
                                    font= main_font,
                                    command= lambda 
                                    m= choices[len(points)][3] : 
                                    self.check_correct(m)).grid(row= 3, column= 1)

        else:
            self.QOLframe.grid_forget()
            FinishScreen()
      
    def check_correct(self, m):
        """Checks if the button in which the user has pushed is correct"""
        

        if self.answer[len(points)] == m:
            points.append(1)

        else:
            points.append(0)
            
        self.QOLframe.grid_forget()
        self.correct = Correct()
        self.correct.open_page()
        self.next_question
    
    def next_question(self):
        self.QOLframe = Frame()
        
class Correct:
    def __init__(self):

        self.correct_frame = Frame(padx= 10, pady= 10)

        if points[-1] == 1:
            self.answer = "Correct"
            self.answer_check()
        else:
            self.answer = "Incorrect"
            self.answer_check()

        self.new_question = Button(self.correct_frame,
                              text= "next question",
                              font= main_font,
                              command= self.return_to_question)
        self.new_question.grid(row= 1, columnspan= 2)

    def answer_check(self):
        self.w = Label(self.correct_frame,
                       text= self.answer,
                       font= heading).grid(row= 0, columnspan= 2)
        
    def open_page(self):
        self.correct_frame.grid(padx= 10, pady= 10)

    def return_to_question(self):
        self.correct_frame.grid_forget()
        MainSystem().next_question

class FinishScreen():
    def __init__(self):

        self.final_frame = Frame(padx= 10, pady= 10)
        self.final_frame.grid(padx= 10, pady= 10)

        self.title = Label(self.final_frame,
            text= "GAME OVER",
            font= heading)
        self.title.grid(row= 0, column= 0, columnspan= 2)

        self.w = Label(self.final_frame,
                       text= "Points:",
                       font= main_font)
        self.w.grid(row= 1, column= 0)

        self.points = Label(self.final_frame,
                            text= f"{sum(points)} / {sum(question_amount)}",
                            font = main_font)
        self.points.grid(row= 1, column= 1)

        if sum(points) == 30:
            self.legend_status

        elif sum(points) == question_amount[0]:
            self.end_message = ("Although passing through this challenge\n"
                           "You must succeed in the gauntlet to truly be a legend")
            self.message()

        else:
            self.end_message = ("Alas you have failed my challenge\n" 
                          "while falling short of becoming a true LEGEND")
            self.message()

            
        self.retry = Button(self.final_frame,
                            text= "Retry?",
                            font= main_font,
                            command= self.run_again).grid(row= 3, column= 0)
        
        self.close = Button(self.final_frame,
                            text= "Take easy way out",
                            font= main_font,
                            command= root.destroy).grid(row= 3, column= 1)
        
    def message(self):
        self.w = Label(self.final_frame,
                text= self.end_message,
                font= main_font).grid(row= 2, column= 0, columnspan= 2)
        return
        
    def run_again(self):
        self.final_frame.grid_forget()
        Introduction()


    def legend_status(self):
        self.w



if __name__ == "__main__":
    root = Tk()
    root.title("Quiz of Legends")
    Introduction()
    root.mainloop()