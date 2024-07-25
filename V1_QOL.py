from tkinter import *
from tkinter import *
import json
with open("questions.json") as f:
    data = json.load(f)

FONT = ("Candara", "20")
heading = ("Goudy Stout", "25", "bold")
points = []
question_amount = []

class Introduction:
    def __init__(self):

        # Creating frame
        self.intro_frame = Frame()
        self.intro_frame.grid(padx= 20, pady= 10)

        #Heading
        self.heading = Label(self.intro_frame,
                             text= "Quiz of Legends",
                             font= ("Goudy Stout", "30", "bold"))
        self.heading.grid(row= 0, columnspan = 2)

        instructions = ("For millenia people have tried their knowledge and failed this very quiz.\n"
                        "Many individuals falter under the sheer right to be called a legend.\n"
                        "Do you have what it takes to be granted this title?\n"
                        "Or will you falter like the latter?")

        # Label
        self.message = Label(self.intro_frame,
                             text= instructions,
                             font= FONT)
        self.message.grid(row= 1, columnspan= 2)

        # Buttons
        self.start_button = Button(self.intro_frame,
                            text= "Run the gauntlet",
                            font= FONT,
                            width= 15,
                            command= self.start)
        self.start_button.grid(row= 2, column= 0)

        self.falter = Button(self.intro_frame,
                             text= "Falter like the rest",
                             font= FONT,
                             width= 15,
                             command= root.destroy)
        self.falter.grid(row= 2, column= 1)
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

        stats = "30 Questions: The gauntlet \n20-15 Questions: The trial \n14-10 Questions: The test \n9-5 Questions: Yowaimo"

        self.status = Label(self.mainframe,
                            text= stats,
                            font= FONT,
                            justify= "left")
        self.status.grid(rowspan= 2, row= 2, column= 0)

        self.number_of_questions = IntVar()
        
        self.entry = Entry(self.mainframe,
                           textvariable= self.number_of_questions,
                           font= FONT,
                           width= 12,
                           justify= "center")
        self.entry.grid(row= 2, column= 1)

        self.start_button = Button(self.mainframe,
                            text= "BEGIN",
                            font= FONT,
                            command= self.check_number)
        self.start_button.grid(row= 3, column= 1)

    def check_number(self):

        self.value = self.number_of_questions.get()
        question_amount.append(self.value)

        if self.value < 5:
            error = Label(self.mainframe,
                          text= "ERROR: Question count too small",
                          font= FONT)
            error.grid(row= 4, columnspan= 2)

        elif self.value > 30:
            error = Label(self.mainframe,
                          text= "ERROR: Question count too large",
                          font= FONT)
            error.grid(row= 4, columnspan= 2)
        else:
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
                              font= FONT)
            self.question.grid(row= 1, columnspan= 2)

            for x in choices:

                self.answers1 = Button(self.QOLframe,
                                    text= choices[len(points)][0],
                                    font= FONT,
                                    command= lambda 
                                    m= choices[len(points)][0] : 
                                    self.check_correct(m))
                self.answers1.grid(row= 2, column= 0)

                self.answers2 = Button(self.QOLframe,
                                    text= choices[len(points)][1],
                                    font= FONT,
                                    command= lambda 
                                    m= choices[len(points)][1] : 
                                    self.check_correct(m))
                self.answers2.grid(row= 2, column= 1)

                self.answers3 = Button(self.QOLframe,
                                    text= choices[len(points)][2],
                                    font= FONT,
                                    command= lambda 
                                    m= choices[len(points)][2] : 
                                    self.check_correct(m))
                self.answers3.grid(row= 3, column= 0)
                
                self.answers4 = Button(self.QOLframe,
                                    text= choices[len(points)][3],
                                    font= FONT,
                                    command= lambda 
                                    m= choices[len(points)][3] : 
                                    self.check_correct(m))
                self.answers4.grid(row= 3, column= 1)

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
        self.correct.page_open()
        self.next_question
    
    def next_question(self):
        self.QOLframe = Frame()
        


class Correct:
    def __init__(self):

        self.correct_frame = Frame(padx= 10, pady= 10)

        if points[-1] == 1:
            self.answer_correct()
        else:
            self.answer_incorrect()

        self.new_question = Button(self.correct_frame,
                              text= "next question",
                              font= FONT,
                              command= self.return_to_question)
        self.new_question.grid(row= 1, columnspan= 2)

    def answer_correct(self):
        self.w = Label(self.correct_frame,
            text= "Correct",
            font= heading)
        self.w.grid(row= 0, columnspan= 2)

    def answer_incorrect(self):
        self.w = Label(self.correct_frame,
            text= "Incorrect",
            font= heading)
        self.w.grid(row= 0, columnspan= 2)
        
    def page_open(self):
        self.correct_frame.grid(padx= 10, pady= 10)

    def return_to_question(self):
        self.correct_frame.grid_forget()
        MainSystem().next_question



class FinishScreen():
    def __init__(self):

        self.final_frame = Frame(padx= 10, pady= 10)
        self.final_frame.grid(padx= 10, pady= 10)

        self.title = Label(self.final_frame,
            text= "Congratulations",
            font= heading)
        self.title.grid(row= 0, column= 0, columnspan= 2)

        self.w = Label(self.final_frame,
                       text= "Points:",
                       font= FONT)
        self.w.grid(row= 1, column= 0)

        self.points = Label(self.final_frame,
                            text= sum(points),
                            font = FONT)
        self.points.grid(row= 1, column= 1)


        

if __name__ == "__main__":
    root = Tk()
    root.title("Quiz of Legends")
    Introduction()
    root.mainloop()
