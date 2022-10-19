
'''
Let’s take a password as a combination of alphanumeric characters along with special characters, and check whether the password is valid or not with the help of few conditions.

Conditions for a valid password are:

Should have at least one number.
Should have at least one uppercase and one lowercase character.
Should have at least one special symbol.
Should be between 6 to 20 characters long
'''
special_symbols=['@','$','#','%']
password=input("please enter password:")
val=True
if len(password) <6:
    print("let should be atleast 6")
    val=False
    
if len(password) >20:
    print("must not be >20")
    val=False
    
if not any(char.isdigit() for char in password):
    print("Should have at least one number")
    val=False

if not any(char.isupper() for char in password):
    print("Should have at least one uppercase")
    val=False    ws
    
if not any(char.islower() for char in password):
    print("Should have at least one lowercase")
    val=False

if not any(char in special_symbols for char in password):
    print("please enter atleast one special symbol")
    val=False    
    
if val:
    val=val
print(val)    