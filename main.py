# Do not modify these lines
__winc_id__ = '78029e0e504a49e5b16482a7a23af58c'
__human_name__ = 'modules'

# Add your code after this line
import this
import time
import math
import sys
from datetime import datetime as dt
import greet
print(this.s)

#2
def wait(seconds):
    time.sleep(seconds)

#3
def my_sin(x):
    return math.sin(x)

#4
def iso_now():
    return dt.now().strftime("%Y-%m-%dT%H:%M")

#5
def platform():
    return sys.platform

#6 Create a new file greet.py, and in that file implement a 
# function supergreeting that takes a name as an argument (str) 
# and returns a string of the form 'Hellooo...ooo, Bob!'. 
# Then import this function in main.py and write a 
# function supergreeting_wrapper that takes the 
# exact same type of argument, calls supergreeting with it and returns the result.

def supergreeting_wrapper(name):
    return greet.supergreeting(name)

if __name__ == "__main__":
    print(wait(1))
    print(my_sin(5))
    print(iso_now())
    print(platform())
    print(supergreeting_wrapper("Winc"))