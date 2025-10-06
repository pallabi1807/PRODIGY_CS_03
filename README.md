# PRODIGY_CS_03
Password Complexity Checker

🎯 Aim

Build a tool that assesses the strength of a password based on criteria such as length, presence of uppercase and lowercase letters, numbers, and special characters. Provide feedback to users on the password's strength.


---

🧠 Objective

The objective of this project is to help users understand and improve the security of their passwords by checking for length, uppercase, lowercase, digits, special characters, and avoidance of common patterns.


---

🏢 Internship Task

The assigned internship task was to develop a password strength checking tool.
I enhanced the task by creating a professional GUI version using Tkinter, making it more interactive and user-friendly. This demonstrates both technical skill and user experience design.


---

⚙️ Working

The user enters a password in the input box.

The program evaluates the password in real-time based on multiple criteria: length, uppercase, lowercase, digit, special character, and common patterns.

A strength label updates dynamically as Weak , Moderate, or Strong.

Suggestions for improvement are displayed one sentence per line in a read-only feedback box.

Users can toggle Show/Hide Password for convenience.

Password input is masked with * by default for privacy.



---

💻 Steps to Run

1. Install Python 3 on your system.

2. Open the code file password_strength_checker.py in VS Code or any Python IDE.

3. Run the program using:

password_strength_tool.py

4. Type your password in the entry box and view strength and feedback.

5. Use the Show/Hide Password button to toggle visibility.




---

🧩 Example Output

Weak Password:

Password: 12345
Strength: Weak 
Feedback:
- Use at least 8 characters (12+ is better).
- Add at least one uppercase letter.
- Add at least one lowercase letter.
- Add at least one special character.
- Avoid common or easily guessed words.

Strong Password:

Password: My$ecureP@ss123
Strength: Strong 
Feedback:
 Great! Your password looks secure.
