"""
Note: that this version is an extras edition that has more add-ons from V4.
There are many more things that I would like to implement
however if this design is not finished then V4 will be the final.
DLC
"""
from tkinter import *
import json
with open("challenges.json") as q:
    trial = json.load(q)

heading_colour = "#B8D8D8"
colour2 = "#7a8E9F"
colour3 = "#4f6367"
text_colour = "#eef5db"
colour5 = "#fe5f55"

main_font = ("Candara", "17")
heading = ("Goudy Stout", "25", "bold")

points = []
question_amount = []
trials = []

class Introduction:
    def __init__(self):
        self.intro_frame = Frame(bg= colour2, borderwidth= 6, relief= "ridge")

        self.intro_frame.grid(padx= 10, pady= 10)

        self.heading = Label(self.intro_frame,
                             text= "Quiz of Legends",
                             width= 14,
                             bg= colour2,
                             fg= heading_colour,
                             borderwidth= 5,
                             relief= "sunken",
                             font= ("Goudy Stout", "30", "bold")).grid(row= 0, columnspan = 2)
        
        instructions = ("For millenia people have tried their knowledge and failed this quiz.\n"
                        "Many individuals falter under the sheer right to be called a legend.\n"
                        "Do you think you have what it takes to be granted this title?\n"
                        "Or will you falter like the latter?")

        self.message = Label(self.intro_frame,
                             text= instructions,
                             font= main_font,
                             fg= text_colour,
                             bg= colour3,
                             width= 60).grid(row= 1, columnspan= 2)

        self.start_button = Button(self.intro_frame,
                            text= "Run the gauntlet",
                            font= main_font,
                            width= 15,
                            bg= colour5,
                            borderwidth= 5,
                            relief= "ridge",
                            command= self.start).grid(row= 2, column= 0)

        self.falter = Button(self.intro_frame,
                             text= "Falter like the rest",
                             font= main_font,
                             width= 15,
                             bg= colour5,
                             borderwidth= 5,
                             relief= "ridge",
                             command= root.destroy).grid(row= 2, column= 1)
        self.category = Category()

    def start(self):
        """Closes this frame and then uses a function from another class to open a different frame"""
        self.intro_frame.grid_forget()
        self.category.open_page()

class Category:
    def __init__(self):
        self.category_frame = Frame(bg= colour2, borderwidth= 6, relief= "ridge")

        self.heading = Label(self.category_frame,
                            text= "Choose your trial",
                            font= ("Goudy Stout", "25", "bold"),
                            fg= heading_colour,
                            bg= colour2,
                            borderwidth= 5,
                    relief= "sunken").grid(row= 0, columnspan = 2)
        
        self.text = Label(self.category_frame,
                          text= "Choose the category you would like to be trialled on",
                          font= ("Candara", "20", "bold"),
                          fg = text_colour,
                          borderwidth= 5,
                          relief= "groove",
                          bg = colour3).grid(row=1, columnspan = 2)

        placement = 1
        
        for challenges, self.questions in trial.items():
            trials.append(challenges)

        for x in trials:
            self.label = Button(self.category_frame,
                    font= main_font,
                    text= f"Trial of {x}",
                    bg= colour5,
                    borderwidth= 5,
                    relief= "ridge",
                    command = lambda m= trial[x] : self.chosen_trial(m))
            self.label.grid(column= 0, row= placement + 1, columnspan= 2)
        
            placement += 1
        self.mainmenu = MainMenu()


    def open_page(self):
        """Opens the frame"""
        self.category_frame.grid(padx= 10, pady= 10)

    def chosen_trial(self, m):

        global trial_questions
        trial_questions = m

        self.category_frame.grid_forget()
        self.mainmenu.open_page()

    def open_page(self):
        """Opens the frame"""
        self.category_frame.grid(padx= 10, pady= 10)


class MainMenu:
    def __init__(self):
        self.mainframe = Frame(bg= colour2, borderwidth= 6, relief= "ridge")
        
        self.heading = Label(self.mainframe,
                             text= "Choose your future",
                             font= heading,
                             bg= colour2,
                             fg= heading_colour,
                             borderwidth= 5,
                             relief= "sunken")
        self.heading.grid(row=0, columnspan= 2)

        instructions = ("Enter the amount of questions and answer\n"
                        "them to see if you've got what it takes")

        self.information = Label(self.mainframe,
                                 text= instructions,
                                 fg= text_colour,
                                 bg= colour3,
                                 width= 48,
                                 borderwidth= 5,
                                 relief= "groove",
                                 font= ("Candara", "20", "bold"))
        self.information.grid(row= 1, columnspan= 2)

        stats = ("30 Questions: The gauntlet \n"
                "20-15 Questions: The trial \n"
                "14-10 Questions: The test \n"
                "9-5 Questions: Yowaimo")

        self.status = Label(self.mainframe,
                            text= stats,
                            font= (main_font),
                            bg= colour2,
                            fg= text_colour,
                            justify= "left")
        self.status.grid(rowspan= 2, row= 2, column= 0)

        self.entry = Entry(self.mainframe,
                           font= main_font,
                           bg= colour2,
                           fg= text_colour,
                           width= 12,
                           justify= "center")
        self.entry.grid(row= 2, column= 1)


        self.start_button = Button(self.mainframe,
                            text= "BEGIN",
                            bg= colour5,
                            font= main_font,
                            borderwidth= 5,
                            relief= "ridge",
                            command= self.check_number)
        self.start_button.grid(row= 3, column= 1)

        self.error_message = Label(self.mainframe,
                                   text= "",
                                   font= ("Candara", "20", "bold"),
                                   fg= "red",
                                   bg= colour2)
        self.error_message.grid(row= 4, columnspan= 2)


    def check_number(self):
        """Checks the number that the user has inputted is valid, if not then send ERROR message"""

        number_of_questions = self.entry.get()
        value, error_sentence = self.validate_number(number_of_questions)

        if not value:
            self.error_message.config(text= error_sentence)

        else:
            self.begin()

    def validate_number(self, value):
        """Validates a number and see whether it is appropriate to use"""
        if str(value) == "":
            return False, "ERROR: Input a number"
        
        elif not str(value).isdigit():
            return False, "ERROR: Please use a number"
        number = int(value)
        
        if number > 30 or number < 5:
            return False, "ERROR: Number must be from 5-30"
        
        else:
            question_amount.append(number)
            return True, ""

    def open_page(self):
        """Opens the frame"""
        self.mainframe.grid(padx= 10, pady= 10)
    
    def begin(self):
        """Starts the main program"""
        self.mainframe.grid_forget()
        MainSystem()

class MainSystem:
    def __init__(self):
        self.QOLframe = Frame(bg= colour2)
        self.QOLframe.grid(padx= 10, pady= 10)

        self.heading = Label(self.QOLframe,
                             text= "Quiz Of Legends",
                             font= heading,
                             bg= colour3,
                             fg= heading_colour,
                             borderwidth= 5,
                             relief= "sunken")
        self.heading.grid(row= 0, columnspan= 2)

        questions = []
        choices = []
        self.answer = []
        for key, value in trial_questions.items(): # Gathers the data from the json and adds to a list
            self.answered = False
            questions.append(value["question"])
            self.answer.append(value["answer"])
            choices.append(value["choice"])


        if (question_amount[0] - 1) >= len(points): # Checks if the points are smaller than the amount of questions
            self.question = Label(self.QOLframe,
                              text= questions[len(points)],
                              bg= colour2,
                              fg= text_colour,
                              font= main_font)
            self.question.grid(row= 1, columnspan= 2)

            for x in choices:
                self.answers1 = Button(self.QOLframe,
                                    text= choices[len(points)][0],
                                    bg = colour5,
                                    borderwidth= 5,
                                    relief= "ridge",
                                    font= main_font,
                                    command= lambda 
                                    m= choices[len(points)][0] : 
                                    self.check_correct(m)).grid(row= 2, column= 0)
                
                self.answers2 = Button(self.QOLframe,
                                    text= choices[len(points)][1],
                                    bg = colour5,
                                    borderwidth= 5,
                                    relief= "ridge",
                                    font= main_font,
                                    command= lambda 
                                    m= choices[len(points)][1] : 
                                    self.check_correct(m)).grid(row= 2, column= 1)

                self.answers3 = Button(self.QOLframe,
                                    text= choices[len(points)][2],
                                    bg = colour5,
                                    borderwidth= 5,
                                    relief= "ridge",
                                    font= main_font,
                                    command= lambda 
                                    m= choices[len(points)][2] : 
                                    self.check_correct(m)).grid(row= 3, column= 0)
                
                self.answers4 = Button(self.QOLframe,
                                    text= choices[len(points)][3],
                                    bg = colour5,
                                    borderwidth= 5,
                                    relief= "ridge",
                                    font= main_font,
                                    command= lambda 
                                    m= choices[len(points)][3] : 
                                    self.check_correct(m)).grid(row= 3, column= 1)

        else: # When the amount of points in a list exceed the question amount the finish screen opens
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

        self.correct_frame = Frame(bg= colour2)



        self.new_question = Button(self.correct_frame,
                    text= "next question",
                    font= main_font,
                    borderwidth= 5,
                    relief= "ridge",
                    command= self.return_to_question)
        self.new_question.grid(row= 1, columnspan= 2)

        if points[-1] == 1:
            self.answer = "Correct"
            self.new_question.config(bg = "green")
            self.answer_display()
        else:
            self.answer = "Incorrect"
            self.new_question.config(bg = "red")
            self.answer_display()

    def answer_display(self):
        self.w = Label(self.correct_frame,
                    text= self.answer,
                    bg= colour3,
                    fg= heading_colour,
                    borderwidth= 5,
                    relief= "sunken",
                    font= heading).grid(row= 0, columnspan= 2)
        
    def open_page(self):
        self.correct_frame.grid(padx= 10, pady= 10)

    def return_to_question(self):
        self.correct_frame.grid_forget()
        MainSystem().next_question

class FinishScreen():
    def __init__(self):
        self.final_frame = Frame(bg= colour2)
        self.final_frame.grid(padx= 10, pady= 10)

        self.title = Label(self.final_frame,
            text= "GAME OVER",
            font= heading,
            bg= colour2,
            fg= heading_colour,
            borderwidth= 5,
            relief= "sunken",)
        self.title.grid(row= 0, column= 0, columnspan= 2)

        self.w = Label(self.final_frame,
                       text= "Points:",
                       bg= colour2,
                        fg= text_colour,
                       font= main_font)
        self.w.grid(row= 1, column= 0)

        self.points = Label(self.final_frame,
                            text= f"{sum(points)} / {sum(question_amount)}",
                            bg= colour2,
                            fg= text_colour,
                            font = main_font)
        self.points.grid(row= 1, column= 1)

        if sum(points) == 30:
            self.end_message = ("Congratulations!\n"
                                "You truly are worthy to call yourself a legend")
            self.message()

        elif sum(points) == question_amount[0]:
            self.end_message = ("Although you've passed through this challenge\n"
                           "You must succeed in the gauntlet to truly be a legend")
            self.message()

        else:
            self.end_message = ("Alas you have failed my challenge\n" 
                          "while falling short of becoming a true LEGEND")
            self.message()

            
        self.retry = Button(self.final_frame,
                            text= "Retry?",
                            font= main_font,
                            bg = colour5,
                            borderwidth= 5,
                            relief= "ridge",
                            command= self.run_again).grid(row= 3, column= 0)
        
        self.close = Button(self.final_frame,
                            text= "Take easy way out",
                            font= main_font,
                            bg = colour5,
                            borderwidth= 5,
                            relief= "ridge",
                            command= root.destroy).grid(row= 3, column= 1)
        
    def message(self):
        self.w = Label(self.final_frame,
                text= self.end_message,
                bg= colour2,
                fg= text_colour,
                font= main_font).grid(row= 2, column= 0, columnspan= 2)
        return
        
    def run_again(self):
        self.final_frame.grid_forget()
        question_amount.clear()
        points.clear()
        trials.clear()
        Introduction()

if __name__ == "__main__":
    root = Tk()
    root.title("Quiz of Legends")
    root.configure(background= colour3,
                   borderwidth= 8,
                   relief= "ridge")
    Introduction()
    root.mainloop()