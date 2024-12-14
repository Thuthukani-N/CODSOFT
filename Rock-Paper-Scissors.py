import tkinter as tk
import random

options = ["rock", "paper", "scissors"]

def play(player_choice):
    computer_choice = random.choice(options)

    if player_choice == computer_choice:
        result = "It's a tie!"
    elif (player_choice == "rock" and computer_choice == "scissors") or \
         (player_choice == "paper" and computer_choice == "rock") or \
         (player_choice == "scissors" and computer_choice == "paper"):
        result = "You win!"
    else:
        result = "You lose!"

    result_label.config(text=f"You chose {player_choice}.\nComputer chose {computer_choice}.\n{result}")

def exit_game():
    root.destroy()

root = tk.Tk()
root.title("Rock-Paper-Scissors Game")

title_label = tk.Label(root, text="Rock-Paper-Scissors", font=("Arial", 20, "bold"))
title_label.pack(pady=10)

button_frame = tk.Frame(root)
button_frame.pack(pady=10)

rock_button = tk.Button(button_frame, text="Rock", font=("Arial", 14), command=lambda: play("rock"))
rock_button.grid(row=0, column=0, padx=10)

paper_button = tk.Button(button_frame, text="Paper", font=("Arial", 14), command=lambda: play("paper"))
paper_button.grid(row=0, column=1, padx=10)

scissors_button = tk.Button(button_frame, text="Scissors", font=("Arial", 14), command=lambda: play("scissors"))
scissors_button.grid(row=0, column=2, padx=10)

result_label = tk.Label(root, text="", font=("Arial", 14), wraplength=400, justify="center")
result_label.pack(pady=20)

exit_button = tk.Button(root, text="Exit", font=("Arial", 14), command=exit_game)
exit_button.pack(pady=10)

root.mainloop()
