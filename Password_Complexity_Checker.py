import re
def check_password_strength(password):
    feedback = []
    if len(password) < 8:
        feedback.append("Password should be at least 8 characters long.")
    if not any(char.isupper() for char in password):
        feedback.append("Password should include at least one uppercase letter.")
    if not any(char.islower() for char in password):
        feedback.append("Password should include at least one lowercase letter.")
    if not any(char.isdigit() for char in password):
        feedback.append("Password should include at least one digit.")
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        feedback.append("Password should include at least one special character.")

    if not feedback:
        return "Strong password!", feedback
    elif len(feedback) <= 2:
        return "Moderate password.", feedback
    else:
        return "Weak password.", feedback

password = input("Enter a password to check its strength: ")
strength, feedback = check_password_strength(password)
print(f"Password strength: {strength}")
for comment in feedback:
    print(f"- {comment}")
