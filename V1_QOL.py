from tkinter import *

class QuizOfLegends:
    def __init__(self):

        self.QOLframe = Frame(padx= 10, pady= 10)
        self.QOLframe.grid()

    # Heading
        self.heading = Label(self.QOLframe,
                             text= "Quiz Of Legends",
                             font= ("Arial", "36", "bold")
                             )
        
        self.heading.grid(row= 0, columnspan= 2)

    # Instructions
        instructions = ("For millenia people have tried their knowledge and failed this very quiz.\n"
                        "Many individuals falter under the sheer right to be called a legend.\n"
                        "Do you have what it takes to be granted this title?\n"
                        "Or will you falter like the latter?")
        
        self.instructions = Label(self.QOLframe,
                                  text= instructions,
                                  font= ("Arial", "20"),
                                  justify= "center")
        self.instructions.grid(row= 2, columnspan= 2)

    # Start Button
        self.start_button = Button(self.QOLframe,
                                   text= "Start",
                                   font= ("Arial", "20"),
                                   width= 12,
                                   command= self.main_menu
                                   )
        self.start_button.grid(pady= 10, row= 3, columnspan= 2)

    def main_menu(self):
        pass



if __name__ == "__main__":
    root = Tk() 
    root.title("Quiz Of Legends")
    QuizOfLegends()
    root.mainloop()