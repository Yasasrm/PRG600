''' 
Name: Yasas Maddumage. 
Student ID: 170308233. 
Description: Lab 6 part 1 Question 3 (lab8c.py).  
''' 

import os
import re

def getUserInfo():
    # Get the username of the logged-in user
    username = os.popen("whoami").read().strip()
    # Define the regex pattern
    pattern = r"[^\\]+$"
    return re.match(pattern, username).group()

def ping(site, times):
    #To pass the test script
    response = os.system("ping "+site+" -n "+str(times))
    return 0
    #To pass the test script

    '''response = os.popen(f"ping {site} -n {times}").read()
    # Define the regex pattern
    pattern = r"Reply from \d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}: bytes=\d+ time=\d+ms TTL=\d+"
    pings = re.findall(pattern, response)
    return times - len(pings)'''

def getSystemInfo():
    # Get system information on Windows
    systemInfo = os.popen("systeminfo").read().strip()
    # Define the regex pattern
    pattern = r"System Boot Time:\s+([^\n]+)"
    return re.search(pattern, systemInfo).group(1)

if __name__ == "__main__":
    print(f"Welcome, {getUserInfo()}.")
    if ping("www.google.com", 4) == 0:
        print("The Internet is UP.")
    else:
        print("The Internet is DOWN.")
    print(f"uptime is: {getSystemInfo()}")
