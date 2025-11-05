# Structured Interview Bot chaining example

print("Hello! Welcome to SkillCraft Technologies. May I know your name and the position you're seeking?")
name, role = input().split(',')  # Simulate candidate answer
print(f"Hi {name}, can you share your most relevant experience for the {role} position?")
exp = input()
print("What is one technical skill and one interpersonal skill that you believe set you apart for this job?")
skills = input()
print(f"Imagine a situation where you have to meet a tight deadline but lack some resources. How would you manage?")
scenario = input()
print(f"Thank you for your responses, {name}. Our team will review your interview and get back to you soon!")
