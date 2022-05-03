"""
Here there are two functions that uses the principle of *args & **kargs to print your name...!
FUNCTION- print_name() is for *args & print_kname() is for **kargs
"""
import rudrainfo

def print_name(*args):
    print("Hello "+args[0]+" "+args[1]+"...!")
def print_kname(**kargs):
    print("Hello "+kargs['fname']+" "+kargs['lname']+"...!")

print_name("Bishal","De")
print_kname(fname="Bishal",lname='De')