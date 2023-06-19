import random
import tkinter as tk
from tkinter import messagebox

questions = [
    (
        "What is the capital of France?",
        "Paris",
    ),
    (
        "Who painted the Mona Lisa?",
        "Leonardo da Vinci",
    ),
    (
        "Which planet is known as the Red Planet?",
        "Mars",
    ),
    (
        "Who wrote the novel 'Pride and Prejudice'?",
        "Jane Austen",
    ),
    (
        "What is the largest organ in the human body?",
        "Skin",
    ),
    (
        "Which country is famous for the Great Wall?",
        "China",
    ),
    (
        "Who is the current President of the United States?",
        "Joe Biden",
    ),
    (
        "What is the chemical symbol for gold?",
        "Au",
    ),
    (
        "Which is the largest ocean on Earth?",
        "Pacific Ocean",
    ),
    (
        "Who invented the telephone?",
        "Alexander Graham Bell",
    ),
    (
        "What is the tallest mountain in the world?",
        "Mount Everest",
    ),
    (
        "What is the national flower of Japan?",
        "Cherry blossom",
    ),
    (
        "Who painted the Sistine Chapel ceiling?",
        "Michelangelo",
    ),
    (
        "Which city hosted the 2016 Summer Olympics?",
        "Rio de Janeiro",
    ),
    (
        "What is the chemical symbol for sodium?",
        "Na",
    ),
    (
        "Who wrote the play 'Hamlet'?",
        "William Shakespeare",
    ),
    (
        "What is the largest continent by land area?",
        "Asia",
    ),
    (
        "Who is the author of 'To Kill a Mockingbird'?",
        "Harper Lee",
    ),
    (
        "Which animal is known as the 'King of the Jungle'?",
        "Lion",
    ),
    (
        "What is the longest river in the world?",
        "Nile",
    ),
    (
        "Who is the founder of Microsoft?",
        "Bill Gates",
    ),
    (
        "Which country is famous for the Taj Mahal?",
        "India",
    ),
    (
        "Who painted the 'Starry Night'?",
        "Vincent van Gogh",
    ),
    (
        "What is the largest species of shark?",
        "Whale shark",
    ),
    (
        "Which city is known as the 'Eternal City'?",
        "Rome",
    ),
    (
        "Who wrote the novel '1984'?",
        "George Orwell",
    ),
    (
        "What is the chemical symbol for oxygen?",
        "O",
    ),
    (
        "Which is the highest-grossing film of all time?",
        "Avengers: Endgame",
    ),
    (
        "What is the currency of Japan?",
        "Japanese yen",
    ),
    (
        "Who was the first person to walk on the moon?",
        "Neil Armstrong",
    ),
    (
        "What is the largest desert in the world?",
        "Sahara Desert",
    ),
    (
        "Who is the author of 'The Catcher in the Rye'?",
        "J.D. Salinger",
    ),
    (
        "Which country is famous for the pyramids?",
        "Egypt",
    ),
    (
        "Who painted the 'Girl with a Pearl Earring'?",
        "Johannes Vermeer",
    ),
    (
        "What is the symbol for the chemical element iron?",
        "Fe",
    ),
    (
        "Which is the second-largest country by land area?",
        "Canada",
    ),
    (
        "Who is the author of 'The Great Gatsby'?",
        "F. Scott Fitzgerald",
    ),
    (
        "What is the tallest tree species on Earth?",
        "Coast Redwood",
    ),
    (
        "Which city is known as the 'City of Love'?",
        "Paris",
    ),
    (
        "Who wrote the play 'Romeo and Juliet'?",
        "William Shakespeare",
    ),
    (
        "What is the largest species of penguin?",
        "Emperor penguin",
    ),
    (
        "What is the official language of Brazil?",
        "Portuguese",
    ),
    (
        "Who is the artist of the painting 'The Persistence of Memory'?",
        "Salvador Dalí",
    ),
    (
        "What is the highest mountain range in the world?",
        "Himalayas",
    ),
    (
        "Who is the author of 'The Lord of the Rings'?",
        "J.R.R. Tolkien",
    ),
    (
        "What is the capital of Italy?",
        "Rome",
    ),
    (
        "Who painted the 'The Last Supper'?",
        "Leonardo da Vinci",
    ),
    (
        "Which country is famous for the Colosseum?",
        "Italy",
    ),
    (
        "Who composed the symphony 'Symphony No. 9'?",
        "Ludwig van Beethoven",
    ),
    (
        "What is the chemical symbol for silver?",
        "Ag",
    ),
    (
        "Which is the smallest continent by land area?",
        "Australia",
    ),
]


class QuizApplication(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Quiz Application")
        self.geometry("500x400")
        self.configure(bg="#000000")

        self.score = 0
        self.current_question_index = 0

        self.question_label = tk.Label(self, wraplength=450, font=("Arial", 12), fg="#FFFFFF", bg="#000000")
        self.question_label.pack(pady=10)

        self.answer_entry = tk.Entry(self, font=("Arial", 12))
        self.answer_entry.pack(pady=10)

        self.submit_button = tk.Button(self, text="Submit", command=self.submit_answer, font=("Arial", 12), bg="#51D09E", fg="#000000")
        self.submit_button.pack(pady=5)

        self.hint_button = tk.Button(self, text="Hint", command=self.show_hint, font=("Arial", 12), bg="#51D09E", fg="#000000")
        self.hint_button.pack(pady=5)

        self.answer_button = tk.Button(self, text="View Answer", command=self.view_answer, font=("Arial", 12), bg="#51D09E", fg="#000000")
        self.answer_button.pack(pady=5)

        self.feedback_label = tk.Label(self, fg="red", font=("Arial", 12), bg="#000000")
        self.feedback_label.pack(pady=5)

        self.next_button = tk.Button(self, text="Next", command=self.show_next_question, font=("Arial", 12), bg="#51D09E", fg="#000000")
        self.next_button.pack(pady=5)

        self.previous_button = tk.Button(self, text="Previous", command=self.show_previous_question, font=("Arial", 12), bg="#51D09E", fg="#000000")
        self.previous_button.pack(pady=5)

        self.show_question()

    def show_question(self):
        question, _ = questions[self.current_question_index]

        self.question_label.config(text=question)
        self.answer_entry.delete(0, tk.END)
        self.feedback_label.config(text="")

    def submit_answer(self):
        user_answer = self.answer_entry.get().strip().lower()
        _, answer = questions[self.current_question_index]

        if user_answer == answer.lower():
            self.score += 1
            self.feedback_label.config(text="Correct!", fg="green")
        else:
            self.feedback_label.config(text="Incorrect. Try again!", fg="red")

    def show_hint(self):
        hint = "Here is a hint."
        messagebox.showinfo("Hint", hint)

    def view_answer(self):
        _, answer = questions[self.current_question_index]
        messagebox.showinfo("Answer", answer)

    def show_next_question(self):
        self.current_question_index = (self.current_question_index + 1) % len(questions)
        self.show_question()

    def show_previous_question(self):
        self.current_question_index = (self.current_question_index - 1) % len(questions)
        self.show_question()

    def show_result(self):
        messagebox.showinfo("Quiz Result", f"Your score is {self.score}.")
        self.destroy()

if __name__ == "__main__":
    app = QuizApplication()
    app.mainloop()
