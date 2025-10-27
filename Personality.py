import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

# ----------------- Question Set -----------------
questions = [
    "You prefer to spend your free time alone or with a small group of close friends.",
    "You find it easy to introduce yourself to new people.",
    "You get energized by social gatherings and parties.",
    "You enjoy deep, meaningful conversations over small talk.",
    "You like being the center of attention in social settings.",
    "You prefer working alone rather than in a team.",
    "You enjoy trying new activities and meeting new people.",
    "You often think before you speak.",
    "You find social interactions draining after a while.",
    "You feel comfortable sharing your thoughts openly."
]

# ----------------- Scoring Logic -----------------
# (Higher score = more extroverted)
weights = [0, 1, 1, 0, 1, 0, 1, 0, 0, 1]

# ----------------- App Class -----------------
class PersonalityApp:
    def __init__(self, root):
        self.root = root
        self.root.title("AI Personality Predictor")
        self.root.geometry("800x500")
        self.root.config(bg="#F8F9FA")
        self.root.resizable(False, False)

        self.style = ttk.Style()
        self.style.configure("TButton", font=("Segoe UI", 12, "bold"), padding=10)
        self.style.map("TButton", background=[("active", "#6C63FF")])

        self.question_index = 0
        self.answers = []
        self.setup_quiz_interface()

    def setup_quiz_interface(self):
        self.title_label = tk.Label(
            self.root, text="🧠 AI Personality Prediction Quiz 🧠", 
            font=("Helvetica", 22, "bold"), fg="white", bg="#1E1E2E"
        )
        self.title_label.pack(pady=20)

        self.frame = tk.Frame(self.root, bg="#282A36", bd=5, relief="ridge")
        self.frame.place(relx=0.5, rely=0.55, anchor="center", width=700, height=300)

        self.question_label = tk.Label(
            self.frame, text="", wraplength=650, justify="center",
            font=("Helvetica", 16), fg="#F8F8F2", bg="#282A36"
        )
        self.question_label.pack(pady=40)

        self.var = tk.IntVar()
        self.options = ["Strongly Disagree", "Disagree", "Neutral", "Agree", "Strongly Agree"]
        self.radio_buttons = []
        for i, opt in enumerate(self.options):
            rb = ttk.Radiobutton(self.frame, text=opt, variable=self.var, value=i+1)
            rb.pack(anchor="w", padx=100, pady=2)
            self.radio_buttons.append(rb)

        self.next_button = ttk.Button(self.root, text="Next ➡️", command=self.next_question)
        self.next_button.pack(pady=20)

        self.show_question()

    def show_question(self):
        self.question_label.config(text=f"Q{self.question_index+1}. {questions[self.question_index]}")
        self.var.set(0)

    def next_question(self):
        if self.var.get() == 0:
            messagebox.showwarning("⚠️ Warning", "Please select an answer before continuing!")
            return

        self.answers.append(self.var.get())

        if self.question_index < len(questions) - 1:
            self.question_index += 1
            self.show_question()
        else:
            self.show_result()

    def show_result(self):
        score = 0
        for i in range(len(questions)):
            score += self.answers[i] * weights[i]

        avg_score = score / sum(weights)

        if avg_score <= 2:
            personality = "Introvert"
            desc = "You enjoy solitude and deep reflection. You feel recharged after quiet time alone."
        elif avg_score >= 4:
            personality = "Extrovert"
            desc = "You thrive in social settings, enjoy meeting new people, and express yourself openly."
        else:
            personality = "Ambivert"
            desc = "You have a balanced mix of introversion and extroversion traits."

        # Clear all widgets
        for widget in self.root.winfo_children():
            widget.destroy()

        # Show results
        result_label = tk.Label(
            self.root, text="✨ Personality Prediction Result ✨",
            font=("Helvetica", 22, "bold"), fg="#00FFB3", bg="#1E1E2E"
        )
        result_label.pack(pady=30)

        type_label = tk.Label(
            self.root, text=personality,
            font=("Helvetica", 20, "bold"), fg="#FFD700", bg="#1E1E2E"
        )
        type_label.pack(pady=20)

        desc_label = tk.Label(
            self.root, text=desc,
            wraplength=700, justify="center",
            font=("Helvetica", 14), fg="#F8F8F2", bg="#1E1E2E"
        )
        desc_label.pack(pady=20)

        restart_button = ttk.Button(self.root, text="Take Quiz Again 🔄", command=self.restart)
        restart_button.pack(pady=20)

    def restart(self):
        self.question_index = 0
        self.answers = []
        for widget in self.root.winfo_children():
            widget.destroy()
        self.setup_quiz_interface()

# ----------------- Main Execution -----------------
if __name__ == "__main__":
    root = tk.Tk()
    app = PersonalityApp(root)
    root.mainloop()
