import re
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# Function to evaluate password strength
def check_password_strength(password):
    score = 0
    feedback = []
    
    # Length
    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
    else:
        feedback.append("Use at least 8 characters (12+ is better).")
    
    # Uppercase
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Add at least one uppercase letter.")
    
    # Lowercase
    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Add at least one lowercase letter.")
    
    # Digit
    if re.search(r"[0-9]", password):
        score += 1
    else:
        feedback.append("Add at least one number.")
    
    # Special character
    if re.search(r"[!@#$%^&*(),.?\{}|<>]", password):
        score += 1
    else:
        feedback.append("Add at least one special character.")
    
    # Avoid common patterns
    common_patterns = ["password", "admin", "12345", "qwerty", "abc"]
    if any(word in password.lower() for word in common_patterns):
        feedback.append("Avoid common or easily guessed words.")
        score -= 1
    
    # Determine strength
    if score >= 6:
        strength = "Strong "
        color = "green"
    elif 3 <= score < 6:
        strength = "Moderate "
        color = "orange"
    else:
        strength = "Weak "
        color = "red"
    
    return strength, score, color, feedback

# Function triggered on typing
def update_strength(event=None):
    password = password_entry.get()
    strength, score, color, feedback = check_password_strength(password)
    strength_label.config(text=f"Strength: {strength} | Score: {max(0, score)}/6", fg=color)
    feedback_text.config(state="normal")
    feedback_text.delete(1.0, tk.END)
    if feedback:
        for tip in feedback:
            feedback_text.insert(tk.END, f"{tip}\n " , "bold")
    else:
        feedback_text.insert(tk.END, " Great! Your password looks secure.", "bold")
    feedback_text.config(state="disabled")

# Show/Hide toggle function
def toggle_show_password():
    if password_entry.cget('show') == '':
        password_entry.config(show='*')
        show_button.config(text="Show")
    else:
        password_entry.config(show='')
        show_button.config(text="Hide")

# Tkinter Window Setup
root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("500x400")
root.resizable(False, False)

# Title
title_label = tk.Label(root, text=" Secure Password Strength Checker", font=("Arial", 14, "bold"))
title_label.pack(pady=10)

# Password Entry with show/hide toggle button
frame = tk.Frame(root)
frame.pack(pady=10, padx=20, fill='x')

password_entry = tk.Entry(frame, show="*", font=("Arial", 12))
password_entry.pack(side="left", fill='x', expand=True)
password_entry.bind("<KeyRelease>", update_strength)

show_button = tk.Button(frame, text="Show", command=toggle_show_password)
show_button.pack(side="left", padx=5)

# Strength Label
strength_label = tk.Label(root, text="Strength: ", font=("Arial", 12))
strength_label.pack(pady=10)

# Feedback Box (Read Only)
feedback_text = tk.Text(root, height=8, font=("Arial", 11), state="disabled")
feedback_text.tag_configure("bold", font=("Arial", 11, "bold") )
feedback_text.pack(pady=10, padx=20, fill='both')

root.mainloop()
