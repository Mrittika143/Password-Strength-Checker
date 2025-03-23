import re
def password_strength_check(password):
    strength = 0
    feedback=[]
    
    if len(password)>=8:
        strength+=1
    else:
        feedback.append("Password should be atleast 8 characters")
    
    if re.search(r'[A-Z]',password):
        strength+=1
    else:
        feedback.append("There should be atleast one uppercase letter")
    
    if re.search(r'[a-z]',password):
        strength+=1
    else:
        feedback.append("There should be atleast one lowercase letter")
    
    if re.search(r'[0-9]',password):
        strength+=1
    else:
        feedback.append("There should be atleast one number")
        
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        strength+=1
    else:
        feedback.append("There should be atleast one special character (!@#$%^&* etc.)")
    
    strength_levels = {
        5: "Strong 💪",
        4: "Moderate 👍",
        3: "Weak ⚠️",
        2: "Very Weak ❌",
        1: "Extremely Weak ❌",
        0: "Not Acceptable ❌"
    }
    
    print(f"Password strength:{strength_levels[strength]}")
    if feedback:
        print("Suggestions to improve the password:")
        for suggestion in feedback:
            print(f"-{suggestion}")
            
#usage
password=input("Enter a password:")
password_strength_check(password)