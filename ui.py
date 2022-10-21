from quiz_brain import QuizBrain
THEME_COLOR = "#375362"
from tkinter import *

class QuicBrainUi:
    def __init__(self,quiz:QuizBrain):
        self.quiz=quiz
        self.window=Tk()
        self.window.title("Quizler")
        self.label_score=Label(text="Score:0",fg="white",bg=THEME_COLOR)
        self.label_score.grid(row=0,column=2)
        self.window.config(padx=20,pady=20,bg=THEME_COLOR)
        self.canvas=Canvas(width=300,height=250,highlightthickness=0)
        self.questin_text=self.canvas.create_text(150,125,width=280,text="some question ",fill="blue",font=("Arial",20,"italic"))
        self.canvas.grid(row=1,column=0,columnspan=2,pady=50)
        true_image=PhotoImage(file="images/true.png")
        self.true_button=Button(image=true_image,highlightthickness=0,command=self.right_answer)
        self.true_button.grid(row=2,column=0)
        false_image=PhotoImage(file="images/false.png")
        self.false_button=Button(image=false_image,highlightthickness=0,command=self.wrong_answer)
        self.false_button.grid(row=2,column=1)
        self.next_questin()
        # self.canvas.create_image(100,112,image=self.tamoto_img)
        self.window.mainloop()
    def next_questin(self):
        if self.quiz.still_has_questions():
            self.label_score.config(text= f"Score:{self.quiz.score}")
            self.canvas.config(bg="white")
            q_text=self.quiz.next_question()
            self.canvas.itemconfig(self.questin_text,text=q_text)
        else:
            self.canvas.itemconfig(self.questin_text,text="You have end all question")
            self.true_button.config(state="disable")
            self.false_button.config(state="disable")

    def right_answer(self):
        is_right=self.quiz.check_answer("True")
        self.give_feedback(is_right)
    def wrong_answer(self):
        is_right=self.quiz.check_answer("False")
        self.give_feedback(is_right)
    def give_feedback(self,is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000,self.next_questin)


