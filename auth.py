#Authentication Module
def login (username, password):
   # Simple authenticaton logic
   if username == "admin" and password == "password":
      return True
   return False

def logout():
     return "User logged out"

