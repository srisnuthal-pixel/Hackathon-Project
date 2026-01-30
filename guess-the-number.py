import tkinter as tk
import random
from tkinter import messagebox

class NumberGuessingGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Number Guessing Game")
        self.root.geometry("300x200")
        self.secret_number = 0
        self.attempts = 0
        self.max_attempts = 5
        self.setup_gui()
        self.start_new_game()

    def setup_gui(self):
        # Instructions Label
        self.instructions = tk.Label(self.root, text=f"Guess a number between 1 and 100.\nYou have {self.max_attempts} attempts.")
        self.instructions.pack(pady=10)

        # Entry field for user guess
        self.guess_entry = tk.Entry(self.root)
        self.guess_entry.pack(pady=5)

        # Guess Button
        self.guess_button = tk.Button(self.root, text="Guess", command=self.check_guess)
        self.guess_button.pack(pady=5)

        # Feedback Label
        self.feedback_label = tk.Label(self.root, text="", fg="black")
        self.feedback_label.pack(pady=10)

        # Play Again Button (hidden initially)
        self.play_again_button = tk.Button(self.root, text="Play Again", command=self.start_new_game)
        
    def start_new_game(self):
        self.secret_number = random.randint(1, 100)
        self.attempts = 0
        self.feedback_label.config(text="")
        self.guess_entry.delete(0, tk.END)
        self.guess_button.config(state=tk.NORMAL)
        self.play_again_button.pack_forget() # Hide the play again button

    def check_guess(self):
        try:
            guess = int(self.guess_entry.get())
            if not (1 <= guess <= 100):
                self.feedback_label.config(text="Please enter a number between 1 and 100.", fg="orange")
                return

            self.attempts += 1

            if guess == self.secret_number:
                self.feedback_label.config(text=f"Correct! You guessed it in {self.attempts} attempts.", fg="green")
                self.end_game()
            elif guess < self.secret_number:
                self.feedback_label.config(text="Too low! Try a higher number.", fg="red")
            else:
                self.feedback_label.config(text="Too high! Try a lower number.", fg="red")

            if self.attempts >= self.max_attempts and guess != self.secret_number:
                self.feedback_label.config(text=f"Sorry, you ran out of attempts! The number was {self.secret_number}.", fg="red")
                self.end_game()

        except ValueError:
            self.feedback_label.config(text="Invalid input. Please enter a valid number.", fg="orange")
        finally:
            self.guess_entry.delete(0, tk.END) # Clear the entry box after each guess

    def end_game(self):
        self.guess_button.config(state=tk.DISABLED) # Disable the guess button
        self.play_again_button.pack(pady=10) # Show the play again button

if __name__ == "__main__":
    root = tk.Tk()
    game = NumberGuessingGame(root)
    root.mainloop()
