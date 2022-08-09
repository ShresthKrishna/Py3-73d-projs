from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"
FONT = ("Arial", 10, "italic")


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.score = 0
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        self.true = PhotoImage(file="./images/true.png")
        self.false = PhotoImage(file="./images/false.png")

        self.true_but = Button(image=self.true, bg=THEME_COLOR, highlightthickness=0, borderwidth=0, command=self.tr_ue)
        self.true_but.grid(row=2, column=0, ipady=10, ipadx=10)
        self.false_but = Button(image=self.false, bg=THEME_COLOR, highlightthickness=0, borderwidth=0, command=self.fal_se)
        self.false_but.grid(row=2, column=1, ipady=10, ipadx=10)

        self.canvas = Canvas(height=250, width=300, bg="white")
        self.question_text = self.canvas.create_text(150, 100, text="Some Question", width=280, font=FONT)
        self.canvas.grid(row=1,column=0, columnspan=2)

        self.score_bd = Label(text=f"Score: {self.score}", bg=THEME_COLOR, fg="white")
        self.score_bd.grid(row=0, column=1, ipady=10, ipadx=0, sticky= E)

        self.ques_next()

        self.window.mainloop()

    def ques_next(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():

            quiz_que = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=f"{quiz_que}")
        else:
            self.canvas.itemconfig(self.question_text,text=f"End Of Quiz"
                                                           f"\nScore is : {self.score}")
            self.true_but.config(state="disabled")
            self.false_but.config(state="disabled")
    def tr_ue(self):
        self.quiz.check_answer("True")
        if self.quiz.check_answer("True"):
            self.score += 1
            self.score_bd.config(text=f"Score: {self.score}")
        self.feedback(self.quiz.check_answer("True"))
    def fal_se(self):

        self.quiz.check_answer("False")
        if self.quiz.check_answer("False"):
            self.score+=1
            self.score_bd.config(text=f"Score: {self.score}")
        self.canvas.config(bg="white")
        self.feedback(self.quiz.check_answer("False"))

    def feedback(self, answer):
        if answer == True:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000,self.ques_next)
            #

