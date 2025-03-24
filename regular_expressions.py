import re
email = input("what's your email?").strip()

if re.search(r"^\w+@\w+\.edu$", email, re.IGNORECASE):
    print("valid")
    
else:
    print("invalid")





""" username, domain = email.split("@")

if username and email.endswith(".edu"):
    print("valid")
else:
    print("invalid")
"""

""" if "@" in email and "." in email:
    print("valid")

else:
    print("invalid")
    
"""
