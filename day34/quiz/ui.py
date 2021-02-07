import tkinter as tk
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):

        self.quiz = quiz_brain
        self.window = tk.Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = tk.Label(
            text=f"Sore: {self.quiz.score}", fg="white", bg=THEME_COLOR
        )
        self.canvas = tk.Canvas(
            width=300, heigh=250, bg="white", highlightthickness=0
        )
        self.q_text = self.canvas.create_text(
            150,
            125,
            width="280",
            text="Question Placeholder",
            fill=THEME_COLOR,
            font=("Arial", 16, "italic"),
        )
        true_img = tk.PhotoImage(file="images/true.png")
        false_img = tk.PhotoImage(file="images/false.png")
        self.true_button = tk.Button(
            image=true_img,
            highlightthickness=0,
            border=0,
            bg=THEME_COLOR,
            command=self._true_press,
        )
        self.false_button = tk.Button(
            image=false_img,
            highlightthickness=0,
            bg=THEME_COLOR,
            border=0,
            command=self._false_press,
        )

        self.score_label.grid(row=0, column=1)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        self.false_button.grid(row=2, column=0)
        self.true_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        self.score_label.config(text=f"Sore: {self.quiz.score}")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.q_text, text=q_text)
        else:
            self.canvas.itemconfig(
                self.q_text, text="You've reached the end of the quiz"
            )
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def _true_press(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def _false_press(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
