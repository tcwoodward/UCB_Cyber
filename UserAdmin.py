# Administrator accounts list
adminList = [
    {
        "username": "DaBigBoss",
        "password": "DaBest"
    },
    {
        "username": "root",
        "password": "toor"
    }
]
# Build your login functions below
# Function to prompt for login credentials
def getCreds():
    username = input("Username: ")
    password = input("Password: ")
    userInfo = {"username": username, "password": password}
    return userInfo

# Function to check login credentials
def checkLogin(userInfo, adminList):
    if (userInfo["username"] == adminList[0]["username"] and userInfo["password"] == adminList[0]["password"] or userInfo["username"] == adminList[1]["username"] and userInfo["password"] == adminList[1]["password"]):
        loggedIn = True
        print("YOU HAVE LOGGED IN!")
        return loggedIn
    else:
        loggedIn = False
        return loggedIn

user_info = getCreds()
loggedIn = checkLogin(user_info, adminList)
print("------------------")

while (loggedIn == False):
    user_info = getCreds()
    loggedIn = checkLogin(user_info, adminList)
    print("------------------")
