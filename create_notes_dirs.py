import os

def main():
    os.mkdir("CyberSecurity-Notes")
    for num in range(1,25):
        os.makedirs("CyberSecurity-Notes/Week " + str(num))
        for days in range(1,4):
            os.makedirs("CyberSecurity-Notes/Week " + str(num) + "/Day " + str(days))
main()
